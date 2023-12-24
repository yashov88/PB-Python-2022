import math

# 6 човешки месеца се равняват на 1 котешки месе
# Порода    British Shorthair    Siamese    Persian     Ragdoll     American Shorthair      Siberian
# (m)       13 години           15 години   14 години   16 години       12 години           11 години
# (f)       14 години           16 години   15 години   17 години       13 години           12 години
#     • Порода на котката  –  текст  –  една от възможностите: "British Shorthair", "Siamese", "Persian",
#                                                               "Ragdoll", "American Shorthair" или "Siberian"
#     • Пол на котката  – символ –  'm' или 'f'
# "{котешки месецa} cat months"
# Резултатът трябва да е закръглен до най-близкото цяло число надолу.

cat_breed = input()
sex = input()

if sex == "m":
    if cat_breed == "British Shorthair":
        print(f"{math.floor((13 * 12) / 6)} cat months")
    elif cat_breed == "Siamese":
        print(f"{math.floor((15 * 12) / 6)} cat months")
    elif cat_breed == "Persian":
        print(f"{math.floor((14 * 12) / 6)} cat months")
    elif cat_breed == "Ragdoll":
        print(f"{math.floor((16 * 12) / 6)} cat months")
    elif cat_breed == "American Shorthair":
        print(f"{math.floor((12 * 12) / 6)} cat months")
    elif cat_breed == "Siberian":
        print(f"{math.floor((11 * 12) / 6)} cat months")
    else:
        print(f"{cat_breed} is invalid cat!")
elif sex == "f":
    if cat_breed == "British Shorthair":
        print(f"{math.floor((14 * 12) / 6)} cat months")
    elif cat_breed == "Siamese":
        print(f"{math.floor((16 * 12) / 6)} cat months")
    elif cat_breed == "Persian":
        print(f"{math.floor((15 * 12) / 6)} cat months")
    elif cat_breed == "Ragdoll":
        print(f"{math.floor((17 * 12) / 6)} cat months")
    elif cat_breed == "American Shorthair":
        print(f"{math.floor((13 * 12) / 6)} cat months")
    elif cat_breed == "Siberian":
        print(f"{math.floor((12 * 12) / 6)} cat months")
    else:
        print(f"{cat_breed} is invalid cat!")

