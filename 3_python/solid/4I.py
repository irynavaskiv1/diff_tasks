"""
Багато спеціалізованих інтерфейсів краще за один універсальний. Інтерфейс може бути поділений на спеціалізовані
ще на стадії проектування, заради майбутньої гнучкості програмних компонентів.
"""


class Shape:
    def draw(self):
        raise NotImplemented


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass
