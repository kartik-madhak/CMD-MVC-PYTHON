from lib.communication import *


class ViewHandler:
    def __init__(self, initLink: str = ''):
        header = {'form_redirect': initLink}
        self.currentView = self.getResponseView(header)

    def update(self):
        header = self.currentView.header
        self.currentView = self.getResponseView(header)

    @staticmethod
    def getResponseView(header):
        request: Request = Request(header)
        response: Response = getRouter().sendRequest(request)

        return response.view

    def render(self):
        self.currentView.render()
