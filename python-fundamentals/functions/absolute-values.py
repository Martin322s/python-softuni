sequence = input()


def absolute_values(sequence_str: str):
    list_strings = sequence_str.split()
    list_numbers = []

    for num in list_strings:
        list_numbers.append(abs(float(num)))

    print(list_numbers)


absolute_values(sequence)
