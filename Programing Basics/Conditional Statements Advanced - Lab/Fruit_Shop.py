product = input()  # banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
day_of_week = input()  # Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
quantity = float(input())

price = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if product == "banana":
        price = 2.50
        print(f"{price * quantity:.2f}")
    elif product == "apple":
        price = 1.20
        print(f"{price * quantity:.2f}")
    elif product == "orange":
        price = 0.85
        print(f"{price * quantity:.2f}")
    elif product == "grapefruit":
        price = 1.45
        print(f"{price * quantity:.2f}")
    elif product == "kiwi":
        price = 2.70
        print(f"{price * quantity:.2f}")
    elif product == "pineapple":
        price = 5.50
        print(f"{price * quantity:.2f}")
    elif product == "grapes":
        price = 3.85
        print(f"{price * quantity:.2f}")
    else:
        print("error")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if product == "banana":
        price = 2.70
        print(f"{price * quantity:.2f}")
    elif product == "apple":
        price = 1.25
        print(f"{price * quantity:.2f}")
    elif product == "orange":
        price = 0.90
        print(f"{price * quantity:.2f}")
    elif product == "grapefruit":
        price = 1.60
        print(f"{price * quantity:.2f}")
    elif product == "kiwi":
        price = 3.0
        print(f"{price * quantity:.2f}")
    elif product == "pineapple":
        price = 5.60
        print(f"{price * quantity:.2f}")
    elif product == "grapes":
        price = 4.20
        print(f"{price * quantity:.2f}")
    else:
        print("error")
else:
    print("error")
