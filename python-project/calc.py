import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

# Color scheme
bg_color = "black"
fg_color = "white"
button_color = "blue"
button_fg_color = "white"

window.configure(bg=bg_color)

# Global variables
operand1 = ""
operator = ""
operand2 = ""
result = None

# Function to update label with current value
def updateLabel():
    global operand1, operator, operand2, result
    expression = operand1 + " " + operator + " " + operand2
    if result is not None:
        expression += " = " + str(result)
    hello["text"] = expression

# Function to handle button clicks for numbers and operators
def buttonClick(char):
    global operand1, operator, operand2, result
    if result is not None:
        operand1, operator, operand2, result = "", "", "", None
    if char in '0123456789':
        if operator == "":
            operand1 += char
        else:
            operand2 += char
    elif char == '.' and '.' not in (operand2 if operator else operand1):
        if operator == "":
            operand1 += char
        else:
            operand2 += char
    elif char in '+-*/':
        if operand1 and not operand2:
            operator = char
    updateLabel()

# Function to evaluate the expression and display result
def calculate():
    global operand1, operator, operand2, result
    if operand1 and operator and operand2:
        try:
            if operator == '+':
                result = float(operand1) + float(operand2)
            elif operator == '-':
                result = float(operand1) - float(operand2)
            elif operator == '*':
                result = float(operand1) * float(operand2)
            elif operator == '/':
                if float(operand2) != 0:
                    result = float(operand1) / float(operand2)
                else:
                    result = "Error: Division by zero"
            if result == int(result):
                result = int(result)
        except ValueError:
            result = "Error: Invalid input"
        updateLabel()
        operand1, operator, operand2 = str(result), "", ""  # Prepare for next calculation
    else:
        hello["text"] = "Error: Incomplete expression"

# Function to clear the entire expression
def clear():
    global operand1, operator, operand2, result
    operand1, operator, operand2, result = "", "", "", None
    updateLabel()

# Function to delete the last character
def delete():
    global operand1, operator, operand2
    if operator == "":
        operand1 = operand1[:-1]
    else:
        operand2 = operand2[:-1]
    updateLabel()

# Function to handle keypress events
def keyPress(event):
    if event.char.isdigit() or event.char in '+-*/.':
        buttonClick(event.char)
    elif event.char == '\r':  # Enter key
        calculate()
    elif event.char == '\x08':  # Backspace key
        delete()
    elif event.char == '\x1b':  # Escape key
        clear()

# Create Label widget
hello = tk.Label(window, text="", bg=bg_color, fg=fg_color, font=("Arial", 24))
hello.grid(row=0, column=0, columnspan=4)

# Create Number Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('AC', 5, 0), ('DEL', 5, 1)
]
for (text, row, col) in buttons:
    action = lambda x=text: buttonClick(x) if x not in ['=', 'AC', 'DEL'] else calculate() if x == '=' else clear() if x == 'AC' else delete()
    tk.Button(window, text=text, command=action, bg=button_color, fg=button_fg_color, font=("Arial", 18)).grid(row=row, column=col, sticky="nsew")

# Set up grid weights
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Bind keypress events
window.bind('<Key>', keyPress)

window.mainloop()
