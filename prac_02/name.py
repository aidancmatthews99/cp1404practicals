
FILENAME = "name.txt"

filename = open(FILENAME, "w")

name = input("What is your name? ")
print("Your name is {}".format(name), file=filename)

filename.close()