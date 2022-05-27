import random
from abc import ABCMeta, abstractmethod


class MyHandler(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def handler():
        "Need to implement"


class FirstStep(MyHandler):

    @staticmethod
    def handler(step):
        print(f'FirstStep:handler step is {step}')
        test = random.randint(1, 2)
        if test == 1:
            concrete_step = step + 20
            finish_step = SecondStep().handler(step=concrete_step)
        elif test == 2:
            concrete_step = step - 20
            finish_step = SecondStep().handler(step=concrete_step)
        return finish_step


class SecondStep(MyHandler):

    @staticmethod
    def handler(step):
        print(f'SecondStep:handler step is {step}')
        test = random.randint(4, 5)
        if test == 1:
            concrete_step = step + 20
            finish_step = FirstStep().handler(step=concrete_step)
        else:
            concrete_step = step - 20
            finish_step = FirstStep().handler(step=concrete_step)
        return finish_step


class Chain:

    @staticmethod
    def start(step):
        return FirstStep().handler(step)


chain = Chain()
out = chain.start(1)
print(f'Finish result: {out}')
