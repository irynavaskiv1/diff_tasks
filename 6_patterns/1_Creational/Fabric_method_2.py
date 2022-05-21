from __future__ import annotations

from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def ram(self):
        pass

    @abstractmethod
    def cpu(self):
        pass

    @abstractmethod
    def size(self):
        pass


class MAC(Laptop):

    def ram(self):
        default_value = 16
        return default_value

    def cpu(self):
        default_value = 80
        return default_value

    def size(self):
        default_value = 13
        return default_value


class Windows(Laptop):

    def ram(self):
        default_value = 8
        return default_value

    def cpu(self):
        default_value = 80
        return default_value

    def size(self):
        default_value = 18
        return default_value


m = MAC
print(m.ram)

w = Windows
print(w.ram)
