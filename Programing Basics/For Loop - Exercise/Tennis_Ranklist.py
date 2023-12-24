import math

tournament_count = int(input())
init_points = int(input())

win_count = 0
total_points = init_points
for i in range(1, tournament_count + 1):
    level = input()

    if level == "W":
        win_count += 1
        total_points += 2000
    elif level == "F":
        total_points += 1200
    elif level == "SF":
        total_points += 720

print(f"Final points: {total_points}")
avg_points = (total_points - init_points) / tournament_count
print(f"Average points: {math.floor(avg_points)}")
percent_win = win_count / tournament_count * 100
print(f"{percent_win:.2f}%")