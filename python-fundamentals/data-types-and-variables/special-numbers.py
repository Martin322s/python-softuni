number = int(input())

for num in range(1, number + 1):
    num_as_string = str(num)
    sum_of_digits = 0
    isSpecial = False

    for i in range(len(num_as_string)):
        sum_of_digits += int(num_as_string[i])

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        isSpecial = True

    print(f"{num} -> {isSpecial}")
