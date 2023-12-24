nylon = int(input())
paint = int(input())
diluent = int(input())
hours_work = int(input())

nylon_price = 1.5 * (nylon + 2)
paint_price = 14.5 * (paint + (paint * 0.1))
diluent_price = 5 * diluent
price_of_bags = 0.4
total = nylon_price + paint_price + diluent_price + price_of_bags
price_of_workers = (total * 0.3) * hours_work
total_price = total + price_of_workers

print(total_price)