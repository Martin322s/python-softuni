secret_message = input().split()
for element in secret_message:
    numbers_list = []
    letters_list = []
    for symbol in element:
        if symbol.isdigit():
            numbers_list.append(symbol)
        elif symbol.isalpha():
            letters_list.append(symbol)
    first_letter = chr(int("".join(numbers_list)))
    letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
    last_letters = "".join(letters_list)
    total_word = first_letter + last_letters
    print(total_word, end=" ")
