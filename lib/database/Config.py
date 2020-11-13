class Config(object):

    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        """

        :param host:
        :param user:
        :param password:
        :param database:
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
