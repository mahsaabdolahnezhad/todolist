import csv
from pathlib import Path
filename = "tasks.csv"


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority


class Todolist: 
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)


    
    def remove_task(self, task):
        if not self.tasks:
            print("Sorry, the list is empty.")
            return

        self.tasks.remove(task)


    
    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"\n{index}. {task.name}")
            print(f"   Description: {task.description}")
            print(f"   Priority: {task.priority}")


    def save_tasks(self):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority"])

            for task in self.tasks:
                writer.writerow([
                    task.name,
                    task.description,
                    task.priority
                ])
    def load_tasks(self):
        if not Path(filename).exists():
            self.save_tasks()
            return

        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader , None)  # Skip the header row
            for row in reader:
                name, description, priority = row
                task = Task(name, description, priority)
                self.tasks.append(task)
            

todo = Todolist()
todo.load_tasks()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Remove task")
    print("4. Save tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Task name: ")
        description = input("Task description: ")
        priority = input("Task priority (P1/P2/P3): ")

        task = Task(name, description, priority)
        todo.add_task(task)
        todo.save_tasks()
        print("Task added!")

    elif choice == "2":
        todo.display_tasks()

    elif choice == "3":
        todo.display_tasks()

        if todo.tasks:
            try:
                number = int(input("Enter the task number to remove: "))
                task = todo.tasks[number - 1]
                todo.remove_task(task)
                todo.save_tasks()
                print("Task removed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        todo.save_tasks()
        print("Tasks saved!")

    elif choice == "5":
        todo.save_tasks()
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1–5.")
