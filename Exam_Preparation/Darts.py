#     • Името на играча - текст
# След това до получаване на команда "Retire" се четат многократно по два реда:
#     1. Поле – текст ("Single", "Double" или "Triple")
# започва с 301 точки    x1         x2           x3
#     2. Точки – цяло число в интервала [0… 100]
#     • Ако играчът е спечелил лега:
#         ◦ "{името на играча} won the leg with {успешните изстрели} shots."
#     • Ако играчът се е отказал от играта:
#         ◦ "{името на играча} retired after {неуспешни изстрели} unsuccessful shots."

name_of_player = input()
successful_shots = 0
unsuccessful_shots = 0

total_points = 301

while total_points > 0:
    command = input()

    if command == "Retire":
        print(f"{name_of_player} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    current_pints = int(input())

    if command == "Single":
        pass
    elif command == "Double":
        current_pints *= 2
    elif command == "Triple":
        current_pints *= 3

    if current_pints > total_points:
        unsuccessful_shots += 1
        continue

    total_points -= current_pints
    successful_shots += 1

if total_points == 0:
    print(f"{name_of_player} won the leg with {successful_shots} shots.")