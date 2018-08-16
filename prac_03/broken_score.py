"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = receive_score()
    if score < 0 or score > 100:
        print("Invalid score")
    elif 90 > score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


def receive_score():
    return float(input("Enter score: "))


main()
