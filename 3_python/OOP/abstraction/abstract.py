from abc import ABC, abstractmethod


class Connection(ABC):

    IP = '0.0.0.0'

    @property
    @abstractmethod
    def connect(self):
        print(type(self))

    @abstractmethod
    def disconnect(self):
        print(type(self))

    @abstractmethod
    def get_status(self):
        print(type(self))

    @classmethod
    @abstractmethod
    def new_class(cls):
        pass


class SSH(Connection):

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_status(self):
        pass

    def new_class(self):
        pass


ssh = SSH()
pass
