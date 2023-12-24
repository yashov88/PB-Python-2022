#     • 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
#     • 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
#     • 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
#     • 4ти ред: брой работници – цяло число в интервала [1 … 20]
#     • Ако произведеното вино е по-малко от нужното:
#         ◦ “It will be a tough winter! More {недостигащо вино} liters wine needed.”
#             ▪ Резултатът трябва да е закръглен към по-ниско цяло число
#     • Ако произведеното вино е колкото или повече от нужното:
#         ◦ “Good harvest this year! Total wine: {общо вино} liters.”
#             ▪ Резултатът трябва да е закръглен към по-ниско цяло число
#         ◦ “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
#             ▪ И двата резултата трябва да са закръглени към по-високото цяло число
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
import math

vineyard = int(input())
grapes = float(input())
liters_vine = int(input())
workers = int(input())

area = vineyard * 0.40
vine = (area * grapes) / 2.5
diff = abs(vine - liters_vine)

if vine >= liters_vine:
    print(f"Good harvest this year! Total wine: {math.floor(vine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(diff / workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
