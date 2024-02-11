toDoList = []

def addTask(task):
    toDoList.append(task)
    print("Task added successfully!")

def displayTasks():
    if toDoList:
        print("Your To-Do List:")
        length= len(toDoList)
        for index in range(length):
            print(str(index + 1) + ". " +toDoList[index])
    else:
        print("Your to-do list is empty!")

def removeTask():
    if toDoList:
        displayTasks()
        removeIndex = int(input("Enter the index of the task to remove: ")) - 1
        if 0 <= removeIndex < len(toDoList):
            removedTask = toDoList.pop(removeIndex)
            print("Task removed successfully!")
        else:
            print("Invalid index, Please enter a valid index.")



# Main program loop

while True:
    print("\n1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        addTask(task)
    elif choice == '2':
        displayTasks()
    elif choice== '3':
        removeTask()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")


