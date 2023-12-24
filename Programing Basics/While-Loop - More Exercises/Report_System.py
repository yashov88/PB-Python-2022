# винаги се редуват: плащане в брой и плащане с карта.
#     • Ако продуктът надвишава 100лв., за него не може да се плати в брой
#     • Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# "End" или докато не се съберат нужните средства:
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
#     • При успешна транзакция: "Product sold!"
#     • При неуспешна транзакция: "Error in transaction!"
#     • Ако сумата на всички закупени продукти надвиши или достигне очакваната сума,
#       програмата трябва да приключи и на конзолата да се изпишат два реда:
#     • "Average CS: {средно плащане в кеш на човек}"
#     • "Average CC: {средно плащане с карта на човек}"
#       Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
#     • При получаване на команда "End", да се изпише един ред:
#     • "Failed to collect required money for charity."
money_for_charity = int(input())

count = 0
total_sum = 0
card = 0
kash = 0
card_count = 0
kash_count = 0
is_Found = False
input_line = input()

while input_line != "End":
    price = int(input_line)
    count += 1
    total_sum += price
    if count % 2 == 0:
        card += price
        if price < 10:
            card -= price
            total_sum -= price
            print("Error in transaction!")
        else:
            card_count += 1
            print("Product sold!")
    else:
        kash += price
        if price > 100:
            kash -= price
            total_sum -= price
            print("Error in transaction!")
        else:
            kash_count += 1
            print("Product sold!")

    if total_sum >= money_for_charity:
        is_Found = True
        break

    input_line = input()


if is_Found:
    print(f"Average CS: {(kash / kash_count):.2f}")
    print(f"Average CC: {(card / card_count):.2f}")
else:
    print("Failed to collect required money for charity.")