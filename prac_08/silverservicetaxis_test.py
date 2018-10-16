from prac_08.silverservicetaxis import SilverServiceTaxi
from prac_08.taxi import Taxi
from random import randint

MENU = """q)uit, c)hoose taxi, d)rive"""
TAXIES = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    print("Let's drive!")
    print(MENU)
    choice = input('>>>').upper()
    current_taxi = None
    bill = 0
    while choice != 'Q':
        if choice == 'C':
            current_taxi = choose_taxi()
        elif choice == 'D':
            drive_taxi(current_taxi)
        else:
            print('Invalid choice')

        bill += current_taxi.get_fare()
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        choice = input('>>>').upper()

    print('Total trip cost: ${:.2f}'.format(bill))
    print("Taxis are now:")
    for i, taxi in enumerate(TAXIES):
        print("{} - {}".format(i, taxi))


def choose_taxi():
    print('Taxis available:')
    for i, taxi in enumerate(TAXIES):
        print('{} - {}'.format(i, taxi))
    valid = False
    while not valid:
        try:
            current_taxi = TAXIES[int(input('Choose taxi: '))]
            valid = True
        except ValueError:
            print('Enter a valid number')
        except IndexError:
            print('Invalid choice')
    current_taxi.start_fare()
    return current_taxi


def drive_taxi(current_taxi):
    valid = False
    while not valid:
        try:
            distance = int(input('Drive how far? '))
            if distance > 0:
                current_taxi.drive(distance)
                valid = True
            else:
                print('Distance must be > 0')
        except ValueError:
            print('Invalid distance')
    print("Your {} trip cost ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))



if __name__ == '__main__':
    main()