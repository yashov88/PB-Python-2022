number_eggs = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
color = ""

for count in range(number_eggs):
    input_line = input()

    if input_line == "red":
        red_count += 1
    elif input_line == "orange":
        orange_count += 1
    elif input_line == "blue":
        blue_count += 1
    elif input_line == "green":
        green_count += 1

max_number = max(red_count, orange_count, blue_count, green_count)

if red_count == max_number:
    color = "red"
elif orange_count == max_number:
    color = "orange"
elif blue_count == max_number:
    color = "blue"
elif green_count == max_number:
    color = "green"

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_number} -> {color}")
