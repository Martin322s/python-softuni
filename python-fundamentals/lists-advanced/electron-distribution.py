count_electrons = int(input())
shell = [0]
index = 1
while count_electrons > 0:
    vacancies = 2 * index ** 2
    if shell[index - 1] < vacancies:
        count_electrons -= 1
        shell[index - 1] += 1
    else:
        count_electrons -= 1
        shell.append(1)
        index += 1
print(shell)
