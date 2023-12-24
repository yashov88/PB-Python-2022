#     • IP – 499.99 лева.
#     • Normal – 249.99 лева.
#       От 1 до 4 – 75% от бюджета.
#     • От 5 до 9 – 60% от бюджета.
#     • От 10 до 24 – 50% от бюджета.
#     • От 25 до 49 – 40% от бюджета.
#     • 50 или повече – 25% от бюджета.
#     • На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
#     • На втория ред е категорията – "VIP" или "Normal"
#     • На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
#     • Ако бюджетът е достатъчен:
#         ◦ "Yes! You have {останалите пари на групата} leva left."
#     • Ако бюджетът НЕ Е достатъчен:
#         ◦ "Not enough money! You need {сумата, която не достига} leva."
budget = float(input())
category = input()
people_in_group = int(input())

vip_price = 0
normal_price = 0
travel = 0
diff = 0

if people_in_group <= 4:
    travel = budget * 0.25
    if category == "VIP":
        vip_price = people_in_group * 499.99
        diff = travel - vip_price
    elif category == "Normal":
        normal_price = people_in_group * 249.99
        diff = travel - normal_price
elif people_in_group <= 9:
    travel = budget * 0.40
    if category == "VIP":
        vip_price = people_in_group * 499.99
        diff = travel - vip_price
    elif category == "Normal":
        normal_price = people_in_group * 249.99
        diff = travel - normal_price
elif people_in_group <= 24:
    travel = budget * 0.50
    if category == "VIP":
        vip_price = people_in_group * 499.99
        diff = travel - vip_price
    elif category == "Normal":
        normal_price = people_in_group * 249.99
        diff = travel - normal_price
elif people_in_group <= 49:
    travel = budget * 0.60
    if category == "VIP":
        vip_price = people_in_group * 499.99
        diff = travel - vip_price
    elif category == "Normal":
        normal_price = people_in_group * 249.99
        diff = travel - normal_price
elif people_in_group >= 50:
    travel = budget * 0.75
    if category == "VIP":
        vip_price = people_in_group * 499.99
        diff = travel - vip_price
    elif category == "Normal":
        normal_price = people_in_group * 249.99
        diff = travel - normal_price

if diff > 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")