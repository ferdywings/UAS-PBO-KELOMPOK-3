import random     # Mengimpor modul random untuk memilih karakter acak
import string     # Mengimpor modul string untuk mendefinisikan karakter yang digunakan dalam password
import tkinter as tk     # Mengimpor modul tkinter untuk membuat antarmuka pengguna
from tkinter import messagebox     # Mengimpor messagebox dari tkinter untuk menampilkan pesan kesalahan

def generate_password(event=None):
    # Mengambil panjang password dari kotak masukan
    length = length_entry.get()   
    try:
        length = int(length)  # Mengonversi panjang menjadi bilangan bulat
        # Menentukan karakter yang digunakan untuk menghasilkan password acak
        characters = string.ascii_letters + string.digits + string.punctuation    
        password = ''   # Variabel untuk menyimpan password

        # Menghasilkan password acak
        for _ in range(length):
            password += random.choice(characters)
        
        # Menampilkan password di label
        password_label.config(text="Password: " + password)
    except ValueError:
        # Menampilkan pesan error jika panjang password tidak valid
        messagebox.showerror("Error", "Masukkan angka sebagai panjang password!")

root = tk.Tk()  # Membuat jendela utama menggunakan tkinter
root.title("UAS PBO Kelompok 3")   # Mengatur judul jendela

# Warna Latar
root.configure(bg="#e1e1e1")

# Header
header_label = tk.Label(root, text="Random Password Generator", font=("Times New Roman", 20), bg="#e1e1e1")
header_label.pack(pady=20)   # Membuat label header dengan teks, font, dan warna latar belakang tertentu

# Password Length
length_frame = tk.Frame(root, bg="#e1e1e1")   # Membuat frame untuk panjang password dengan warna latar belakang tertentu
length_frame.pack()

length_label = tk.Label(length_frame, text=" Panjang Password :", font=("Times New Romanl", 10), bg="#e1e1e1")
length_label.pack(side=tk.LEFT, padx=10)   # Membuat label untuk teks "Panjang Password" dengan font dan warna latar belakang tertentu

length_entry = tk.Entry(length_frame, font=("Times New Roman", 10))   # Membuat kotak masukan untuk panjang password dengan font tertentu
length_entry.pack(side=tk.LEFT, padx=10)
length_entry.bind('<Return>', generate_password)  # Menghubungkan tombol "Enter" pada kotak masukan dengan fungsi generate_password

#  Pembuatan Generate Button
generate_button = tk.Button(root, text="Generate", font=("Times New Roman", 10), bg="#A9A9A9", command=generate_password)
generate_button.pack(pady=10)  # Membuat tombol "Generate" dengan teks, font, warna latar belakang, dan menghubungkannya dengan fungsi generate_password


# Password Display
password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14), bg="#e1e1e1")
password_label.pack(pady=10)   # Membuat label untuk menampilkan password dengan teks, font, dan warna latar belakang tertentu

# Memulai loop utama untuk menampilkan antarmuka pengguna
root.mainloop()
