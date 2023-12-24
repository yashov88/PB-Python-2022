floors = int(input())
flats_per_flor = int(input())

flat_number = 0
flat_name = ""
for floor_n in range(floors, 0, -1):
    for flat_n in range(flats_per_flor):

        flat_number = floor_n * 10 + flat_n
        if floor_n == floors:
            flat_name = f"L{flat_number}"
        elif floor_n % 2 == 0:
            flat_name = f"O{flat_number}"
        elif floor_n % 2 != 0:
            flat_name = f"A{flat_number}"

        print(flat_name, end=" ")

    print()