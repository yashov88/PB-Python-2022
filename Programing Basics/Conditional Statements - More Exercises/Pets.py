#     • Първи ред – брой дни – цяло число в интервал [1…5000]
#     • Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
#     • Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
#     • Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
#     • Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
#     • Ако оставената храна Е достатъчна:
#         ◦ "{килограма остатък} kilos of food left."
#             ▪ Резултатът трябва да е закръглен към по-ниското цяло число
#     • Ако оставената храна НЕ Е достатъчна:
#         ◦ “{килограма недостигат} more kilos of food are needed.”
# Резултатът трябва да е закръглен към по-високото цяло число
import math

days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

all_food_needed = (days * dog_food) + (days * cat_food) + ((days * turtle_food) / 1000)
diff = abs(food_left - all_food_needed)

if food_left > all_food_needed:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
    