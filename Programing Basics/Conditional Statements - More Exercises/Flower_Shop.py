#     • Магнолии – 3.25 лева -> Magnolias
#     • Зюмбюли – 4 лева -> Hyacinths
#     • Рози – 3.50 лева -> Roses
#     • Кактуси – 8 лева -> Cacti
# От общата сума, Мария трябва да плати 5% данъци.
#     • Брой магнолии – цяло число в интервала [0 … 50]
#     • Брой зюмбюли – цяло число в интервала [0 … 50]
#     • Брой рози – цяло число в интервала [0 … 50]
#     • Брой кактуси – цяло число в интервала [0 … 50]
#     • Цена на подаръка – реално число в интервала [0.00 … 500.00]
#     • Ако парите СА стигнали: "She is left with {останали} leva."
#     – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).
#     • Ако парите НЕ достигат: "She will have to borrow {останали} leva."
#     – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).
import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
price_of_present = float(input())

total_sum = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.5) + (cacti * 8)
sum_left = total_sum * 0.95
diff = abs(sum_left - price_of_present)

if sum_left < price_of_present:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
else:
    print(f"She is left with {math.floor(diff)} leva.")
