def even_numbers(string):
    strings_list = string.split(" ")
    numbers_list = map(int, strings_list)
    even_list = list(filter(lambda x: x % 2 == 0, numbers_list))

    return even_list


sequence = input()
print(even_numbers(sequence))
