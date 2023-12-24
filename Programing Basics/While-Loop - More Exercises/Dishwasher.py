# 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.
# всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери
# Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# "End" или докато количеството препарат не се изчерпи,
# брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
bottles_detergent = int(input())

count = 0
detergent_plate = 0
detergent_pot = 0
total_detergent = bottles_detergent * 750
plates = 0
pots = 0
is_Enough = False
input_line = input()

while input_line != "End":
    dishes = int(input_line)
    count += 1

    if count % 3 == 0:
        detergent_pot += (dishes * 0.15) * 100
        pots += dishes
    else:
        detergent_plate += (dishes * 0.05) * 100
        plates += dishes

    diff = total_detergent - (detergent_plate + detergent_pot)

    if diff < 0:
        is_Enough = True
        break
    input_line = input()

if is_Enough:
    print(f"Not enough detergent, {abs(diff):.0f} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff:.0f} ml.")
