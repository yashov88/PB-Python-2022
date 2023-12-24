# 1 кг храна = 12.45 лева.
#     • Ако котката изяжда от 100 (вкл.)  до 200 грама, то тя попада в група 1: малки котки.
#     • Ако котката изяжда от 200 (вкл.)  до 300 грама, то тя попада в група 2: големи котки.
#     • Ако котката изяжда от 300 (вкл.)  до 400 грама, то тя попада в група 3: огромни котки.
#     • На първи ред - броят на котките - цяло число в интервала [1..100]
#     • На всеки следващ ред за всяка котка - Х грама храна - реално число в интервала [100.00..400.00]
# "Group 1: {броят на котките в група 1: малки котки} cats."
# "Group 2: {броят на котките в група 2: големи котки} cats."
# "Group 3: {броят на котките в група 3: огромни котки} cats."
# "Price for food per day: {цената за храната} lv."

cats_count = int((input()))
group1_count = 0
group2_count = 0
group3_count = 0
total_amount = 0

for i in range(1, cats_count + 1):
    food_grams = float(input())

    if 100 <= food_grams < 200:
        total_amount += food_grams
        group1_count += 1
    elif 200 <= food_grams < 300:
        total_amount += food_grams
        group2_count += 1
    elif 300 <= food_grams < 400:
        total_amount += food_grams
        group3_count += 1

total_food_for_cats = total_amount / 1000
total_sum = total_food_for_cats * 12.45

print(f"Group 1: {group1_count} cats.")
print(f"Group 2: {group2_count} cats.")
print(f"Group 3: {group3_count} cats.")
print(f"Price for food per day: {total_sum:.2f} lv.")