rent = int(input())

price_trophy = rent * 0.70
price_catering = price_trophy * 0.85
price_sound = price_catering / 2

total_sum = rent + price_trophy + price_catering + price_sound
print(f"{total_sum:.2f}")
