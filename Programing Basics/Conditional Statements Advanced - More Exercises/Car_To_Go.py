# "Summer" и "Winter" -> "Cabrio" и "Jeep"
#     • При бюджет по-малък или равен от 100лв.:
#         ◦ Класът ще е - "Economy class"
#         ◦ Според сезона колата и цената ще са:
#             ▪ Лято – Кабрио – 35% от бюджета
#             ▪ Зима – Джип – 65% от бюджета
#     • При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
#         ◦ Класът ще е - "Compact class"
#         ◦ Според сезона колата и цената ще са:
#             ▪ Лято – Кабрио – 45% от бюджета
#             ▪ Зима – Джип – 80% от бюджета
#     • При бюджет по-голям от 500лв.:
#         ◦ Класът ще е – "Luxury class"
#         ◦ За всеки сезон колата ще е джип и цената ще е:
#             ▪ 90% от бюджета
# Вход • Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
#      • Втори ред –  Сезон – текст "Summer" или "Winter"
# Изход • Първи ред – "{Вид на класа}"
#         ◦ "Economy class", "Compact class" или "Luxury class"
#       • Втори ред – "{Вид на колата} - {цена на колата}"
#         ◦ Видът на колата – "Cabrio" или "Jeep"
#         ◦ Цената трябва да е форматирана до втория знак след запетаята
budget = float(input())
season = input()

car_class = ""
type_car = ""
car_price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.80
elif budget > 500:
    car_class = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.90

print(f"{car_class}")
print(f"{type_car} - {car_price:.2f}")