num_of_pens = int(input())
num_of_markers = int(input())
liters_of_detergent = int(input())
percent = int(input())
price_of_pens = num_of_pens * 5.8
price_of_markers = num_of_markers * 7.2
price_of_detergent = liters_of_detergent * 1.2
sum = price_of_pens + price_of_markers + price_of_detergent
discount = sum * (percent / 100)
total_sum = sum - discount
print(total_sum)
