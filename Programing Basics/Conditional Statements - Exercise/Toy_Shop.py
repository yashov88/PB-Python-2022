# input
trip_price = float(input())
puzzle_count = int(input())
dol_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

# logic
total = puzzle_count * 2.6
total += dol_count * 3
total += bears_count * 4.1
total += minions_count * 8.2
total += trucks_count * 2

toys_count = puzzle_count + dol_count + bears_count + minions_count + trucks_count

if toys_count >= 50:
    total -= total * 0.25
total -= total * 0.1

# output
if total >= trip_price:
    print(f"Yes! {total - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total:.2f} lv needed.")
