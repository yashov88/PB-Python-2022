n = int(input())

max_num = 0
total_sum = 0

for i in range(n):
    current_num = int(input())

    total_sum += current_num

    if current_num > max_num:
        max_num = current_num

other_sum = total_sum - max_num

if max_num == other_sum:
    print("Yes")
    print(f"Sum = {other_sum}")
else:
    print("No")
    diff = abs(other_sum - max_num)
    print(f"Diff = {diff}")
