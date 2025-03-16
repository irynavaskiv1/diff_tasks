# Introspection is the ability of a program to examine the type or properties of an object at runtime
class MetaDog(type):
    def __repr__(cls):
        return "Main Dog"


class MetaPuppi(metaclass=MetaDog):
    def __init__(self, age, city, idea):
        self.age = age
        self.city = city
        self.idea = idea

    def get_idea(self):
        return self.idea


baddi = MetaPuppi(age=2, city="Lviv", idea="gav-gav")
print(type(baddi))  # Main Dog
print(type(MetaPuppi))  # <class '__main__.MetaDog'>

# get introspection dir()
print(dir(baddi))

# get introspection getattr()
print("The age is:", getattr(baddi, "age"))  # The age is: 2
print("The age is:", baddi.age)  # The age is: 2

# get introspection hasattr()
print("The age is:", hasattr(baddi, "age"))  # The age is: True
print("The age is:", hasattr(baddi, "test"))  # The age is: False
