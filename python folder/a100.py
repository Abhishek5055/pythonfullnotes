import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()
        
        self.update_task_listbox()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "complete": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["complete"] else " "
            self.task_listbox.insert(tk.END, f"{index}. [{status}] {task['task']}")
    
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["complete"] = True
            self.update_task_listbox()
            messagebox.showinfo("Task Complete", "Task marked as complete!")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
