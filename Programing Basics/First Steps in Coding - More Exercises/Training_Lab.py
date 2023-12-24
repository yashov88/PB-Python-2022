# input
w = float(input())
h = float(input())

# logic
wight = w * 100
length = h * 100

desk = wight // 120
row = (length - 100) // 70
number_of_places = (desk * row) - 3

# output
print(f"{number_of_places:.0f}")
