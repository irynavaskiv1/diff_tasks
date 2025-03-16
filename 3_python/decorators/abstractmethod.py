from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


# in this step we can not create instance of class Super,  x = Super()
# because we not write logic of abstract class


class Sub(Super):
    def action(self):
        print("spam")


# now we can create instance, we have logic in abstract method


s = Sub()
s.action()
s.delegate()
