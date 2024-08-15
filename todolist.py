import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Protected To-Do List App")
        self.tasks = []  # Store tasks

        # Set window background color
        self.root.configure(bg="#F5F5F5")  # White Smoke

        # Create widgets with updated colors
        self.task_entry = tk.Entry(root, width=50, bg="#FFF5EE")  # Seashell background for the entry field
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#FFB6C1", fg="#2F4F4F")  # Light Pink button
        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks, bg="#FFB6C1", fg="#2F4F4F")  # Light Pink button
        self.hide_button = tk.Button(root, text="Hide Tasks", command=self.hide_tasks, bg="#FFB6C1", fg="#2F4F4F")  # Light Pink button
        self.task_listbox = tk.Listbox(root, width=50, height=10, bg="#E6F7FF", fg="#004080")  # Light Sky Blue listbox, Navy Blue text
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#FFB6C1", fg="#2F4F4F")  # Light Pink button
        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task, bg="#FFB6C1", fg="#2F4F4F")  # Light Pink button

        # Place widgets
        self.task_entry.pack(pady=10)
        self.add_button.pack(pady=5)
        self.show_button.pack(pady=5)
        self.hide_button.pack(pady=5)
        self.task_listbox.pack(pady=10)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.edit_button.pack(side=tk.LEFT, padx=5)

    def password_protect(self, action):
        password = simpledialog.askstring("Password", "Enter password to view tasks:")
        if password == "reno@2004":  # Replace with your actual password
            action()
        else:
            messagebox.showerror("Error", "Incorrect password.")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self._add_task(task)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def _add_task(self, task):
        self.tasks.append(task)  # Add task to the list
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully.")

    def show_tasks(self):
        self.password_protect(self._display_tasks)

    def _display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    def hide_tasks(self):
        self.task_listbox.delete(0, tk.END)  # Clear the display listbox
        # Optionally, you can perform other actions here if needed

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self._delete_task(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def _delete_task(self, index):
        del self.tasks[index]  # Remove task from the list
        self.task_listbox.delete(index)  # Remove task from the listbox

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Enter new task:")
            if new_task:
                self._edit_task(selected_task_index, new_task)
            else:
                messagebox.showwarning("Input Error", "Please enter a task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def _edit_task(self, index, new_task):
        self.tasks[index] = new_task  # Update task in the list
        self.show_tasks()  # Refresh the listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
