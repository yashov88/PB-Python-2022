# • Пари, нужни за екскурзията - реално число;
# • Налични пари - реално число.
# След това многократно се четат по два реда:
# • Вид действие – текст с две възможности: "spend" или "save";
# ◦ Сумата, която ще спести/похарчи - реално число.
# • Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# • "You can't save the money."
# • "{Общ брой изминали дни}"
# • Ако Джеси събере парите за почивката, на конзолата се изписва:
# • "You saved the money for {общ брой изминали дни} days."

needed_money = float(input())
init_money = float(input())

total_sum = init_money
count_total_days = 0
count_spend_days = 0
while total_sum < needed_money:
    if count_spend_days >= 5:
        break
    action = input()
    amount = float(input())

    count_total_days += 1

    if action == "spend":
        count_spend_days += 1
        total_sum -= amount
        if total_sum <= 0:
            total_sum = 0
    elif action == "save":
        count_spend_days = 0
        total_sum += amount

if count_spend_days == 5:
    print("You can't save the money.")
    print(count_total_days)
else:
    print(f"You saved the money for {count_total_days} days.")