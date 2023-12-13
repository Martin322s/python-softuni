current_year = int(input())

while True:
    current_year += 1
    year_str = str(current_year)

    if len(set(year_str)) == len(year_str):
        print(current_year)
        break
