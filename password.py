import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip  # Make sure to install it using: pip install pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x300")

        self.password_var = tk.StringVar()
        self.password_var.set("")

        # Complexity options
        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_spinbox = ttk.Spinbox(master, from_=4, to=30, increment=1, width=5)
        self.length_spinbox.set(12)

        self.lowercase_var = tk.IntVar(value=1)
        self.lowercase_checkbox = ttk.Checkbutton(master, text="Include Lowercase", variable=self.lowercase_var)

        self.uppercase_var = tk.IntVar(value=1)
        self.uppercase_checkbox = ttk.Checkbutton(master, text="Include Uppercase", variable=self.uppercase_var)

        self.digits_var = tk.IntVar(value=1)
        self.digits_checkbox = ttk.Checkbutton(master, text="Include Digits", variable=self.digits_var)

        self.symbols_var = tk.IntVar(value=1)
        self.symbols_checkbox = ttk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var)

        # Copy to clipboard button
        self.copy_button = ttk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)

        # Generate password button
        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)

        # Display generated password
        self.password_label = ttk.Label(master, textvariable=self.password_var, font=("Courier", 12))

        # Layout
        self.length_label.grid(row=0, column=0, pady=5, sticky="w")
        self.length_spinbox.grid(row=0, column=1, pady=5, sticky="w")
        self.lowercase_checkbox.grid(row=1, column=0, pady=5, sticky="w")
        self.uppercase_checkbox.grid(row=2, column=0, pady=5, sticky="w")
        self.digits_checkbox.grid(row=3, column=0, pady=5, sticky="w")
        self.symbols_checkbox.grid(row=4, column=0, pady=5, sticky="w")
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.password_label.grid(row=6, column=0, columnspan=2, pady=10)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=5)

    def generate_password(self):
        length = int(self.length_spinbox.get())
        include_lowercase = bool(self.lowercase_var.get())
        include_uppercase = bool(self.uppercase_var.get())
        include_digits = bool(self.digits_var.get())
        include_symbols = bool(self.symbols_var.get())

        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            characters = string.ascii_letters + string.digits  # Use default if no option is selected

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
