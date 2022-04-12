class Sykhiv:
    def __init__(self, street, park):
        self.street = street
        self.park = park


from dataclasses import dataclass


@dataclass
class SykhivNew:
    street_new: str
    park_new: str


# create instance
s = SykhivNew(street_new='Santa', park_new='Forest')
print(s.park_new)
