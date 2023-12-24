# буква          a    e   i   o   u
# стойност       1    2   3   4   5

text = input()

result = 0

for symbol in text:
    if symbol == "a":
        result += 1
    elif symbol == "e":
        result += 2
    elif symbol == "i":
        result += 3
    elif symbol == "o":
        result += 4
    elif symbol == "u":
        result += 5

print(result)
