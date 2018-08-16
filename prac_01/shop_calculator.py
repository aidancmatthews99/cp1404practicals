
number_items = int(input("Number of items: "))
total = 0.00
item_price = 0.00

while number_items <= 0:
    number_items = int(input("Invalid number of items! \nNumber of items: "))

for i in range(0, number_items):
    item_price = int(input("Price of item: "))
    while item_price < 0:
        item_price = int(input("Invalid price! \nPrice of item: "))
    total += item_price
if total > 100:
    total *= 0.90

print("Total price for {} item(s) ${:.2f}".format(number_items, total), end="")
