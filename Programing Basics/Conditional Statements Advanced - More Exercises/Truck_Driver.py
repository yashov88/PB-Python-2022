#                               Пролет/Есен         Лято        Зима
# км на месец <= 5000           0.75 лв./км     0.90 лв./км     1.05 лв./км
# 5000 < км на месец <= 10000   0.95 лв./км     1.10 лв./км     1.25 лв./км
# 10000 < км на месец <= 20000       1.45 лв./км – за който и да е сезон
#     • Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
#     • Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]
# Заплатата на шофьора след данъците, форматирана до втория знак след десетичната запетая.

season = input()
kilometers = float(input())

salary = 0

if season == "Spring" or season == "Autumn":
    if kilometers <= 5000:
        salary = ((kilometers * 0.75) * 4) * 0.9
    elif 5000 < kilometers <= 10000:
        salary = ((kilometers * 0.95) * 4) * 0.9
    elif 10000 < kilometers <= 20000:
        salary = ((kilometers * 1.45) * 4) * 0.9
elif season == "Summer":
    if kilometers <= 5000:
        salary = ((kilometers * 0.90) * 4) * 0.9
    elif 5000 < kilometers <= 10000:
        salary = ((kilometers * 1.10) * 4) * 0.9
    elif 10000 < kilometers <= 20000:
        salary = ((kilometers * 1.45) * 4) * 0.9
elif season == "Winter":
    if kilometers <= 5000:
        salary = ((kilometers * 1.05) * 4) * 0.9
    elif 5000 < kilometers <= 10000:
        salary = ((kilometers * 1.25) * 4) * 0.9
    elif 10000 < kilometers <= 20000:
        salary = ((kilometers * 1.45) * 4) * 0.9


print(f"{salary:.2f}")
