#     • Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
#     • Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
#     • Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
#     • Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
#     • Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта

kilometers = int(input())
travel = input()
total_sum = 0

if kilometers < 20:
    if travel == "day":
        total_sum = (kilometers * 0.79) + 0.70
    elif travel == "night":
        total_sum = (kilometers * 0.90) + 0.70
elif 20 <= kilometers < 100:
    total_sum = kilometers * 0.09
elif kilometers >= 100:
    total_sum = kilometers * 0.06

print(f"{total_sum:.2f}")
