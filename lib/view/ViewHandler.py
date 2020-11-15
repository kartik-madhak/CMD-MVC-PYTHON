from lib.communication import *
from lib.view.View import View
from typing import TypedDict
from lib.communication import *


class ViewHandler:
    def __init__(self, initLink: str = ''):
        header = {'method': 'GET', 'form_redirect': initLink}
        r = Request(header)
        response: Response = getRouter().sendRequest(r)

        if response.responseType == ResponseType.error:
            if response.view is None:
                self.currentView = View(self.currentView.path, {'error': response.msg})
            else:
                self.currentView = View(response.view.path, {'error': response.msg})
        else:
            self.currentView = response.view

    def update(self):
        header = self.currentView.header
        try:
            header['method']
        except KeyError:
            header['method'] = 'GET'
        r = Request(header)
        result: Response = getRouter().sendRequest(r)

        if result.responseType == ResponseType.error:
            self.currentView = View(self.currentView.path, {'error': result.msg})
        else:
            self.currentView = result.view

    def render(self):
        self.currentView.render()
