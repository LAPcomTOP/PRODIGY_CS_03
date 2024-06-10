import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    digits = re.compile(r'[0-9]')
    special_chars = re.compile(r'[^a-zA-Z0-9]')
    
    
    min_length = 8
    
    if len(password) < min_length:
        strength_label.config(text="Password is too short. Minimum length should be {} characters".format(min_length), fg="red")
        return
    
    if not lower_case.search(password):
        strength_label.config(text="Password must contain at least one lower letter.", fg="red")
        return
    
    if not  upper_case.search(password):
        strength_label.config(text="Password must contain at least one uppercase letter", fg="red")
        return
    
    if not digits.search(password):
        strength_label.config(text="Password must contain at least one digits", fg="red")
        return
    
    if not special_chars.search(password):
        strength_label.config(text="Password must contain at least one special character.", fg="red")
        return
    
    strength_label.config(text="Password is strong.", fg="green")
    
    
root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack()


strength_label = tk.Label(root, text="", fg="black")
strength_label.pack()

root.mainloop
