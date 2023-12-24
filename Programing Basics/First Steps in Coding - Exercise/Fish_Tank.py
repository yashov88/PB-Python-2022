length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
total_liters = volume / 1000
acc_total = total_liters * (percent / 100)
result = total_liters - acc_total

print(result)
