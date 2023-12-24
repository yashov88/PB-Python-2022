# input
movie_budget = float(input())
actor_count = int(input())
suit_price = float(input())

# logic
decor_price = movie_budget * 0.1
actor_suit_total_price = actor_count * suit_price

if actor_count > 150:
    actor_suit_total_price -= actor_suit_total_price * 0.1

movie_price = decor_price + actor_suit_total_price

# output
if movie_price <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - movie_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {movie_price - movie_budget:.2f} leva more.")
