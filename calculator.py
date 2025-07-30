import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Inputs
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar()
operation_var.set('+')  # default

operations_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operations_menu.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
