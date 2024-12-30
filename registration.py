import sqlite3
import tkinter as tk
from tkinter import messagebox


# first_name = tk.StringVar()
# last_name = tk.StringVar()
# email = tk.StringVar()
# username = tk.StringVar()
# Phoneno = tk.IntVar()
# password = tk.StringVar()



def create_table():
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user (
                 first_name TEXT,
                 last_name TEXT,
                 email TEXT,
                 username TEXT,
                 password TEXT)''')
    conn.commit()
    conn.close()




def register():
    create_table()
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO user (first_name, last_name, email, username, password) VALUES (?, ?, ?, ?, ?)",
                  (first_name_entry.get(), last_name_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Registration Failed.")
    conn.close()

root = tk.Tk()
root.title("Electricity Theft Detection")
root.geometry("500x500")

# Set up background color
root.configure(bg="#292929")

# Add title label
title_label = tk.Label(root, text="Electricity Theft Detection", font=("Helvetica", 20), fg="#ffffff", bg="#292929")
title_label.pack(pady=20)

# Add registration frame
registration_frame = tk.Frame(root, bg="#383838", pady=10)
registration_frame.pack(pady=20)

# Add registration labels
first_name_label = tk.Label(registration_frame, text="First Name", font=("Helvetica", 14), fg="#ffffff", bg="#383838")
first_name_label.grid(row=0, column=0, padx=10, pady=5)
last_name_label = tk.Label(registration_frame, text="Last Name", font=("Helvetica", 14), fg="#ffffff", bg="#383838")
last_name_label.grid(row=1, column=0, padx=10, pady=5)
email_label = tk.Label(registration_frame, text="Email ID", font=("Helvetica", 14), fg="#ffffff", bg="#383838")
email_label.grid(row=2, column=0, padx=10, pady=5)
username_label = tk.Label(registration_frame, text="Username", font=("Helvetica", 14), fg="#ffffff", bg="#383838")
username_label.grid(row=3, column=0, padx=10, pady=5)
password_label = tk.Label(registration_frame, text="Password", font=("Helvetica", 14), fg="#ffffff", bg="#383838")
password_label.grid(row=4, column=0, padx=10, pady=5)

# Add registration entry fields
first_name_entry = tk.Entry(registration_frame, font=("Helvetica", 14), bg="#ffffff")
first_name_entry.grid(row=0, column=1, padx=10, pady=5)
last_name_entry = tk.Entry(registration_frame, font=("Helvetica", 14), bg="#ffffff")
last_name_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry = tk.Entry(registration_frame, font=("Helvetica", 14), bg="#ffffff")
email_entry.grid(row=2, column=1, padx=10, pady=5)
username_entry = tk.Entry(registration_frame, font=("Helvetica", 14), bg="#ffffff")
username_entry.grid(row=3, column=1, padx=10, pady=5)
password_entry = tk.Entry(registration_frame, font=("Helvetica", 14), bg="#ffffff", show="*")
password_entry.grid(row=4, column=1, padx=10, pady=5)


# Create a button to submit the form
submit_btn = tk.Button(root, text="Register", font=("Helvetica", 15), fg="#e6e6e6", bg="#383838", command=register)
submit_btn.pack(pady=10)

# Create a link to the login page
login_label = tk

root.mainloop()



