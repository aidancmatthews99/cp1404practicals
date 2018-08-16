
print("\n   ASCII Number Converter \n\n")

letter = input("Enter the character: ")
print("The ASCII code for {} is: {}.\n".format(letter, ord(letter)))
number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is : {}.\n".format(number, chr(number)))
