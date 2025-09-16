import tkinter as tk
from tkinter import messagebox
import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                line = f"{task.description}|{task.completed}\n"
                file.write(line)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    description, completed = line.strip().split("|")
                    task = Task(description)
                    task.completed = completed == "True"
                    self.tasks.append(task)

class ToDoApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("Krish's To-Do List 📝")

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack()

        self.task_listbox = tk.Listbox(root, width=70, height=15)
        self.task_listbox.pack(pady=10)

        self.refresh_task_list()

    def add_task(self):
        desc = self.task_entry.get()
        if desc.strip():
            self.todo_list.add_task(desc)
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.todo_list.remove_task(index)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task to remove!")

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.todo_list.mark_task_complete(index)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Select a task to mark complete!")

    def save_tasks(self):
        self.todo_list.save_tasks()
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
