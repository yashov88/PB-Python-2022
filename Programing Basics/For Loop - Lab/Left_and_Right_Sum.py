number = int(input())

left_sum = 0
right_sum = 0

for i in range(number):  # 1, number + 1
    current_num = int(input())
    left_sum += current_num

for j in range(number):  # 2, number + 2
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
