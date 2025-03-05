import json
import random
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Motivational Quotes
QUOTES = [
    "Believe in yourself and all that you are!",
    "Your only limit is your mind.",
    "Do something today that your future self will thank you for.",
    "Small progress is still progress!",
    "You are capable of amazing things!"
]

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_quote():
    """Show a random motivational quote."""
    print("\n🌟 Daily Motivation 🌟")
    print(random.choice(QUOTES))
    print("-" * 30)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet! Start by adding one.")
        return
    print("\n📌 Your Tasks:")
    completed = sum(1 for t in tasks if t["done"])
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    
    # Show progress
    if tasks:
        progress = (completed / len(tasks)) * 100
        print(f"\n📊 Progress: {progress:.2f}% completed")

def mark_done(index):
    """Mark a task as done."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Task marked as done: {tasks[index]['task']}")
    else:
        print("❌ Invalid task number!")

def delete_task(index):
    """Delete a task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed_task['task']}")
    else:
        print("❌ Invalid task number!")

# Main CLI loop
def main():
    show_quote()
    while True:
        print("\nCommands: add/view/done/delete/exit")
        command = input("Enter command: ").strip().lower()
        
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        
        elif command == "view":
            view_tasks()
        
        elif command == "done":
            index = int(input("Enter task number: ")) - 1
            mark_done(index)
        
        elif command == "delete":
            index = int(input("Enter task number: ")) - 1
            delete_task(index)
        
        elif command == "exit":
            print("Goodbye! Stay motivated! 🚀")
            break
        
        else:
            print("❌ Invalid command! Try again.")

if __name__ == "__main__":
    main()
