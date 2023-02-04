choice=-1

tasks = []

def show_tasks():
    if len(tasks)==0:
        print("There is no tasks in this file.")
        print("Create one by chosing '2. Add a task.'")
        return
    task_index=0
    for task in tasks:
        print(task+" ["+str(task_index)+"]")
        task_index+=1

def add_task():
    task=input("New task: ")
    tasks.append(task)
    print("The task has been added succesfully.")
    print()

def delete_task():
    task_index=int(input("Task index with a task to delete: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("This index does not exist.")
        return
    tasks.pop(task_index)
    print("The task has been removed succesfully.")
    print()

def save_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()

def load_tasks_from_file():
    try:
        file = open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()

while choice !=5:
    print()
    print("1. Show tasks.")
    print("2. Add a task.")
    print("3. Delete a task.")
    print("4. Save a file.")
    print("5. Leave.")
    #IN NEXT VERSION:
    #print("5. Mark as 'done'.")
    #print("6. Mark as 'in progress'.")
    #print("7. Leave.")
    print()

    choice=int(input("Give a number: "))
    print()
    if choice == 1:
        show_tasks()
    if choice == 2:
        add_task()
    if choice == 3:
        delete_task()
    if choice == 4:
        save_file()