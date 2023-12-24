"""from math import floor"""
number_of_pages = int(input())
pages = int(input())
number_of_days = int(input())
time_to_read = number_of_pages / pages
hours_per_day = time_to_read / number_of_days
print(int(hours_per_day))
