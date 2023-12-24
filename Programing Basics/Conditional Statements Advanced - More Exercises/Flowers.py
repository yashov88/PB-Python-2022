# Chrysanthemums    Roses   Tulips
#       2.00        4.10    2.50    -> Spring, Summer
#       3.75        4.50    4.15    -> Autumn, Winter
# В празнични дни цените на всички цветя се увеличават с 15%
#     • За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
#     • За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
#     • За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Отстъпките се правят по така написания ред и могат да се наслагват!
# Всички отстъпки важат след оскъпяването за празничен ден!
# Цената за аранжиране на букета винаги е 2лв.
#     • На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
#     • На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
#     • На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
#     • На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
#     • На петия ред е посочено дали денят е празник – [Y – да / N - не]
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()

all_flowers = chrysanthemums + roses + tulips
total_price = 0


if season == "Spring":
    total_price = (chrysanthemums * 2.0) + (roses * 4.10) + (tulips * 2.5)
    if tulips > 7:
        total_price *= 0.95

    if day == "Y":
        total_price = total_price + (total_price * 0.15)
elif season == "Summer":
    total_price = (chrysanthemums * 2.0) + (roses * 4.10) + (tulips * 2.5)
    if day == "Y":
        total_price = total_price + (total_price * 0.15)
elif season == "Autumn":
    total_price = (chrysanthemums * 3.75) + (roses * 4.50) + (tulips * 4.15)
    if day == "Y":
        total_price = total_price + (total_price * 0.15)
elif season == "Winter":
    total_price = (chrysanthemums * 3.75) + (roses * 4.50) + (tulips * 4.15)
    if day == "Y":
        total_price = total_price + (total_price * 0.15)

    if roses >= 10:
        total_price *= 0.90

if all_flowers > 20:
    total_price *= 0.80

arrangement = total_price + 2
print(f"{arrangement:.2f}")