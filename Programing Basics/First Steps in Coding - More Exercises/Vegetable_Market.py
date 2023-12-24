# input
price_vegetables = float(input())
price_fruits = float(input())
kilograms_vegetables = int(input())
kilograms_fruits = int(input())

# logic
sum_vegetables = (price_vegetables * kilograms_vegetables) * 1.0
sum_fruits = (price_fruits * kilograms_fruits) * 1.0
total_sum = sum_vegetables + sum_fruits
euro = total_sum / 1.94

# output
print(f"{euro:.2f}")
