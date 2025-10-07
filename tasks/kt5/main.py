import tkinter as tk
from datetime import datetime

def load_tasks(filename):
    tasks = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                name, date_str = line.strip().split('|')
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    tasks.append((name, date))
                except ValueError:
                    continue  
    return tasks

def format_task(task, today):
    name, date = task
    delta = (today - date).days

    if delta > 0:
        return f"Прошло {delta} дней от {name}", 'red'
    elif delta < 0:
        return f"Осталось {-delta} дней до {name}", 'white'
    else:
        return f"Прямо щаз происходит {name}", 'orange'

def main():
    tasks = load_tasks("tasks.txt")
    today = datetime.now().date()

    root = tk.Tk()
    root.title("Что мне делать, как мне жить?")
    root.configure(bg="black")

    title = tk.Label(root, text="Мои текущие задачи", font=("Arial", 24, "bold"),
                     fg="yellow", bg="black")
    title.pack(pady=20)

    for task in sorted(tasks, key=lambda x: x[1]):
        text, color = format_task(task, today)
        label = tk.Label(root, text=text, font=("Arial", 14),
                         fg=color, bg="black")
        label.pack(anchor='w')

    root.mainloop()

main()
