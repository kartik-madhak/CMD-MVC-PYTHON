# noinspection PyUnresolvedReferences
from datetime import datetime

import lib.logger  # do not remove it, because this makes logger subscribe to events...
from Models import User, Post
from Models.User_auth import User_auth
from lib.database import *
from lib.event import getEventHandler
from lib.model.Migration import Migrate
from lib.view.ViewHandler import ViewHandler


getEventHandler()
if __name__ == '__main__':
    # Migrate.generateTable(User)
    viewHandler = ViewHandler()
    while True:
        if viewHandler.render() == -1:  # displays and takes input from user...
            break
        viewHandler.update()  # gets new view and loads objects...
