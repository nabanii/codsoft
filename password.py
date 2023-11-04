import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=40, pady=40)

length_label = tk.Label(frame, text="Enter password length:-")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_label = tk.Label(frame, text="")
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()