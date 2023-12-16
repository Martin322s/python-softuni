to_do_task = input()
to_do_list = []
tasks_list = []
tasks = []

while to_do_task != "End":
    to_do_list.append(to_do_task.split("-"))
    to_do_task = input()

tasks_list = [to_do[1] for to_do in sorted([[int(el[0]), el[1]] for el in to_do_list])]

print(tasks_list)
