
chicken_menu = int(input())
fish_menu = int(input())
vedge_menu = int(input())

chicken_price = 10.35 * chicken_menu
fish_price = 12.40 * fish_menu
vedge_price = 8.15 * vedge_menu

total = chicken_price + fish_price + vedge_price
dessert_price = total * 0.20
delivery = 2.5

total_price = total + dessert_price + delivery

print(round(total_price, 2))