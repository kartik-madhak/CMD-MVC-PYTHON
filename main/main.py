from lib.database import *

config = Config('localhost', 'root', '', 'test')
connection = Connection(config)

cursor = connection.getCursor()
cursor.execute('insert into people values (%s,%s)', ('godammn', 'godamn street'))
print(cursor)
