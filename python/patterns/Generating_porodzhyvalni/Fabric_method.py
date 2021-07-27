from __future__ import annotations
from abc import ABC, abstractmethod


class People(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def what_people_do(self) -> str:
        people_instance = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {people_instance.operation()}"
        return result


class Ira(People):
    def factory_method(self) -> Action:
        return Walk()


class Maria(People):
    def factory_method(self) -> Action:
        return Drive()


class Action(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class Walk(Action):
    def operation(self) -> str:
        return "{Result of the Walk}"


class Drive(Action):
    def operation(self) -> str:
        return "{Result of the Drive}"


def client_code(people: People) -> None:
    print(f"Client: I'm not aware of the people's class, but it still works.\n"
          f"{people.what_people_do()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(Ira())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(Maria())
