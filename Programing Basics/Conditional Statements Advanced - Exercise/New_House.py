# • Ако бюджетът им е достатъчен - "";
# • Ако бюджета им е НЕ достатъчен - "".
type_flowers = input() # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
#                           5       3.80        2.80        3               2.50
count_flowers = int(input())
budget = int(input())

total_sum = 0

if type_flowers == "Roses":
    total_sum = count_flowers * 5
    if count_flowers > 80:
        total_sum = total_sum * 0.9
elif type_flowers == "Dahlias":
    total_sum = count_flowers * 3.8
    if count_flowers > 90:
        total_sum = total_sum * 0.85
elif type_flowers == "Tulips":
    total_sum = count_flowers * 2.8
    if count_flowers > 80:
        total_sum = total_sum * 0.85
elif type_flowers == "Narcissus":
    total_sum = count_flowers * 3
    if count_flowers < 120:
        total_sum = total_sum * 1.15
elif type_flowers == "Gladiolus":
    total_sum = count_flowers * 2.5
    if count_flowers < 80:
        total_sum = total_sum * 1.2

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
