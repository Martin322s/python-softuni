budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
sweet_bread_quantity = 0
colored_eggs_quantity = 0
sweet_bread_price = flour_price + milk_price + eggs_price

while budget > sweet_bread_price:
    sweet_bread_quantity += 1
    budget -= sweet_bread_price
    colored_eggs_quantity += 3

    if sweet_bread_quantity % 3 == 0:
        colored_eggs_quantity -= sweet_bread_quantity - 2

print(f'You made {sweet_bread_quantity} loaves of Easter bread! Now you have {colored_eggs_quantity} eggs '
      f'and 'f'{budget:.2f}BGN left.')
