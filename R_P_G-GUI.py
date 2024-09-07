import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)  # Clear the result field
    result_entry.insert(0, password)  # Display the generated password

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(result_entry.get())  # Append the password to clipboard
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Uppercase letters
uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, columnspan=2, padx=10, pady=5)

# Digits
digits_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, columnspan=2, padx=10, pady=5)

# Special characters
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=3, columnspan=2, padx=10, pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, columnspan=2, padx=10, pady=10)

# Result display
tk.Label(root, text="Generated Password:").grid(row=5, column=0, padx=10, pady=10)
result_entry = tk.Entry(root, width=30)
result_entry.grid(row=5, column=1, padx=10, pady=10)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, columnspan=2, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
