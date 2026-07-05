import tkinter as tk
from tkinter import messagebox
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
expenses = []

def add_expense():
    expense = entry_expense.get()

    if expense == "":
        messagebox.showwarning("Warning", "Please enter an expense amount!")
        return

    try:
        amount = float(expense)

        if amount <= 0:
            messagebox.showerror("Error", "Expense must be greater than 0!")
            return

        expenses.append(amount)

        expense_list.insert(tk.END, f"₹ {amount:.2f}")

        total = sum(expenses)
        total_label.config(text=f"Total Spent: ₹ {total:.2f}")

        entry_expense.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def clear_expenses():
    expenses.clear()
    expense_list.delete(0, tk.END)
    total_label.config(text="Total Spent: ₹ 0.00")


# ==========================
# MAIN WINDOW
# ==========================
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x600")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# ==========================
# HEADING
# ==========================
title = tk.Label(
    root,
    text="💰 Expense Tracker",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="#FFD700"
)
title.pack(pady=20)

# ==========================
# INPUT FRAME
# ==========================
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

entry_expense = tk.Entry(
    input_frame,
    font=("Arial", 14),
    width=20,
    justify="center"
)
entry_expense.grid(row=0, column=0, padx=10)

add_btn = tk.Button(
    input_frame,
    text="Add Expense",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    command=add_expense
)
add_btn.grid(row=0, column=1)

# ==========================
# EXPENSE LIST
# ==========================
list_frame = tk.Frame(root, bg="#1e1e2f")
list_frame.pack(pady=20)

expense_list = tk.Listbox(
    list_frame,
    width=35,
    height=12,
    font=("Arial", 12),
    bg="#2d2d44",
    fg="white",
    selectbackground="#4CAF50"
)
expense_list.pack()

# ==========================
# TOTAL LABEL
# ==========================
total_label = tk.Label(
    root,
    text="Total Spent: ₹ 0.00",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#00FFAA"
)
total_label.pack(pady=20)

# ==========================
# CLEAR BUTTON
# ==========================
clear_btn = tk.Button(
    root,
    text="Clear All",
    font=("Arial", 12, "bold"),
    bg="#E53935",
    fg="white",
    width=15,
    command=clear_expenses
)
clear_btn.pack(pady=10)

# ==========================
# FOOTER
# ==========================
footer = tk.Label(
    root,
    text="Track your spending wisely 📊",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="lightgray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()