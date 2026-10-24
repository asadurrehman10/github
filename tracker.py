tasks = []


def add_task(task):
    """Add a task to the list and confirm it."""
    tasks.append(task)
    print(f"Added: {task}")


def show_tasks():
    """Print all tasks as a numbered list."""
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


# The program starts here
task = input("Enter the task: ")  # input() is called OUTSIDE the function
add_task(task)                    # pass the typed text into the function
show_tasks()

# i make some changes to push on second branch

def show_count():
    print(f"Total tasks: {len(tasks)}")