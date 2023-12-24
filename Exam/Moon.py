import math

speed = float(input())
gas = float(input())

total_distance = 384400 * 2
time = (total_distance / speed)
total_time = time + 3
need_gas = (gas * total_distance) / 100

print(math.ceil(total_time))
print(int(need_gas))