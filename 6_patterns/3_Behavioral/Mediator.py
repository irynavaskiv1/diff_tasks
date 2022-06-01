class Monitor:

    def display_monitor(self, monitor_name):
        print(f'Monitor name is {monitor_name} !')


class Page:

    def __init__(self, name, display_monitor):
        self.name = name
        self.display_monitor = display_monitor

    def send_monitor(self):
        print(f'Monitor sent {self.display_monitor} !')

    def __str__(self):
        return self.name


if __name__ == '__main__':
    first_page = Page(name='First', display_monitor='Mac')
    second_page = Page(name='Second', display_monitor='Win')

    first_page.send_monitor()
    second_page.send_monitor()
