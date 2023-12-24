#     • Бензин – 2.22 лева за един литър,
#     • Дизел – 2.33 лева за един литър
#     • Газ – 0.93 лева за литър
# намаления за литър гориво: 18 ст. за литър бензин, 12 ст. за литър дизел и 8 ст. за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.
#     • Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
#     • Количество гориво – реално число в интервала [1.00 … 50.00]
#     • Притежание на клубна карта – текст с възможности: "Yes" или "No"
# "{крайната цена на горивото} lv."
fuel = input()
liters_fuel = float(input())
club_cart = input()

liter_price = 0
diesel_price = 0
gasoline_price = 0
gas_price = 0

if fuel == "Diesel":
    liter_price = 2.33
    diesel_price = liter_price * liters_fuel
    if club_cart == "Yes":
        liter_price = liter_price - 0.12
        diesel_price = liter_price * liters_fuel
        if 20 < liters_fuel <= 25:
            diesel_price = diesel_price * 0.92
            print(f"{diesel_price:.2f} lv.")
        elif 25 < liters_fuel:
            diesel_price = diesel_price * 0.90
            print(f"{diesel_price:.2f} lv.")
        else:
            print(f"{diesel_price:.2f} lv.")
    else:
        if 20 < liters_fuel <= 25:
            diesel_price = diesel_price * 0.92
            print(f"{diesel_price:.2f} lv.")
        elif 25 < liters_fuel:
            diesel_price = diesel_price * 0.90
            print(f"{diesel_price:.2f} lv.")
        else:
            print(f"{diesel_price:.2f} lv.")
elif fuel == "Gasoline":
    liter_price = 2.22
    gasoline_price = liter_price * liters_fuel
    if club_cart == "Yes":
        liter_price = liter_price - 0.18
        gasoline_price = liter_price * liters_fuel
        if 20 < liters_fuel <= 25:
            gasoline_price = gasoline_price * 0.92
            print(f"{gasoline_price:.2f} lv.")
        elif 25 < liters_fuel:
            gasoline_price = gasoline_price * 0.90
            print(f"{gasoline_price:.2f} lv.")
        else:
            print(f"{gasoline_price:.2f} lv.")
    else:
        if 20 < liters_fuel <= 25:
            gasoline_price = gasoline_price * 0.92
            print(f"{gasoline_price:.2f} lv.")
        elif 25 < liters_fuel:
            gasoline_price = gasoline_price * 0.90
            print(f"{gasoline_price:.2f} lv.")
        else:
            print(f"{gasoline_price:.2f} lv.")
elif fuel == "Gas":
    liter_price = 0.93
    gas_price = liter_price * liters_fuel
    if club_cart == "Yes":
        liter_price = liter_price - 0.08
        gas_price = liter_price * liters_fuel
        if 20 < liters_fuel <= 25:
            gas_price = gas_price * 0.92
            print(f"{gas_price:.2f} lv.")
        elif 25 < liters_fuel:
            gas_price = gas_price * 0.90
            print(f"{gas_price:.2f} lv.")
        else:
            print(f"{gas_price:.2f} lv.")
    else:
        if 20 < liters_fuel <= 25:
            gas_price = gas_price * 0.92
            print(f"{gas_price:.2f} lv.")
        elif 25 < liters_fuel:
            gas_price = gas_price * 0.90
            print(f"{gas_price:.2f} lv.")
        else:
            print(f"{gas_price:.2f} lv.")
