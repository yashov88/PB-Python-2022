time_for_movie = int(input())
number_of_scenes = int(input())
time_for_scenes = int(input())

field_preparation = time_for_movie * 0.15
total_time_for_scenes = number_of_scenes * time_for_scenes
time_needed = total_time_for_scenes + field_preparation

diff = abs(time_for_movie - time_needed)
if time_needed > time_for_movie:
    print(f"Time is up! To complete the movie you need {diff:.0f} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {diff:.0f} minutes left!")

