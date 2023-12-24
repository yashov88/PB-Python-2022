# input
mackerel = float(input())
sprat = float(input())
bonito = float(input())
scad = float(input())
mussels = int(input())

# logic
bonito_price = mackerel + (mackerel * 0.60)
sum_bonito = bonito_price * bonito
price_scad = sprat + (sprat * 0.8)
sum_scad = price_scad * scad
sum_mussels = 7.5 * (mussels * 1.0)
total_sum = sum_bonito + sum_scad + sum_mussels

# output
print(f'{total_sum:.2f}')