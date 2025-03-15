class Grabber:

    """Class for understand class and instance attribute."""

    USER = 'user_ira'

    def __init__(self):
        self.__class__.USER = 'user_ira2'  # змінюємо змінну (константу) класу

    @classmethod
    def change_pass(cls, pwd='user4'):
        """відразу підстановка під час виклику функції, має посилання на обєкти класу"""
        cls.USER = pwd
        print(cls.USER)

    @staticmethod
    def check_connection(server):
        """звичайна ф-ція, яка має логічну прив'язку, немає посилання на інстанси класу"""
        print(f'Connection {server} to server')


# get class variable
print(Grabber.USER)  # user_ira

# get instance variable
g = Grabber()
print(g.USER)  # user_ira2

# get method variable
print(g.change_pass(pwd='user_ira5'))  # user_ira5
