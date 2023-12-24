#     • Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
#     • Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
# "24-27" или "28-31"
#     • Трети ред - брой нощувки - цяло число в интервала [1… 100]
# "Easter trip to {дестинация} : {разходи за екскурзията} leva."

destination = input()
dates = input()
number_of_night = int(input())

total_cost = 0

if destination == "France":
    if dates == "21-23":
        total_cost = number_of_night * 30
    elif dates == "24-27":
        total_cost = number_of_night * 35
    elif dates == "28-31":
        total_cost = number_of_night * 40
elif destination == "Italy":
    if dates == "21-23":
        total_cost = number_of_night * 28
    elif dates == "24-27":
        total_cost = number_of_night * 32
    elif dates == "28-31":
        total_cost = number_of_night * 39
elif destination == "Germany":
    if dates == "21-23":
        total_cost = number_of_night * 32
    elif dates == "24-27":
        total_cost = number_of_night * 37
    elif dates == "28-31":
        total_cost = number_of_night * 43
print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
