# Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата. При модулното деление - остатъка. Трябва да се има предвид, че делителят може
# да е равен на 0 (нула), а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.
#     • Ако операцията е събиране, изваждане или умножение:
#         ◦  "{N1} {оператор} {N2} = {резултат} - {even/odd}"
#     • Ако операцията е деление:
#         ◦ "{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
#     • Ако операцията е модулно деление:
#         ◦ "{N1} % {N2} = {остатък}"
#     • В случай на деление с 0 (нула):
#         ◦ "Cannot divide {N1} by zero"
first_num = int(input())
second_num = int(input())
operator = input()

sum = 0
zero_flag = False

if operator == "+":
    sum = first_num + second_num
elif operator == "-":
    sum = first_num - second_num
elif operator == "*":
    sum = first_num * second_num
elif operator == "/":
    if second_num == 0:
        zero_flag = True
    else:
        sum = first_num / second_num
elif operator == "%":
    if second_num == 0:
        zero_flag = True
    else:
        sum = first_num % second_num

if operator == "+" or operator == "-" or operator == "*":
    if sum % 2 == 0:
        print(f"{first_num} {operator} {second_num} = {sum} - even")
    else:
        print(f"{first_num} {operator} {second_num} = {sum} - odd")
elif operator == "/":
    if zero_flag:
        print(f"Cannot divide {first_num} by zero")
    else:
        print(f"{first_num} {operator} {second_num} = {sum:.2f}")
elif operator == "%":
    if zero_flag:
        print(f"Cannot divide {first_num} by zero")
    else:
        print(f"{first_num} {operator} {second_num} = {sum}")
