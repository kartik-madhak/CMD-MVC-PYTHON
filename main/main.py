# noinspection PyUnresolvedReferences
import lib.logger  # do not remove it, because this makes logger subscribe to events...
from lib.database import *
from lib.view import View

if __name__ == '__main__':
    config = Config('localhost', 'root', '', 'test')
    connection = Connection(config)
    cursor = connection.getCursor()
    cursor.execute('select * from people')
    people = cursor.fetchall()
    people = {'people': people}
    print(View('').parse(people))
    print(people)
