# • Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# • Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# • Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# • Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# • До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# ◦ "The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%.
#   Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# ◦ "For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."
pool = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

p1_liters = hours * p1
p2_liters = hours * p2
total_liters = p1_liters + p2_liters
diff = abs(total_liters - pool)
percent_p1 = (p1_liters / total_liters) * 100
percent_p2 = (p2_liters / total_liters) * 100
percent_pool = (total_liters / pool) * 100

if total_liters <= pool:
    print(f"The pool is {percent_pool}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {diff} liters.")
