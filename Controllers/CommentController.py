from datetime import datetime
from typing import List

from Models import User, Post
from Models.Comment import Comment
from Models.Post_like import Post_like
from lib.communication import *
from lib.controller import Controller
from lib.view import View


class CommentController(Controller):
    @staticmethod
    def add_form(request: Request):
        user = request.user
        post_id = int(request.inputs['ext'][0])

        post = Post.query().select().where('id', post_id).getOne()

        view = View('comment.add', {'user': user, 'post': post}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def add(request: Request):
        user = request.user
        post_id = int(request.inputs['ext'][0])
        content = request.inputs['content']

        Comment.query().insert([post_id, user.id, content, datetime.today(), datetime.today()])

        post = Post.query().select().where('id', post_id).getOne()

        post_like: Post_like = Post_like.query().select().where('post_id', post_id).where('user_id', user.id).getOne()

        liked = False
        if post_like is not None:
            liked = True

        view = View('post.load', {'user': user, 'post': post, 'whether_post_liked_by_user': liked}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def view(request: Request):
        user = request.user
        post_id = int(request.inputs['ext'][0])

        post = Post.query().select().where('id', post_id).getOne()
        comments: List[Comment] = Comment.query().select().where('post_id', post_id).sortBy('created_at', False).get()

        view = View('comment.load', {'user': user, 'post': post, 'comments': comments}, request.json)
        return Response(ResponseType.valid, view)