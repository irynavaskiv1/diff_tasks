class MakePhoto:
    def make_photo(self):
        print('MakePhoto:make_photo')


class Call:
    def call(self):
        print('Call:call')


class Chate:
    def chatting(self):
        print('Chate:chatting')


class MyPhone:

    def __init__(self):
        self.make_photo_my = MakePhoto()
        self.call_my = Call()
        self.chatting_my = Chate()

    def use_my_phone(self):
        self.make_photo_my.make_photo()
        self.call_my.call()
        self.chatting_my.chatting()


if __name__ == "__main__":

    phone = MyPhone()
    phone.use_my_phone()
