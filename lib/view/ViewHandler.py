from lib.communication.router import Router
from lib.view.View import View
from typing import TypedDict
from lib.communication import *


class ViewHandler:
    def __init__(self, initLink: str = '', initObjects: TypedDict = {}):
        self.currentView = View(initLink, initObjects)

    def update(self):
        header = self.currentView.header
        header['handler'] = self
        try:
            header['method']
        except KeyError:
            header['method'] = 'GET'
        request = Request(header)
        router = Router()

    def render(self):
        self.currentView.render()
