age = int(input())
price_wash_machine = float(input())
toy_price = int(input())

count_toys = 0
money = 0
total_sum = 0
brother_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        money += 10
        total_sum += money
        brother_count += 1

result = ((count_toys * toy_price) + total_sum) - brother_count

diff = abs(price_wash_machine - result)

if result >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
