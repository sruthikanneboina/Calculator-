import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field for input and output
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define buttons and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 14),
                  command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=132, pady=20, font=('Arial', 14),
                  command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 14),
                  command=lambda t=text: click(t)).grid(row=row, column=col)

# Run the application
root.mainloop()

