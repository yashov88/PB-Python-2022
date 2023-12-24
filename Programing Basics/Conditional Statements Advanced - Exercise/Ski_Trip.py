# вид помещение               по-малко от 10 дни           между 10 и 15 дни            повече от 15 дни
# room for one person         не ползва намаление          не ползва намаление          не ползва намаление
# apartment                   30% от крайната цена         35% от крайната цена         50% от крайната цена
# president apartment         10% от крайната цена         15% от крайната цена         20% от крайната цена
#
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление
# Атанас добавя 25% от нея. Ако оценката му е негативна приспада от цената 10%.

days_stay = int(input())
room = input()   # "room for one person", "apartment" или "president apartment"
rating = input()    # "positive"  или "negative"

room_for_one = 18.00
apartment = 25.00
president_ap = 35.00
rent = 0

if room == "room for one person":
    rent = (days_stay - 1) * room_for_one
elif room == "apartment":
    if days_stay < 10:
        rent = ((days_stay - 1) * apartment) * 0.70
    elif 10 < days_stay <= 15:
        rent = ((days_stay - 1) * apartment) * 0.65
    elif days_stay > 15:
        rent = ((days_stay - 1) * apartment) * 0.50
    else:
        rent = (days_stay - 1) * apartment
elif room == "president apartment":
    if days_stay < 10:
        rent = ((days_stay - 1) * president_ap) * 0.90
    elif 10 < days_stay <= 15:
        rent = ((days_stay - 1) * president_ap) * 0.85
    elif days_stay > 15:
        rent = ((days_stay - 1) * president_ap) * 0.80
    else:
        rent = (days_stay - 1) * president_ap

final_price = 0

if rating == "positive":
    final_price = rent * 1.25
elif rating == "negative":
    final_price = rent * 0.90

print(f"{final_price:.2f}")
