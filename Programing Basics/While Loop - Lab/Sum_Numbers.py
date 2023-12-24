constant_number = int(input())
sum_numbers_count = 0

while True:
    current_num = int(input())
    sum_numbers_count += current_num

    if sum_numbers_count >= constant_number:
        print(sum_numbers_count)
        break
