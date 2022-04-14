class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")


class Parrot(Bird):
    def flight(self):
        return "Parrots can fly"


class Penguin(Bird):
    def flight(self):
        return "Penguins do not fly"


obj_parr = Parrot()
print('obj_parr.flight()', obj_parr.flight())

obj_peng = Penguin()
print('obj_peng.flight()', obj_peng.flight())
