number_of_locations = int(input())

while True:
    expected_amount = float(input())
    days_amount = int(input())

    total_gold_per_day = 0

    for i in range(days_amount):
        gold_per_day = float(input())
        total_gold_per_day += gold_per_day

    average_gold_per_day = abs(total_gold_per_day / days_amount)
    diff = expected_amount - average_gold_per_day
    if average_gold_per_day >= expected_amount:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        #gold_needed = abs(expected_amount - average_gold_per_day)
        print(f"You need {diff:.2f} gold.")

# location_count = int(input())
#
#  for i in range(location_count):
#      expected_mining = float(input())
#      day_count = int(input())
#
#      current_gold = 0
#      for j in range(day_count):
#          gold = float(input())
#          current_gold += gold
#
#      average_mining = current_gold / day_count
#      diff = expected_mining - average_mining
#      if expected_mining <= average_mining:
#          print(f"Good job! Average gold per day: {average_mining:.2f}.")
#      elif expected_mining > average_mining:
#          print(f"You need {diff:.2f} gold.")