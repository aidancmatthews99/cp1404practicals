
import random

number_picks = int(input("How many 'Quick Picks'? "))
picks = []
random_number = random.randint(0, 45)

picks = []

# for j in range(0, number_picks):
#     for i in range(0, 6):
#         while random_number in picks:
#             random_number = random.randint(0, 45)
#         picks.append(random_number)

print(picks)