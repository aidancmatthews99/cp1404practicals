"""Aidan"""
MIN_LENGTH = 6


def main():
    password = get_password()

    while len(password) < MIN_LENGTH:
        print("Error! Password too short!")
        password = get_password()

    print_asterix(password)


def print_asterix(password):
    print("*" * len(password))


def get_password():
    return input("Password: ")


main()
