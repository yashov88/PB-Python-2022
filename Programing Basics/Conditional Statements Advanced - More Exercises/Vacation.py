#     • При бюджет по-малък или равен от 1000лв.:
#         ◦ Настаняване в "Camp"
#         ◦ Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
#             ▪ Лято – Аляска – 65% от бюджета
#             ▪ Зима – Мароко – 45% от бюджета
#     • При бюджет по-голям от 1000лв. и по-малък или равен от 3000лв.:
#         ◦ Настаняване в "Hut"
#         ◦ Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
#             ▪ Лято – Аляска – 80% от бюджета
#             ▪ Зима – Мароко – 60% от бюджета
#     • При бюджет по-голям от 3000лв.:
#         ◦ Настаняване в "Hotel"
#         ◦ Според сезона локацията ще е една от следните и ще струва 90% от бюджета:
#             ▪ Лято – Аляска -> Alaska
#             ▪ Зима – Мароко -> Morocco
#     • Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
#     • Втори ред –  Сезон – текст "Summer" или "Winter"
# "{локацията} – {мястото за настаняване} – {цената}"
budget = float(input())
season = input()

type_place = ""
location = ""
money_pay = 0

if budget <= 1000:
    type_place = "Camp"
    if season == "Summer":
        location = "Alaska"
        money_pay = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        money_pay = budget * 0.45
elif 1000 < budget <= 3000:
    type_place = "Hut"
    if season == "Summer":
        location = "Alaska"
        money_pay = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        money_pay = budget * 0.60
elif budget > 3000:
    type_place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        money_pay = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        money_pay = budget * 0.90

print(f"{location} - {type_place} - {money_pay:.2f}")

