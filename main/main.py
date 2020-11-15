# noinspection PyUnresolvedReferences
import lib.logger  # do not remove it, because this makes logger subscribe to events...
from Models import User, Post
from lib.database import *
from lib.event import getEventHandler
from lib.model.Migration import Migrate
from lib.view.ViewHandler import ViewHandler


getEventHandler()
if __name__ == '__main__':
    Migrate.generateTable(User)
    Migrate.generateTable(Post)
    # viewHandler = ViewHandler('home')
    # while True:
    #     viewHandler.render()  # displays and takes input from user...
    #     viewHandler.update()  # gets new view and loads objects...
