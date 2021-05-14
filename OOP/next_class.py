class NextClass:
    """
    printer посилається на обєкт функції, створює обєкт всередині області
    видимості класу і буде унаслідувана всіма нащадками
    """

    def printer(self, text):
        self.text = text
        print(self.text)


# виклик через інстанс
x = NextClass()
x.printer('ira vaskiv')

# прямий виклик але треба передати інстанс!!
NextClass.printer(x, 'IRA VASKIV')

NextClass.printer('IRA VASKIV')
