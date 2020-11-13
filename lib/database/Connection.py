import mysql.connector

from lib.database.Config import Config


class Connection:
    def __init__(self, config: Config):
        self.conn = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )

    def getCursor(self):
        return self.conn.cursor(prepared=True,)
