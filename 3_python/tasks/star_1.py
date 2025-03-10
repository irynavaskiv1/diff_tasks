class Star:
    def __init__(self):
        self.star_and_temp = dict()

    def get_star_and_temp(self):
        while True:
            data = input('Enter star & temperature separated by ":" ')
            if data == "e":
                break
            name_temp = data.split(":")
            self.star_and_temp[int(name_temp[1])] = name_temp[0]
        print(self.star_and_temp)

    def print_color_and_star(self):
        color_and_stars = []
        for temp in self.star_and_temp:
            if int(temp) < 0:
                color_and_stars.append({"white": self.star_and_temp[temp]})
            elif 0 <= int(temp) < 22:
                color_and_stars.append({"blue": self.star_and_temp[temp]})
            elif 22 <= int(temp) < 40:
                color_and_stars.append({"yellow": self.star_and_temp[temp]})
            elif 40 <= int(temp) < 49:
                color_and_stars.append({"orange": self.star_and_temp[temp]})
            elif 49 <= int(temp) < 100:
                color_and_stars.append({"red": self.star_and_temp[temp]})
            else:
                color_and_stars.append({"I do not number": self.star_and_temp[temp]})
        print(color_and_stars)


s = Star()
s.get_star_and_temp()
s.print_color_and_star()
