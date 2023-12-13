num = int(input())
word = input()
words_search = []

for _ in range(num):
    string = input()
    words_search.append(string)
print(words_search)

filtered_strings = []

for string in words_search:
    if word in string:
        filtered_strings.append(string)

print(filtered_strings)
