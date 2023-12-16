numbers_list = list(map(int, input().split(", ")))

indices = list(map(lambda x: x if numbers_list[x] % 2 == 0 else "no", range(len(numbers_list))))
indices = list(filter(lambda x: x != "no", indices))

print(indices)
