import pymysql

from lib.database.Config import Config


class Connection:
    def __init__(self, config: Config):
        self.conn = pymysql.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )

    def getCursor(self):
        return self.conn.cursor(pymysql.cursors.DictCursor)
