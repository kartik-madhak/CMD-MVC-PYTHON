# noinspection PyUnresolvedReferences
from datetime import datetime
from os import system

from Models.Notification import Notification
from lib.model.Migration import Migrate
from lib.view.ViewHandler import ViewHandler


if __name__ == '__main__':
    # Migrate.generateTable(Notification)
    viewHandler = ViewHandler()
    while True:
        if viewHandler.render() == -1:  # displays and takes input from user...
            break
        viewHandler.update()  # gets new view and loads objects...
        system('cls')
