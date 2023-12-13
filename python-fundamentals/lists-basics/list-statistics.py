count = int(input())
positive_list = []
negative_list = []
sum_negatives = 0

for _ in range(count):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

for element in negative_list:
    sum_negatives += element

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum_negatives}")
