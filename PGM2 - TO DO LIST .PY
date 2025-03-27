class ToDoList:
    def __init__(self):
        self.tasks = []  # This will hold the list of tasks
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")
    
    def edit_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            old_task = self.tasks[task_index]
            self.tasks[task_index] = new_task
            print(f"Task updated: '{old_task}' -> '{new_task}'")
        else:
            print("Invalid task index.")
    
    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task deleted: {removed_task}")
        else:
            print("Invalid task index.")
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks List:")
            for idx, task in enumerate(self.tasks):
                print(f"{idx + 1}. {task}")
    

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        
        elif choice == "2":
            todo_list.display_tasks()
            try:
                task_index = int(input("Enter the task number to edit: ")) - 1
                new_task = input("Enter the new task: ")
                todo_list.edit_task(task_index, new_task)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            todo_list.display_tasks()
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            todo_list.display_tasks()
        
        elif choice == "5":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main()
