# Electricity Bill Calculator
print("\n  Electricity Bill Calculator \n \n")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_choice = float(input("Which tariff? 11 or 31: "))

while tariff_choice != 11 and tariff_choice != 31:
    tariff_choice = int(input("Invalid input! Choose 11 or 31: "))
    if tariff_choice != 11 and tariff_choice != 31:
        is_error = True

daily_use = float(input("Enter daily use: "))
billing_days = float(input("Enter number of billing days: "))

if tariff_choice == 11:
    print("Estimated Bill: ${:.2f}".format(TARIFF_11 * daily_use * billing_days ))
else:
    print("Estimated Bill: ${:.2f}".format(TARIFF_31 * daily_use * billing_days ))


