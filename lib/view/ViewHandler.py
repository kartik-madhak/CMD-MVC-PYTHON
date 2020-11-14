from lib.communication import *
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
        r = Request(header)
        result: Response = getRouter().sendRequest(header['form_redirect'], r)
        if result.responseType == ResponseType.error:
            print('ERROR OCCURRED FUCKER')
        else:
            self.currentView = result.view

    def render(self):
        self.currentView.render()
