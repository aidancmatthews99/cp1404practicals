#
# # Loop 1
# for i in range(1, 21, 2):
#     print(i, end=" ")
# print()
#
# # Loop 2
# for i in range(0, 101, 10):
#     print(i, end=" ")
# print()
#
# # Loop 3
# for i in range(20, 0, -1):
#     print(i, end=" ")
# print()
# print()
#
# # Loop 4
# stars = int(input("Number of stars: "))
#
# for i in range(0, stars):
#     print("*", end="")
# print()
#
# for i in range(0, stars + 1):
#     print("*" * i)

# Loop 5
sales = float(input("Enter Sales: "))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, ". Pretty cool bonus. ", sep='-')
    sales = float(input("Enter Sales: "))
