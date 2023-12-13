command = input()
coffee_count = 0

while command != "END":
    if command == "coding" or command == "CODING":
        if command.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
        command = input()
    elif (command == "DOG" or command == "dog") or (command == "CAT" or command == "cat"):
        if command.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
        command = input()
    elif command == "movie" or command == "MOVIE":
        if command.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
        command = input()
    else:
        command = input()
        continue

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
