input_version = list(map(int, input().split(".")))
next_version = ["0", "0", "0"]

version_one = int(input_version[0])
version_two = int(input_version[1])
version_three = int(input_version[2]) + 1

if version_three > 9:
    version_three = 0
    version_two += 1

if version_two > 9:
    version_two = 0
    version_one += 1

if version_one > 9:
    version_one = 0

next_version[0] = str(version_one)
next_version[1] = str(version_two)
next_version[2] = str(version_three)

print(".".join(next_version))
