from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class IraHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Ira":
            return f"Girl: My name is {request}. I am present."
        else:
            return super().handle(request)


class TarasHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Taras":
            return f"Guy: My name is {request}. I am present."
        else:
            return super().handle(request)


class MariaHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Maria":
            return f"Girl: My name is {request}. I am present."
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:

    for name in ["Maria", "Ira", "Taras"]:
        print(f"\nClient: Is {name} present today?")
        result = handler.handle(name)
        if result:
            print(f"{result}", end="")
        else:
            print(f"{name} is not present.", end="")


if __name__ == "__main__":
    ira = IraHandler()
    taras = TarasHandler()
    maria = MariaHandler()

    ira.set_next(ira).set_next(maria)
    client_code(taras)
    client_code(maria)
