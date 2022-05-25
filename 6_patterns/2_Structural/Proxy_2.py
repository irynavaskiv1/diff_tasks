class SingleBook:

    def reading_book(self):
        print('Reading single book...')


class BookProxy:

    def __init__(self):
        self.pages = 1000
        self.quntity = 3
        self.book = None

    def reading_book(self):
        print("Proxy in action.")
        if self.pages > 900:
            print('Reading a book!')
            self.book = SingleBook()
            self.book.reading_book()
        else:
            print('Not reading a book!')


if __name__ == '__main__':
    book_proxy = BookProxy()
    book_proxy.reading_book()
