"""
Open/closed principle - Програмні сутності повинні бути відкритими для розширення, але закритими для змін.
Розширення певного класу/інтерфейсу може здійснюватись через його успадкування.
"""


class TelephoneOld:

    def __init__(self, model: str):
        self.model = model

    def get_model(self) -> str:
        return self.model + 'SomeModel'


telephone_models = [TelephoneOld('iphone'), TelephoneOld('android')]


def get_model_name(telephone_models: list):  # use type annotation

    model = []
    for models in telephone_models:
        if models.model == 'iphone':
            model.append('iphone6')
        elif models.model == 'android':
            model.append('android10')
        else:
            model = 'None'

    return model


print(get_model_name(telephone_models))


#_______________________________________________________________________________________________________________________
# Add open to add new logic


class Telephone:

    def __init__(self, model: str):
        self.model = model

    def get_model(self) -> str:
        return self.model + 'SomeModel'

    def make_processor(self):
        pass


telephone_models2 = [Telephone('iphone'), Telephone('android'), Telephone('pixel')]


class Telephone1(Telephone):
    def make_processor(self):
        print('processor2')


class Telephone2(Telephone):
    def make_processor(self):
        print('processor4')


def get_processor(telephone_models2: list):
    for tel in telephone_models2:
        print(tel.make_processor())


print(get_processor(telephone_models2))
