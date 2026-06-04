list_of_tasks = [
    {"task": "Check Email", "priority": 3},
    {"task": "eat", "priority": 9}
]

n = len(list_of_tasks)
low_priority = 2
medium_priority = 5
high_priority = 8


for i in range(n):
    if list_of_tasks[i]["priority"] > high_priority:
        print(list_of_tasks[i]["task"])