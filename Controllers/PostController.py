from datetime import datetime

from Models import User, Post
from Models.Post_like import Post_like
from lib.communication import *
from lib.controller import Controller
from lib.view import View


class PostController(Controller):

    @staticmethod
    def like(request: Request):
        user = request.user
        post_id = int(request.inputs['ext'][0])

        post_like: Post_like = Post_like.query().select().where('post_id', post_id).where('user_id', user.id).getOne()
        liked = False

        if post_like is None:
            liked = True
            Post_like.query().insert([user.id, post_id, datetime.today(), datetime.today()])
        else:
            post_like.delete()

        post = Post.query().select().where('id', post_id).getOne()
        view = View('post.load', {'user': user, 'post': post, 'whether_post_liked_by_user': liked}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def load(request: Request):
        user = request.user
        post_id = int(request.inputs['ext'][0])

        post = Post.query().select().where('id', post_id).getOne()

        post_like: Post_like = Post_like.query().select().where('post_id', post_id).where('user_id', user.id).getOne()

        liked = False
        if post_like is not None:
            liked = True

        if post is None:
            posts = Post.query().select().where('user_id', user.id).get()
            view = View('post.view', {'user': user, 'posts': posts, 'error': 'Incorrect index position. Please try again.'}, request.json)
        else:
            view = View('post.load', {'user': user, 'post': post, 'whether_post_liked_by_user': liked}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def show(request: Request):
        user = request.user

        posts = Post.query().select().where('user_id', user.id).get()

        view = View('post.view', {'user': user, 'posts': posts}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def show_add_form(request: Request):
        user = request.user

        view = View('post.add', {'user': user}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def add(request: Request):
        user: User = request.user
        title = request.inputs['title']
        content = request.inputs['content']
        allow_comments = 0 if request.inputs['allow_comments'] == 'n' else 1
        visibility = 0 if request.inputs['visibility'] == '0' else 1
        tags = request.inputs['tags']

        Post.query().insert([user.id, title, content, allow_comments, visibility, tags, datetime.today(),
                             datetime.today()])

        view = View('home', {'user': user}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def show_all(request: Request):
        user: User = request.user
        posts = Post.query().select().where('public_visibility', 1).sortBy('created_at', False).get()

        view = View('post.view', {'user': user, 'posts': posts}, request.json)
        return Response(ResponseType.valid, view)