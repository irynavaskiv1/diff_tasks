# Client
class Glasses:

    default_input_glasses = 'from the computer'

    @classmethod
    def using_glasses(cls, input_glasses):
        if input_glasses == cls.default_input_glasses:
            print(f'My glasses is {input_glasses}!')
        elif input_glasses == 'from the sun':
            print('My glasses is from the sun!')
        else:
            print('I don*t have a glasses!')

    def destination(self, my_glasses):
        """Charge the phone with the given input voltage."""
        self.using_glasses(my_glasses)


# Adapter
class Iras:
    output_glasses = None


class IraSunGlasses:
    output_glasses = 'from the sun'


class IraComputerGlasses:
    output_glasses = 'from the computer'


# Adaptee
glasses = Glasses()
glasses.destination(IraComputerGlasses.output_glasses)
glasses.destination(IraSunGlasses.output_glasses)

# My glasses is from the computer
# My glasses is from the sun
