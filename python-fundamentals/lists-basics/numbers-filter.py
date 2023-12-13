integers_count = int(input())
numbers_list = []

for _ in range(integers_count):
    num = int(input())
    numbers_list.append(num)

criteria = input()
filtered_numbers_list = []

if criteria == "even":
    for number in numbers_list:
        if number % 2 == 0 or number == 0:
            filtered_numbers_list.append(number)
elif criteria == "odd":
    for number in numbers_list:
        if number % 2 != 0 and number != 0:
            filtered_numbers_list.append(number)
elif criteria == "positive":
    for number in numbers_list:
        if number >= 0:
            filtered_numbers_list.append(number)
elif criteria == "negative":
    for number in numbers_list:
        if number < 0 and number != 0:
            filtered_numbers_list.append(number)

print(filtered_numbers_list)
