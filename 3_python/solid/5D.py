"""
Залежності всередині системи будуються на основі абстракцій, що не повинні залежати від деталей; навпаки,
деталі мають залежати від абстракцій. Класи верхніх рівнів не мають залежати від класів нижчих рівнів.
"""


class NewsPerson:
    """This is a high-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(NewsPaper().publish(news=news))


class NewsPaper:
    """This is a low-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(f"{news} Hello newspaper")


person = NewsPerson()
print(person.publish("News Paper"))
