def ascii_character(first_symbol, second_symbol):
    first_symbol_index = ord(first_symbol)
    second_symbol_index = ord(second_symbol)
    characters = []

    for i in range(first_symbol_index +1, second_symbol_index):
        characters.append(chr(i))

    return " ".join(characters)


char_one = input()
char_two = input()
print(ascii_character(char_one, char_two))
