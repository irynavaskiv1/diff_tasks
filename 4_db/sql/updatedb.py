import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])

# Bob Smith => [Person: Bob Smith, 20000]
# Jak => [Person: Jak, 40000]
# Sue Jones => [Person: Sue Jones, 25000]

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue

db.close()
