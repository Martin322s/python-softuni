def sum_odd_even(number):
    even_sum = 0
    odd_sum = 0
    number_to_string = str(number)

    numbers_list = list(number_to_string)

    for number in numbers_list:
        num = int(number)

        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum


integer = int(input())
print(f"Odd sum = {sum_odd_even(integer)[1]}, Even sum = {sum_odd_even(integer)[0]}")
