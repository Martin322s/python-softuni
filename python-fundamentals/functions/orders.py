product = input()
quantity = int(input())


def calculate_price(product_name, quantity_of_product):
    total_price = 0

    if product_name == "coffee":
        total_price = 1.50
    elif product_name == "water":
        total_price = 1.00
    elif product_name == "coke":
        total_price = 1.40
    elif product_name == "snacks":
        total_price = 2.00

    return float(total_price * quantity_of_product)


print(f"{calculate_price(product, quantity):.2f}")
