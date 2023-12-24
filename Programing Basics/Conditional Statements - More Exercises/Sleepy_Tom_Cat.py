# нормата за игра на Том е 30 000  минути в година, годината има 365 дни.
#     • Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
#     • Когато почива, стопанинът му си играе с него  по 127 минути на ден.
#     • Ако времето за игра на Том е над нормата за текущата година:
#         ◦  На първия ред отпечатайте: “Tom will run away”
#         ◦  На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes more for play”
#     • Ако времето за игра на Том е под нормата за текущата година:
#         ◦ На първия ред отпечатайте: “Tom sleeps well”
#         ◦  На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes less for play”
import math

holidays = int(input())

working_days = 365 - holidays
play_in_working_days = working_days * 63
play_in_holidays = holidays * 127
total_play_time = play_in_working_days + play_in_holidays
diff = abs(total_play_time - 30000)
diff_hours = diff / 60
diff_minutes = diff % 60

if total_play_time > 30000:
    print(f"Tom will run away")
    print(f"{math.floor(diff_hours)} hours and {diff_minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{math.floor(diff_hours)} hours and {diff_minutes} minutes less for play")