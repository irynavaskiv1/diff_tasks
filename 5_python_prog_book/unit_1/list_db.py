# lists
ira = ['Ira Va', 10, 1000, 'software']
vira = ['Vira Va', 20, 2000, 'hardware']
print('Ira pay is ', ira[3])

# make nested list
people = [ira, vira]
for person in people:
    print('person', person)

# get names
for person in people: print('Name is ', person[0])

# get price, return list
pays = [person[2] for person in people]
print('pays: ', pays)

# add indexing
NAME, AGE, PAY = range(3)
print('ira age:', ira[AGE])
print(PAY, ira[PAY])

# join 2 lists
names = ['ira', 'vika', 'vira']
age = [10, 20, 30]
values = list(zip(names, age))
print('values: ', values)

# add new items to db
vika = ['Vika Va', 30, 4000, 'hardware']
vita = ['Vita Va', 50, 5000, 'hardware']
villa = ['Villa Va', 60, 6000, 'hardware']
people.append(villa)
people.append(vita)
people.append(vika)
