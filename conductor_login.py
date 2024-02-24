import tkinter as tk
import subprocess

def login():
    email = email_entry.get()
    password = password_entry.get()
    
    # Perform authentication here, for example, check against a database
    if email == "conductor@gmail.com" and password == "password":
        result_label.config(text="Login successful")
        root.destroy()  # Close the current page
        subprocess.run(["python", "conductor.py"])  # Open the "conductor.py" script
    else:
        result_label.config(text="Login failed")

def open_main_page():
    root.destroy()  # Close the current page
    subprocess.run(["python", "main page.py"])
    
root = tk.Tk()
root.title("Conductor Sign-In")
root.geometry("400x400")
root.configure(bg="white")
root.resizable(False, False)

# Sky blue background frame with "TRIP TRAK" title
title_frame = tk.Frame(root, bg="skyblue")
title_frame.pack(fill="x")
title_label = tk.Label(title_frame, text="TRIP TRAK", font=("Arial", 20, "bold"), bg="skyblue", pady=10)
title_label.pack()

# Blue background frame with "Sign In"
signin_frame = tk.Frame(root, bg="blue")
signin_frame.pack(fill="x")
signin_label = tk.Label(signin_frame, text="SIGN IN", font=("Arial", 15, "bold"), bg="blue", fg="white")
signin_label.pack()

# Email Entry
email_label = tk.Label(root, text="Email:", font=("Arial", 12), bg="white")
email_label.pack(pady=10)
email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.pack()

# Password Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="white")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

# Login Button
login_button = tk.Button(root, text="Log In", command=login, bg="Navy", fg="white", font=("Arial", 12))
login_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
result_label.pack()

# Back Button (bottom left corner)
back_button = tk.Button(root, text="Back", command=open_main_page, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=360)

root.mainloop()
