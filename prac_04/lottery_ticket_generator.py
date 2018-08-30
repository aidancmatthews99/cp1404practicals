
import random

number_picks = int(input("How many 'Quick Picks'? "))
picks = []
random_number = random.randint(0, 45)
for i in range(0, number_picks):
    j = 0
    picks.append([])
    while j < 6:
        if random_number not in picks[i]:
            picks[i].append(random_number)
            j += 1
        random_number = random.randint(0, 45)


print(picks)