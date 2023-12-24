# • Име на актьора - текст
# • Точки от академията - реално число в интервала [2.0... 450.5]
# • Брой оценяващи n - цяло число в интервала[1… 20]
#   На следващите n-на брой реда:
# • Име на оценяващия - текст
# • Точки от оценяващия - реално число в интервала [1.0... 50.0]
# • Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# • Ако точките не са достатъчни:
# "Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!
name_actor = input()
init_points = float(input())
count_people = int(input())

total_points = init_points
flag = False
for i in range(1, count_people + 1):
    name = input()
    points = float(input())

    current_point = (len(name) * points) / 2
    total_points += current_point

    if total_points >= 1250.5:
        flag = True
        break

if flag:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
