name = input()
grades_total = 0
year_count = 0
failed_years = 0

while True:
    annual_grade = float(input())
    year_count += 1

    if annual_grade < 4:
        failed_years += 1

        if failed_years == 2:
            print(f"{name} has been excluded at {year_count} grade")

        year_count -= 1

    else:
        grades_total += annual_grade

    if year_count == 12:
        average_grade = grades_total / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
