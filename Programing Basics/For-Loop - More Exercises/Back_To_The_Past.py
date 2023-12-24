# 18 години и получава наследство, което се състои от X сума пари и машина на времето.
# Той решава да се върне до 1800 година, за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева.
# За всяка нечетна (1801,1803  и т.н.) ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].
#     • Наследените пари – реално число в интервала [1.00 ... 1 000 000.00]
#     • Годината, до която трябва да живее (включително) – цяло число в интервала [1801 ... 1900]
#     • Ако парите са достатъчно:
#       ◦ "Yes! He will live a carefree life and will have {N} dollars left." – където N са парите, които ще му останат.
#     • Ако парите НЕ са достатъчно:
#       ◦ "He will need {М} dollars to survive." – където M е сумата, която НЕ достига.
money = float(input())
years = int(input())

year_count = 0
total_money = money
for i in range(1800, years + 1):
    count = 0
    count += i

    if count % 2 == 0:
        total_money -= 12000
    else:
        total_money -= 12000 + (50 * (year_count + 18))
    year_count += 1

if total_money >= 0:
    print(f"Yes! He will live a carefree life and will have {total_money:.2f} dollars left.")
else:
    print(f"He will need {abs(total_money):.2f} dollars to survive.")