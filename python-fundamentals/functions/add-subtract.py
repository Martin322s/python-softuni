def add_subtract(num_one, num_two, num_three):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    sum_numbers = add(num_one, num_two)
    diff = subtract(sum_numbers, num_three)

    return diff


first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

print(add_subtract(first_integer, second_integer, third_integer))
