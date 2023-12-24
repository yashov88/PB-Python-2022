#  "Diesel", "Gasoline" или "Gas"
# са повече или равни на 25, на конзолата да се отпечата "You have enough {вида на горивото}."
# са по-малко от 25, да се отпечата "Fill your tank with {вида на горивото}!"
# "Invalid fuel!"
fuel = input()
liters = int(input())

if fuel == "Diesel":
    if liters >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
elif fuel == "Gasoline":
    if liters >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
elif fuel == "Gas":
    if liters >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
else:
    print("Invalid fuel!")