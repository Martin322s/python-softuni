string = input()
lst = []

for i in range(len(string)):
    if string[i].isupper():
        lst.append(i)

print(lst)
