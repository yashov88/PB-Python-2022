# • кошничка за яйца (basket) – 1.50 лв.
# • великденски венец (wreath) – 3.80 лв.
# • шоколадов заек (chocolate bunny) – 7 лв.
# • Брои на клиентите в магазина – цяло число [1… 100]
# • След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# ◦ Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
# ◦ "You purchased {броя на покупките} items for {крайната цена} leva."
# • Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# ◦ "Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva.
client_number = int(input())
total_sum_orders = 0

for count in range(client_number):
    current_sum = 0
    product_counter = 0

    while True:
        product = input()


        if product == "Finish":
            break

        product_counter += 1
        if product == "basket":
            current_sum += 1.5
        elif product == "wreath":
            current_sum += 3.8
        elif product == "chocolate bunny":
            current_sum += 7

    if product_counter % 2 == 0:
        current_sum -= current_sum * 0.2

    total_sum_orders += current_sum
    print(f"You purchased {product_counter} items for {current_sum:.2f} leva.")

total_sum_orders /= client_number
print(f"Average bill per client is: {total_sum_orders:.2f} leva.")