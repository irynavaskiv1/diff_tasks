import shelve
from person import Person
from manager import Manager

bob = Person(name='Bob', age=30, pay=3000, job='Dev')
sue = Person(name='Sue', age=20, pay=5000, job='QA')
tom = Manager(name='Tom Tomuch', age=30, pay=3000, job='Manager')

db = shelve.open('class-db-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

db.close()






