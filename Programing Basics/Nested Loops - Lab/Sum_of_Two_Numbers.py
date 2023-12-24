first_num = int(input())
second_num = int(input())
magic_num = int(input())

counter = 0
isFound = False

for a in range(first_num, second_num + 1):
    for b in range(first_num, second_num + 1):
        counter += 1

        if a + b == magic_num:
            print(f"Combination N:{counter} ({a} + {b} = {magic_num})")
            isFound = True

    if isFound:
        break

if not isFound:
    print(f"{counter} combinations - neither equals {magic_num}")
