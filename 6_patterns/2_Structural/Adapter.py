class Name:

    def create_name(self) -> str:
        self.name = 'Ira'
        return f'Name is {self.name}'


class Surname:

    def create_surname(self) -> str:
        self.surname = 'Vaskiv'
        return f'Surname is {self.surname}'


class NameSurname(Name, Surname):

    def return_namesurname(self):
        self.all_data = self.name + self.surname
        return f'All data is {self.all_data}'


def client_code(name: "Name") -> None:
    print(name.create_name(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    name = Name()
    client_code(name)

    surname = Surname()
    print("Client: The Adaptee class has a weird interface.")
    print(f"Adaptee: {surname.create_surname()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Name()
    client_code(adapter)
