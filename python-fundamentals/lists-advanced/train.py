wagons_count = int(input())
command = input()
wagons = [0 for _ in range(0, wagons_count)]

while command != "End":
    command_list = command.split(" ")

    if command_list[0] == "add":
        people_count = int(command_list[1])
        wagons[-1] += people_count
    elif command_list[0] == "insert":
        index = int(command_list[1])
        people_count = int(command_list[2])
        wagons[index] += people_count
    elif command_list[0] == "leave":
        index = int(command_list[1])
        people_count = int(command_list[2])
        wagons[index] -= people_count
    command = input()

print(wagons)
