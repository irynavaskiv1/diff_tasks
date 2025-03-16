from person import Person

bob = Person("Bob Smith")
print(bob)
# Person: Bob Smith, 0]

print(bob.__class__.__name__)
# Person

print(list(bob.__dict__.keys()))
# ['name', 'job', 'pay']
# атрибути - це ключі до словника

for key in bob.__dict__:
    print(key, "=>", getattr(bob, key))
