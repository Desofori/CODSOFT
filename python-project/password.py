import tkinter as tk
import random
import string

# Initialize the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")


# Function to generate password
def generate_password():
    length = int(length_entry.get())
    chars = ""
    if include_uppercase.get():
        chars += string.ascii_uppercase
    if include_lowercase.get():
        chars += string.ascii_lowercase
    if include_digits.get():
        chars += string.digits
    if include_special.get():
        chars += string.punctuation

    if chars:
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text="Generated Password: " + password)
    else:
        result_label.config(text="Error: Select at least one character set")


# Create UI components
frame = tk.Frame(window)
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(frame, width=5)
length_entry.pack(side=tk.LEFT, padx=5)

options_frame = tk.Frame(window)
options_frame.pack(pady=10)

include_uppercase = tk.BooleanVar()
include_lowercase = tk.BooleanVar()
include_digits = tk.BooleanVar()
include_special = tk.BooleanVar()

uppercase_check = tk.Checkbutton(options_frame, text="Uppercase Letters", variable=include_uppercase)
uppercase_check.pack(side=tk.LEFT, padx=5)

lowercase_check = tk.Checkbutton(options_frame, text="Lowercase Letters", variable=include_lowercase)
lowercase_check.pack(side=tk.LEFT, padx=5)

digits_check = tk.Checkbutton(options_frame, text="Digits", variable=include_digits)
digits_check.pack(side=tk.LEFT, padx=5)

special_check = tk.Checkbutton(options_frame, text="Special Characters", variable=include_special)
special_check.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()
