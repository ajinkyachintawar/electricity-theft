import tkinter as tk
import sqlite3
from tkinter import messagebox as ms


# Initialize the database connection
conn = sqlite3.connect('evaluation.db')
c = conn.cursor()



# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# Set up the tkinter window
root = tk.Tk()
root.title("Electricity Theft Detection - Login")
root.geometry("500x300")
root.configure(bg="#303030")
root.resizable(False, False)
username = tk.StringVar()
password = tk.StringVar()


# Define functions
def login():
    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            
            from subprocess import call
            call(['python','ELECTRICITY_THEFT.py'])
            
            root.destroy()

            

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



def register():
    # Code for registering a new user goes here
    from subprocess import call
    call(["python", "registration.py"])


# Add widgets to the window
title_label = tk.Label(root, text="Electricity Theft Detection", font=("Arial", 24), bg="#303030", fg="white")
title_label.pack(pady=20)

login_frame = tk.Frame(root, bg="#404040", padx=20, pady=10)
login_frame.pack()

username_label = tk.Label(login_frame, text="Username:", bg="#404040", fg="white")
username_label.grid(row=0, column=0, sticky="W")

username_entry = tk.Entry(login_frame, bg="white", width=30)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:", bg="#404040", fg="white")
password_label.grid(row=1, column=0, sticky="W")

password_entry = tk.Entry(login_frame, bg="white", width=30, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login, bg="#606060", fg="white")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

error_label = tk.Label(login_frame, text="", bg="#404040", fg="red")
error_label.grid(row=3, column=0, columnspan=2, pady=10)

register_label = tk.Label(root, text="Don't have an account?", bg="#303030", fg="white")
register_label.pack(pady=5)

register_button = tk.Button(root, text="Register Here", command=register, bg="#606060", fg="white")
register_button.pack()


root.mainloop()

# Close the database connection
conn.close()
