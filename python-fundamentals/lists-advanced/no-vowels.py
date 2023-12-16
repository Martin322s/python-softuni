text = input()
forbidden_letters = ['a', 'o', 'u', 'e', 'i']

no_vowels_list = [text[i] for i in range(0, len(text)) if text[i].lower() not in forbidden_letters]

print("".join(no_vowels_list))
