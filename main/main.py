# noinspection PyUnresolvedReferences
import lib.logger  # do not remove it, because this makes logger subscribe to events...
from lib.database import *
from lib.event import getEventHandler
from lib.view import View
from lib.view.ViewHandler import ViewHandler
from lib.communication import *


getEventHandler()
if __name__ == '__main__':
    viewHandler = ViewHandler()
    while True:
        viewHandler.render()  # displays and takes input from user...
        viewHandler.update()  # gets new view and loads objects...
