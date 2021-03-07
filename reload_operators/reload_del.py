class Life:
    def __init__(self, name='unknown'):
        print('Hello ', name)
        self.name = name

    def __del__(self):
        print('Bye ', self.name)

ira = Life('Ira')
