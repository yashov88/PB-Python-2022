is_Negative = False

while True:
    number = float(input())

    if number < 0:
        is_Negative = True

    if is_Negative:
        print("Negative number!")
        break

    print(f"Result: {number * 2:.2f}")