type_ticket = input()
rows = int(input())
cols = int(input())

all_seats = rows * cols

price = 0

if type_ticket == "Premiere":
    price = 12
elif type_ticket == "Normal":
    price = 7.5
elif type_ticket == "Discount":
    price = 5

income = all_seats * price

print(f"{income:.2f} leva")
