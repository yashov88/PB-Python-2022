# 7 лекари, само по един пациент на ден, останалите пациенти се изпращат в други болници.
# Всеки трети ден, болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям от броя на прегледаните,
# се назначава още един лекар, назначаването става преди да започне приемът на пациенти за деня.
# • На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# • На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден.
#   Цяло число в интервала [0…10 000]
#     • На първия ред: "Treated patients: {брой прегледани пациенти}."
#     • На втория ред: "Untreated patients: {брой непрегледани пациенти}."
days = int(input())

treated_patients = 0
untreated_patients = 0
count_days = 0
count_patients = 0
doctors = 7
for i in range(1, days + 1):
    patients = int(input())
    count_days += 1
    count_patients += patients
    if count_days % 3 == 0:
        doctors += 1

    if patients > doctors:
        untreated_patients += patients - doctors
    else:
        treated_patients = count_patients - untreated_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")