class Grabber:
    def __init__(self):
        self.name = "ira"
        self._user = "username"
        self.__password = "password"

    def show_password(self):
        print(self.__password)


gr = Grabber()
print("gr.name", gr.name)
print("gr._user", gr._user)
# print(gr.__password)  # AttributeError: 'Grabber' object has no attribute '__password'


print("gr.__dict__", gr.__dict__)
print(
    "gr._Grabber__password", gr._Grabber__password
)  # AttributeError: 'Grabber' object has no attribute '__password'
print(gr.show_password())
