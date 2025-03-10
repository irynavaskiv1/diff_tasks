class Star:
    def __init__(self):
        self.colors = {"blue": [], "white": [], "yellow": [], "orange": [], "red": []}
        self.star_and_temp = dict()

    def get_star_and_temp(self):
        while True:
            data = input('Enter star & temperature separated by ":" ')
            if data == "e":
                break
            self.name_temp = data.split(":")
            self.star_and_temp[int(self.name_temp[1])] = self.name_temp[0]
        print(self.star_and_temp)

    def adding_planet(self):
        # for _ in range(len(self.name_temp[1])):
        for _ in range(len(self.star_and_temp.keys())):
            if 0 < int(self.name_temp[1]) < 10:
                if self.name_temp[0] in self.colors.get("white"):
                    pass
                else:
                    self.colors.get("white").append(self.name_temp[0])

            elif 10 < int(self.name_temp[1]) < 22:
                if self.name_temp[0] in self.colors.get("blue"):
                    pass
                else:
                    self.colors.get("blue").append(self.name_temp[0])

            elif int(self.name_temp[1]) < 40:
                if self.name_temp[0] in self.colors.get("yellow"):
                    pass
                else:
                    self.colors.get("yellow").append(self.name_temp[0])

            elif int(self.name_temp[1]) < 49:
                if self.name_temp[0] in self.colors.get("orange"):
                    pass
                else:
                    self.colors.get("orange").append(self.name_temp[0])

            elif int(self.name_temp[1]) < 100:
                if self.name_temp[0] in self.colors.get("red"):
                    pass
                else:
                    self.colors.get("red").append(self.name_temp[0])

            else:
                print("I do know!")

        print(self.colors)


s = Star()
s.get_star_and_temp()
s.adding_planet()
