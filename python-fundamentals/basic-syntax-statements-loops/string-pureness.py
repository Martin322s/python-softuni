strings_count = int(input())

for _ in range(strings_count):
    string = input()

    if all(char not in ",._" for char in string):
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
