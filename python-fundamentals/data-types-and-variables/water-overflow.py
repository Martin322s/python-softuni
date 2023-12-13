num = int(input())
capacity = 255
tank = 0

for _ in range(num):
    liters = int(input())
    tank += liters

    if capacity < tank:
        tank -= liters
        print("Insufficient capacity!")
        continue

print(tank)
