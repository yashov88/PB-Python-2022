number = int(input())

num_sum = 0
count = 0
for i in range(number):
    num = int(input())
    count += 1
    num_sum += num

print(f"{(num_sum / count):.2f}")
