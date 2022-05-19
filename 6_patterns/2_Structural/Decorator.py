class Close:
    def __init__(self, close):
        self._close = close

    def get_close(self):
        return self._close


class CloseTrousers:
    def __init__(self, trousers):
        self._trousers = trousers

    def get_close(self):
        return f'Trousers: {self._trousers.get_close()}'


class CloseShirt:
    def __init__(self, shirt):
        self._shirt = shirt

    def get_close(self):
        return f'Shirt: {self._shirt.get_close()}'


if __name__ == '__main__':

    before_close = Close(close="Ira's close")
    after_close = CloseShirt(CloseTrousers(Close("Ira's close")))

    print("before :", before_close.get_close())
    print("after :", after_close.get_close())
