from math import ceil
# input
movie_name = input()
time_of_movie = int(input())
lunch_break = int(input())

# logic
time_to_lunch = lunch_break / 8
time_to_break = lunch_break / 4
time_left = lunch_break - time_to_lunch - time_to_break

# output
if time_left >= time_of_movie:
    print(f"You have enough time to watch {movie_name} and left with {ceil(time_left - time_of_movie)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(time_of_movie - time_left)} more minutes.")
