number_of_orders = int(input())
total_orders_price = 0

for _ in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        total_capsules_count = capsules_needed_per_day * days
        total_price = total_capsules_count * capsule_price
        total_orders_price += total_price
        print(f"The price for the coffee is: ${total_price:.2f}")
    else:
        continue

print(f"Total: ${total_orders_price:.2f}")
