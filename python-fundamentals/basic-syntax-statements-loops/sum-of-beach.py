string = input().lower()
total_count = 0

if string.count("water") > 0:
    total_count += string.count("water")

if string.count("sand") > 0:
    total_count += string.count("sand")

if string.count("fish") > 0:
    total_count += string.count("fish")

if string.count("sun") > 0:
    total_count += string.count("sun")

print(total_count)
