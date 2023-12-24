from math import floor
# input
world_record = float(input())
distance = float(input())
swimming_time = float(input())

# logic
time_to_finish = distance * swimming_time
delay = floor(distance / 15) * 12.5
time_to_finish += delay

# output
if time_to_finish < world_record:
    print(f"Yes, he succeeded! The new world record is {time_to_finish:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_to_finish - world_record:.2f} seconds slower.")
