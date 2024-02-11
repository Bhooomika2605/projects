import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_number(length):
    if length <= 0:
        return "Length should be a positive integer"
    random_number = ''.join(random.choice('0123456789') for _ in range(length))
    return random_number

def generate_random_password(length):
    characters = string.ascii_letters
    password=''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password_with_punctuation(length):
    characters = string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password_with_digits_and_punctuation(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    selected_type = type_var.get()
    length = int(length_entry.get())
    if selected_type == 1:
        result = generate_random_number(length)
    elif selected_type == 2:
        result = generate_random_password(length)
    elif selected_type == 3:
        result = generate_random_password_with_punctuation(length)
    elif selected_type == 4:
        result = generate_random_password_with_digits_and_punctuation(length)
    else:
        messagebox.showerror("Error", "Please select a valid option")
        return
    password_label.config(text="The password: " + result)


root = tk.Tk()
root.title("Random Password Generator")

type_var = tk.IntVar()
length_label = tk.Label(root, text="Enter the length of password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

type_label = tk.Label(root, text="Select type of password:")
type_label.pack()

tk.Radiobutton(root, text="Only Digits", variable=type_var, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="Only Alphabet", variable=type_var, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="Alphabet and Punctuation", variable=type_var, value=3).pack(anchor=tk.W)
tk.Radiobutton(root, text="Digits and Punctuation", variable=type_var, value=4).pack(anchor=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="",  font=("Helvetica", 16))
password_label.pack()
root.geometry("400x300")
root.mainloop()
