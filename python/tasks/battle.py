from random import randrange


class Battle:

    def get_name_and_ships(self):
        """ This function takes name and number of ships from players."""
        first_name = input('Enter name of first player: ')
        while True:
            try:
                int(input('{}, please, enter the number of ships fom 1 '
                          'to 10. : '.format(first_name)))
                break
            except ValueError:
                print('{}, please, enter correct number of ships!'.
                      format(first_name))
                continue

        second_name = input('Enter name of second player: ')
        while True:
            try:
                int(input('{}, please, enter the number of ships fom 1 '
                          'to 10. : '.format(second_name)))
                break
            except ValueError:
                print('{}, please, enter correct number of ships!'.
                      format(second_name))
                continue

    def take_power_away(self):
        """ This function calculated the power. """
        print('Press "1" if you first player and "2" if second,'
              ' when you want to shoot.')

        first_power_status = [100]
        second_power_status = [100]

        while first_power_status[-1] or second_power_status[-1] != 0:
            press_enter = input('Enter value, please: ')
            if press_enter == '1':
                second_power_status.append(
                    second_power_status[-1] - randrange(0, 100, 25))
                print('You take {} power from second player!'.
                      format(100 - second_power_status[-1]))
                if second_power_status[-1] == 0:
                    print('Game is over {} player win!'.format('first'))
                    break

            elif press_enter == '2':
                first_power_status.append(
                    first_power_status[-1] - randrange(0, 100, 25))
                print('You take {} power from first player!'.
                      format(100 - first_power_status[-1]))
                if first_power_status[-1] == 0:
                    print('Game is over {} player win!'.format('second'))
                    break
            else:
                print('Please, enter the correct number!')


b = Battle()
b.get_name_and_ships()
b.take_power_away()
