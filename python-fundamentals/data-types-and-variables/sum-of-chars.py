chars_count = int(input())
sum_of_chars = 0

for _ in range(chars_count):
    char = input()
    ascii_code = int(ord(char))
    sum_of_chars += ascii_code

print(f"The sum equals: {sum_of_chars}")
