# • Цената за наем на кораба през пролетта е  3000 лв.;
# • Цената за наем на кораба през лятото и есента е  4200 лв.;
# • Цената за наем на кораба през зимата е  2600 лв.
# • Ако групата е до 6 човека включително  -  отстъпка от 10%;
# • Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# • Ако групата е от 12 нагоре  -  отстъпка от 25%.
#  5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка,
#  която се начислява след като се приспадне отстъпката по горните критерии.
# "Yes! You have {останалите пари} leva left."
# "Not enough money! You need {сумата, която не достига} leva."
budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter";
count_people = int(input())

price_boat = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if count_people <= 6:
    price_boat *= 0.9
elif 6 < count_people <= 11:
    price_boat *= 0.85
elif count_people > 11:
    price_boat *= 0.75

if count_people % 2 == 0 and season != "Autumn":
    price_boat *= 0.95

diff = abs(budget - price_boat)

if budget >= price_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
