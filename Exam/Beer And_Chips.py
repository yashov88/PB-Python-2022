import math
#     • На първия ред - името на футболният фен – текст
#     • На втория ред - предвиденият бюджет  – реално число в диапазона [1.0… 100 000.0]
#     • На третия ред - брой бутилки бира – цяло число в диапазона [1… 100 000]
#     • На четвърти ред - брой пакети чипс – цяло число в диапазона [1… 100 000]
#     • Ако бюджетът е достатъчен за закупуването на продуктите:
#  "{име} bought a snack and has {останали пари} leva left."
#     • Ако бюджетът НЕ е достатъчен:
# "{име} needs {нужни пари} more leva!"
# Резултатът да се форматира до втория знак след десетичната запетая.
# Цената на една бира е 1.20 лв., а цената на един пакет чипс е равна на 45% от общата стойност на закупените бири

name = input()
budget = float(input())
beer_bottles = int(input())
chips = int(input())

beer_price = 1.2 * beer_bottles
price_of_chips = beer_price * 0.45
total_price_chips = math.ceil(price_of_chips * chips)
total_amount = beer_price + total_price_chips
change = abs(budget - total_amount)


if total_amount <= budget:
    print(f"{name} bought a snack and has {change:.2f} leva left.")
else:
    print(f"{name} needs {change:.2f} more leva!")

