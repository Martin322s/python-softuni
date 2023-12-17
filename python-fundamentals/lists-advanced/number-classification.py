numbers_sequence = list(map(int, input().split(", ")))

positive_numbers = [str(num) for num in numbers_sequence if num >= 0]
negative_numbers = [str(num) for num in numbers_sequence if num < 0]
even_numbers = [str(num) for num in numbers_sequence if num % 2 == 0]
odd_numbers = [str(num) for num in numbers_sequence if num % 2 != 0]

print("Positive: " + ", ".join(positive_numbers))
print("Negative: " + ", ".join(negative_numbers))
print("Even: " + ", ".join(even_numbers))
print("Odd: " + ", ".join(odd_numbers))
