# TECHNIQUE 4: GUI DEVELOPMENT WITH TKINTER

from tkinter import *
from tkinter import messagebox

# Key Concepts Used:
# 1. Event-driven programming
# 2. Widget hierarchy (root → frames → widgets)
# 3. pack() geometry manager
# 4. Variable binding (StringVar, BooleanVar)
# 5. Command callbacks for button actions

# Widgets Used in This Project:
#   - Tk()         : Main application window
#   - Label()      : Display text/images
#   - Entry()      : Text input fields
#   - Button()     : Clickable actions
#   - Checkbutton(): Toggle options
#   - Listbox()    : Scrollable list
#   - Toplevel()   : Secondary windows
#   - messagebox   : Popup dialogs

root = Tk()
root.title("Secure Login System")
root.geometry("450x550")
root.configure(bg="#1e1e1e")

# WIDGET 1: LABEL

# Label  — displays static text or images
# font   — (font_family, size, style)
# fg     — foreground (text) color
# bg     — background color
# pady   — internal vertical padding

title_label = Label(
    root,
    text="🛡 Cyber Security Login System",
    font=("Arial", 18, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)
title_label.pack(pady=20)

# WIDGET 2: ENTRY (Text Input Field)

# Entry  — single line text input
# show   — masks characters (show="*" for password)
# insertbackground — cursor color

username_label = Label(
    root,
    text="Username",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)
username_label.pack()

username_entry = Entry(
    root,
    width=30,
    font=("Arial", 12),
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)
username_entry.pack(pady=8)

# WIDGET 3: PASSWORD ENTRY WITH TOGGLE

# show="*" — hides password characters
# BooleanVar — tracks True/False state of checkbox

password_label = Label(
    root,
    text="Password",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)
password_label.pack()

password_entry = Entry(
    root,
    width=30,
    font=("Arial", 12),
    show="*",
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)
password_entry.pack(pady=8)

# WIDGET 4: CHECKBUTTON (Show/Hide Password)

# BooleanVar() — stores True/False value
# command      — function called on toggle

show_var = BooleanVar()

def toggle_password():
    """Toggles password visibility based on checkbox state."""
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_check = Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)
show_check.pack(pady=5)

# WIDGET 5: BUTTON

# command      — function called on button click
# relief="flat"  — removes 3D border effect
# cursor="hand2" — hand cursor on hover

def on_login():
    """Handles login button click event."""
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields required!")
    else:
        messagebox.showinfo("Success", f"Welcome, {username}!")

login_btn = Button(
    root,
    text="Login",
    command=on_login,
    width=18,
    bg="orange",
    fg="white",
    activebackground="darkorange",
    relief="flat",
    cursor="hand2",
    font=("Arial", 12, "bold")
)
login_btn.pack(pady=15)

# WIDGET 6: STRENGTH LABEL (Dynamic Update)

# .config(text=)     — updates label text at runtime
# bind("<KeyRelease>") — triggers on every keystroke

strength_label = Label(
    root,
    text="Strength: ",
    font=("Arial", 11, "bold"),
    fg="yellow",
    bg="#1e1e1e"
)
strength_label.pack(pady=5)

def show_strength(event):
    """Updates strength label on every keystroke."""
    password = password_entry.get()
    score = 0
    if len(password) >= 8:                     score += 1
    if any(c.isdigit() for c in password):     score += 1
    if any(c.isupper() for c in password):     score += 1
    if any(c in "!@#$%^&*" for c in password): score += 1

    if score <= 1:
        strength_label.config(text="Strength: Weak",   fg="red")
    elif score == 2:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="lightgreen")

# Bind keystroke event to password entry field
password_entry.bind("<KeyRelease>", show_strength)

root.mainloop()