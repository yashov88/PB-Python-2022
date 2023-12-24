#     • При 100 лв. или по-малко - някъде в България:
#         ◦ Лято - 30% от бюджета;
#         ◦ Зима - 70% от бюджета.
#     • При 1000 лв. или по малко - някъде на Балканите:
#         ◦ Лято - 40% от бюджета;
#         ◦ Зима - 80% от бюджета.
#     • При повече от 1000 лв. - някъде из Европа:
#         ◦ При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
#     •  "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
#     • "{Вид почивка} - {Похарчена сума}":
#         ◦ Почивката може да е между "Camp" и "Hotel"
#         ◦ Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая
budget = float(input())
season = input()

destination = ""
place = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        expenses = budget * 0.3
    elif season == "winter":
        place = "Hotel"
        expenses = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        expenses = budget * 0.4
    elif season == "winter":
        place = "Hotel"
        expenses = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    expenses = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")
