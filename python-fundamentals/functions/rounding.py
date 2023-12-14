string = input()
strings_list = string.split(' ')


def round_numbers(list_strings):
    list_numbers = []
    for string_el in list_strings:
        list_numbers.append(round((float(string_el))))

    return list_numbers


print(round_numbers(strings_list))
