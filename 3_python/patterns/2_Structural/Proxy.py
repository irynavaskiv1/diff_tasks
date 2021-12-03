from abc import ABC, abstractmethod


class MainClass(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class Action(MainClass):

    def request(self) -> None:
        print("RealAction: Handling request.")


class ProxyAction(MainClass):

    def __init__(self, real_subject: Action) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: MainClass) -> None:
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subjects = Action()
    client_code(real_subjects)

    print("Client: Executing the same client code with a proxy:")
    real_subjects = Action()
    proxy = ProxyAction(real_subjects)
    client_code(proxy)
