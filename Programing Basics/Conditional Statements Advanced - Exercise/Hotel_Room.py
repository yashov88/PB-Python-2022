# Май и октомври                 Юни и септември                   Юли и август
# Студио - 50 лв./нощувка       Студио - 75.20 лв./нощувка         Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка   Апартамент - 68.70 лв./нощувка     Апартамент - 77 лв./нощувка
#     • За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#     • За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#     • За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#     • За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

month = input()  # May, June, July, August, September или October
count_night = int(input())

studio = 0
apartment = 0
rent_studio = 0
rent_apartment = 0

if month == "May" or month == "October":
    studio = 50
    if 7 < count_night <= 14:
        rent_studio = (count_night * studio) * 0.95
    elif count_night > 14:
        rent_studio = (count_night * studio) * 0.70
    else:
        rent_studio = count_night * studio
    apartment = 65
    if count_night > 14:
        rent_apartment = (count_night * apartment) * 0.90
    else:
        rent_apartment = count_night * apartment
elif month == "June" or month == "September":
    studio = 75.20
    if count_night > 14:
        rent_studio = (count_night * studio) * 0.80
    else:
        rent_studio = count_night * studio
    apartment = 68.70
    if count_night > 14:
        rent_apartment = (count_night * apartment) * 0.90
    else:
        rent_apartment = count_night * apartment
elif month == "July" or month == "August":
    studio = 76
    rent_studio = count_night * studio
    apartment = 77
    if count_night > 14:
        rent_apartment = (count_night * apartment) * 0.90
    else:
        rent_apartment = count_night * apartment

print(f"Apartment: {rent_apartment:.2f} lv.")
print(f"Studio: {rent_studio:.2f} lv.")
