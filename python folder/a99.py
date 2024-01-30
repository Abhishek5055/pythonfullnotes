# import time
# from plyer import notification

# time_hour = float(input("Set the hours after you want to drink water"))
# while(True):
#     time.sleep(3600*time_hour)
#     notification.notify(title="Water",message="You should drink water",timeout=2)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["complete"] else " "
            print(f"{index}. [{status}] {task['task']}")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["complete"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added!")

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            todo_list.mark_complete(task_index)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
