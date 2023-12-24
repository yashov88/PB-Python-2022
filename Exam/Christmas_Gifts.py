#     • Всички до 16 (вкл.) години се считат за деца и ще получат играчка
#     • Всички над 16 години се считат за възрастни и ще получат коледен пуловер
#     • Цената на всяка играчка е 5 лв., а цената на един пуловер е 15 лв.
# От конзолата се четат поредица от редове до получаване на команда "Christmas":
#     • Годините на всеки член от семейството - цяло число в интервала [1 … 130]
#     • "Number of adults: {брой хора над 16 години}"
#     • "Number of kids: {брой хора до 16 (вкл.) години}"
#     • "Money for toys: {сумата за всички играчки}"
#     • "Money for sweaters: {сума за всички пуловери}"

input_line = input()
adult_count = 0
kids_count = 0

while input_line != "Christmas":
    age_of_person = int(input_line)

    if age_of_person <= 16:
        kids_count += 1
    else:
        adult_count += 1

    input_line = input()

price_of_toys = kids_count * 5
price_of_sweaters = adult_count * 15

print(f"Number of adults: {adult_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {price_of_toys}")
print(f"Money for sweaters: {price_of_sweaters}")
