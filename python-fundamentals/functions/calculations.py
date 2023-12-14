operator = input()
first_number = int(input())
second_number = int(input())


def add(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def divide(a: int, b: int):
    return a // b


if operator == 'add':
    print(add(first_number, second_number))
elif operator == 'subtract':
    print(subtract(first_number, second_number))
elif operator == 'multiply':
    print(multiply(first_number, second_number))
elif operator == 'divide':
    print(divide(first_number, second_number))
