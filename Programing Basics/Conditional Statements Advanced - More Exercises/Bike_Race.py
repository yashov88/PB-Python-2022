#           trail     cross-country    downhill     road
# juniors   5.50          8             12.25        20
# seniors    7           9.50           13.75        21.50
#     • Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
#     • Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
#     • Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# "{дарената сума}"
juniors = int(input())
seniors = int(input())
route = input()

juniors_tax = 0
seniors_tax = 0
all_bikers = juniors + seniors
all_money = 0

if route == "trail":
    juniors_tax = juniors * 5.50
    seniors_tax = seniors * 7
    all_money = juniors_tax + seniors_tax
elif route == "cross-country":
    juniors_tax = juniors * 8
    seniors_tax = seniors * 9.50
    all_money = juniors_tax + seniors_tax
    if all_bikers >= 50:
        juniors_tax = (juniors * 8) * 0.75
        seniors_tax = (seniors * 9.5) * 0.75
        all_money = juniors_tax + seniors_tax
elif route == "downhill":
    juniors_tax = juniors * 12.25
    seniors_tax = seniors * 13.75
    all_money = juniors_tax + seniors_tax
elif route == "road":
    juniors_tax = juniors * 20
    seniors_tax = seniors * 21.5
    all_money = juniors_tax + seniors_tax

expenses = all_money * 0.95
print(f"{expenses:.2f}")