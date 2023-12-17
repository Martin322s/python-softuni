input_sequence = input().split(" ")
filtered_words = [string for string in input_sequence if len(string) % 2 == 0]

for word in filtered_words:
    print(word)
