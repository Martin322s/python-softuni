string = input()
beggars = int(input())
all_sums = string.split(", ")
final_list = []

for beggar in range(beggars):
    current_sum = 0
    for i in range(len(all_sums)):
        if i == beggar:
            current_sum += int(all_sums[i])
            beggar += beggars
    final_list.append(current_sum)
print(final_list)
