import sys
import os

TODO_FILE = "todo.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"✅ Task added: {task}")

def list_tasks():
    if not os.path.exists(TODO_FILE):
        print("📭 No tasks found.")
        return
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    print("📝 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("📌 Usage: python todo.py [add/list] [task]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()

