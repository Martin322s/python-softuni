numbers_count = int(input())

for _ in range(numbers_count):
    num = int(input())

    if num % 2 != 0:
        print(f"{num} is odd!")
        break

else:
    print("All numbers are even.")
