# • След това многократно се четат по два реда:
#     ◦ Име на задача – текст;
#     • Оценка - цяло число в интервала [2…6]
#  докато не получи съобщение "Enough"
#  Марин получи определения брой незадоволителни оценки.
#  Незадоволителна е всяка оценка, която е по-малка или равна на 4.
poor_grades = int(input())

input_line = input()
sum_grades = 0
count_grades = 0
last_problem = ""
poor_count = 0
flag = False

while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())

    if current_grade <= 4:
        poor_count += 1

    if poor_count >= poor_grades:
        flag = True
        break

    count_grades += 1
    sum_grades += current_grade
    last_problem = input_line

    input_line = input()

if flag:
    print(f"You need a break, {poor_count} poor grades.")
else:
    avg_grade = sum_grades / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
