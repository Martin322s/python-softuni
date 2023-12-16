strings = input().split(" ")
searched_palindrome = input()
palindromes = []
count = 0

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

    if word == searched_palindrome:
        count += 1

print(palindromes)
print(f"Found palindrome {count} times")
