import shelve

from python.OOP.person import Manager, Person

bob = Person('Bob Smith', 'QA', 20000)
sue = Person('Sue Jones', 'AQA', 25000)
jak = Manager('Jak', pay=40000)

db = shelve.open('persondb')
for object in (bob, sue, jak):
    db[object.name] = object
db.close()
