string = input()
strings_list = string.split()
inverted_numbers = []

for i in range(len(strings_list)):
    if int(strings_list[i]) > 0:
        inverted_numbers.append(int("-" + str(strings_list[i])))
    else:
        inverted_numbers.append(abs(int(strings_list[i])))

print(inverted_numbers)
