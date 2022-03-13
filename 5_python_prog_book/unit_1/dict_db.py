# 1 way create dict
bob = {'name': 'Bob', 'age': 25, 'pay': 3000, 'job': 'dev'}
sue = {'name': 'Sue', 'age': 20, 'pay': 5000, 'job': 'qa'}
print('Bob name is: ', bob['name'])

# 2 way create dict
jack = dict(name='Jack', age=25, pay=3000)
monika = dict(name='Monika', age=22, pay=4000)
print('jack ', jack)

people = [bob, sue, jack, monika]
names = [person['name'] for person in people]
print('names: ', names)

# lists comprehension
new_name = [p['name'] for p in people if p['pay'] > 3000]
print('new_name: ', new_name)

new_age = [p['age'] ** 2 if p['age'] >= 20 else p['age'] for p in people]
print('new_age: ', new_age)

G = (p['age'] for p in people if p['name'] == 'Jack')
print('Jack age: ', next(G))

# nested dict
bob2 = {'name': {'first': 'Bob2', 'second': 'Smith'},
        'age': 43,
        'job': ['dev', 'qa'],
        'pay': (1000, 2000, 3000)}
print('Bob2 first name: ', bob2['name']['first'])
for job in bob2['job']: print(job)

# create db
db = {}
db['bob'] = bob
db['sue'] = sue
db['jack'] = jack
db['monika'] = monika

# make changes in db
db['bob']['age'] = 100

for key in db:
    print(key, ' => ', db[key]['age'])
