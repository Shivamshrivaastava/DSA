# Define a to-do list class
class ToDoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, task_index):
    if 0 <= task_index < len(self.tasks):
      del self.tasks[task_index]
    else:
      print("Invalid task index.")

  def print_list(self):
    if len(self.tasks) == 0:
      print("No tasks in the list.")
    else:
      for i, task in enumerate(self.tasks):
        print(f"{i+1}. {task}")

# Create a to-do list object
todo_list = ToDoList()

# Main loop for user interaction
while True:
  print("\nTo-Do List:")
  todo_list.print_list()

  print("\nOptions:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Exit")

  choice = input("Enter your choice (1/2/3): ")

  if choice == "1":
    task = input("Enter a new task: ")
    todo_list.add_task(task)
    print("Task added successfully.")

  elif choice == "2":
    todo_list.print_list()
    task_index = int(input("Enter the index of the task to remove: ")) - 1
    todo_list.remove_task(task_index)

  elif choice == "3":
    print("Exiting program.")
    break

  else:
    print("Invalid choice. Please try again.")
