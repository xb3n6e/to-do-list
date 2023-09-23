import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_index)
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def on_select(event):
    try:
        selected_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_task)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()
