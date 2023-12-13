name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        exit()

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
        name = input()
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
        name = input()
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
        name = input()
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
        name = input()

print("Welcome to Hogwarts.")
