from Models import User


class Request:
    def __init__(self, json):
        self.json = json
        self.inputs = json['inputs'] if 'inputs' in json else None
        self.user = self.getAuthUser()

    def getAuthUser(self) -> User:
        if 'user_id' not in self.json:
            return None
        return User.query().select().where('id', self.json['user_id']).getOne()
