# Winter vacation   Spring holiday  Summer vacation
#       9.60               7.20            15       -> boys, girls
#       10                  9.50            20      -> mixed group
#     • Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
#     • Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
#     • Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# girls -> Gymnastics   Athletics   Volleyball
# boys -> Judo  Tennis  Football
# mixed group -> Ski    Cycling     Swimming
#     1. Сезонът – текст - “Winter”, “Spring” или “Summer”;
#     2. Видът на групата – текст - “boys”, “girls” или “mixed”;
#     3. Брой на учениците – цяло число в интервала [1 … 10000];
#     4. Брой на нощувките – цяло число в интервала [1 … 100].
# "{спортът} {цената} lv.“
season = input()
group = input()
num_of_children = int(input())
num_of_nights = int(input())

sport = ""
money_pay = 0

if season == "Winter":
    if group == "boys":
        sport = "Judo"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 9.6
    elif group == "girls":
        sport = "Gymnastics"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 9.6) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 9.6
    elif group == "mixed":
        sport = "Ski"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 10) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 10) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 10) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 10
elif season == "Spring":
    if group == "boys":
        sport = "Tennis"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 7.2
    elif group == "girls":
        sport = "Athletics"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 7.2) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 7.2
    elif group == "mixed":
        sport = "Cycling"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 9.5) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 9.5) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 9.5) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 9.5
elif season == "Summer":
    if group == "boys":
        sport = "Football"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 15
    elif group == "girls":
        sport = "Volleyball"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 15) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 15
    elif group == "mixed":
        sport = "Swimming"
        if 10 <= num_of_children < 20:
            money_pay = ((num_of_children * num_of_nights) * 20) * 0.95
        elif 20 <= num_of_children < 50:
            money_pay = ((num_of_children * num_of_nights) * 20) * 0.85
        elif num_of_children >= 50:
            money_pay = ((num_of_children * num_of_nights) * 20) * 0.5
        else:
            money_pay = (num_of_children * num_of_nights) * 20

print(f"{sport} {money_pay:.2f} lv.")
