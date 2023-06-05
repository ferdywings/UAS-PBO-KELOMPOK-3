import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(event=None):
    length = length_entry.get()
    try:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''

        for _ in range(length):
            password += random.choice(characters)

        password_label.config(text="Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka sebagai panjang password!")

root = tk.Tk()
root.title("UAS PBO Kelompok 3")

# Warna Latar
root.configure(bg="#e1e1e1")

# Header
header_label = tk.Label(root, text="Random Password Generator", font=("Times New Roman", 20), bg="#e1e1e1")
header_label.pack(pady=20)

# Password Length
length_frame = tk.Frame(root, bg="#e1e1e1")
length_frame.pack()

length_label = tk.Label(length_frame, text=" Panjang Password :", font=("Times New Romanl", 10), bg="#e1e1e1")
length_label.pack(side=tk.LEFT, padx=10)

length_entry = tk.Entry(length_frame, font=("Times New Roman", 10))
length_entry.pack(side=tk.LEFT, padx=10)
length_entry.bind('<Return>', generate_password)  

#  Pembuatan Generate Button
generate_button = tk.Button(root, text="Generate", font=("Times New Roman", 10), bg="#A9A9A9", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14), bg="#e1e1e1")
password_label.pack(pady=10)

root.mainloop()
