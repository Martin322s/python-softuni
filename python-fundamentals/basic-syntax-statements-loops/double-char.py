word = input()

while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    else:
        doubled_word = ""

        for i in range(len(word)):
            doubled_word = word[i] + word[i]
            print(doubled_word, end="")
        word = input("\n")
