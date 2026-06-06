import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import time

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()

# ---------------- PASSWORD HASH ---------------- #

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- PASSWORD STRENGTH ---------------- #

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char in "!@#$%^&*" for char in password):
        score += 1

    if score <= 1:
        return "Weak"

    elif score == 2:
        return "Medium"

    else:
        return "Strong"

# ---------------- GENERATE PASSWORD ---------------- #

def generate_password():

    password_entry.delete(0, tk.END)
    password_entry.insert(0, "Ronak@123")

# ---------------- SHOW PASSWORD ---------------- #

def toggle_password():

    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# ---------------- REGISTER ---------------- #

def register():

    username = username_entry.get()
    password = hash_password(password_entry.get())

    if username == "" or password_entry.get() == "":
        messagebox.showerror(
            "Error",
            "All fields required"
        )
        return

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Registration Successful"
    )

# ---------------- URL CHECKER ---------------- #

def check_url():

    url = url_entry.get()

    fake_score = 0

    if "@" in url:
        fake_score += 20

    if "-" in url:
        fake_score += 10

    if "http://" in url:
        fake_score += 20

    if len(url) > 30:
        fake_score += 10

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "free",
        "bonus"
    ]

    for word in suspicious_words:
        if word in url.lower():
            fake_score += 10

    if fake_score > 100:
        fake_score = 100

    real_score = 100 - fake_score

    result_label.config(
        text=f"Real: {real_score}%   Fake: {fake_score}%"
    )

    # Color Change

    if fake_score >= 70:

        result_label.config(fg="red")

        safety_label.config(
            text="⚠ Dangerous Website",
            fg="red"
        )

    elif fake_score >= 40:

        result_label.config(fg="orange")

        safety_label.config(
            text="⚠ Suspicious Website",
            fg="orange"
        )

    else:

        result_label.config(fg="lightgreen")

        safety_label.config(
            text="✓ Safe Website",
            fg="lightgreen"
        )

    # Save History

    history.insert(tk.END, url)

# ---------------- DASHBOARD ---------------- #

def open_dashboard():

    messagebox.showinfo(
        "Scanning",
        "Checking Security..."
    )

    dashboard = tk.Toplevel(root)

    dashboard.title("Cyber Dashboard")
    dashboard.geometry("550x650")
    dashboard.configure(bg="#111111")

    # Title

    welcome = tk.Label(
        dashboard,
        text="⚡ SYSTEM SECURED ⚡",
        font=("Arial", 24, "bold"),
        fg="cyan",
        bg="#111111"
    )

    welcome.pack(pady=20)

    # Project Text

    project = tk.Label(
        dashboard,
        text="Cyber Security Project Running Successfully",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#111111"
    )

    project.pack(pady=5)

    # Time Label

    time_label = tk.Label(
        dashboard,
        font=("Arial", 12),
        fg="lightgreen",
        bg="#111111"
    )

    time_label.pack(pady=5)

    def update_time():

        current = time.strftime("%H:%M:%S")

        time_label.config(text=current)

        dashboard.after(1000, update_time)

    update_time()

    # URL Label

    url_label = tk.Label(
        dashboard,
        text="Enter Website URL",
        font=("Arial", 13, "bold"),
        fg="white",
        bg="#111111"
    )

    url_label.pack(pady=10)

    # URL Entry

    global url_entry

    url_entry = tk.Entry(
        dashboard,
        width=40,
        font=("Arial", 12),
        bg="#222222",
        fg="white",
        insertbackground="white"
    )

    url_entry.pack(pady=5)

    # Check Button

    check_btn = tk.Button(
        dashboard,
        text="CHECK URL",
        command=check_url,
        bg="#00bcd4",
        fg="white",
        activebackground="#0097a7",
        relief="flat",
        cursor="hand2",
        font=("Arial", 12, "bold"),
        width=18
    )

    check_btn.pack(pady=15)

    # Result Label

    global result_label

    result_label = tk.Label(
        dashboard,
        text="",
        font=("Arial", 14, "bold"),
        bg="#111111"
    )

    result_label.pack(pady=5)

    # Safety Label

    global safety_label

    safety_label = tk.Label(
        dashboard,
        text="",
        font=("Arial", 14, "bold"),
        bg="#111111"
    )

    safety_label.pack(pady=5)

    # History Title

    history_title = tk.Label(
        dashboard,
        text="Scanned URL History",
        font=("Arial", 12, "bold"),
        fg="cyan",
        bg="#111111"
    )

    history_title.pack(pady=10)

    # History Box

    global history

    history = tk.Listbox(
        dashboard,
        width=50,
        height=8,
        bg="#222222",
        fg="white",
        font=("Arial", 10)
    )

    history.pack(pady=5)

    # Footer

    footer = tk.Label(
        dashboard,
        text="Developed By Ronak",
        font=("Arial", 10),
        fg="gray",
        bg="#111111"
    )

    footer.pack(side="bottom", pady=10)

    # Logout Button

    logout_btn = tk.Button(
        dashboard,
        text="Logout",
        command=dashboard.destroy,
        bg="red",
        fg="white",
        activebackground="darkred",
        relief="flat",
        cursor="hand2",
        font=("Arial", 12, "bold"),
        width=12
    )

    logout_btn.pack(pady=20)

# ---------------- LOGIN ---------------- #

def login():

    username = username_entry.get()
    password = hash_password(password_entry.get())

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:

        messagebox.showinfo(
            "Success",
            "Login Successful"
        )

        open_dashboard()

    else:

        messagebox.showerror(
            "Error",
            "Invalid Credentials"
        )

# ---------------- PASSWORD DISPLAY ---------------- #

def show_strength(event):

    password = password_entry.get()

    strength = check_strength(password)

    strength_label.config(
        text=f"Strength: {strength}"
    )

# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("Secure Login System")
root.geometry("450x550")
root.configure(bg="#1e1e1e")

# Title

title = tk.Label(
    root,
    text="🛡 Cyber Security Login System",
    font=("Arial", 20, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)

title.pack(pady=20)

# Username Label

username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)

username_label.pack()

# Username Entry

username_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)

username_entry.pack(pady=8)

# Password Label

password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)

password_label.pack()

# Password Entry

password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    show="*",
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)

password_entry.pack(pady=8)

password_entry.bind(
    "<KeyRelease>",
    show_strength
)

# Strength Label

strength_label = tk.Label(
    root,
    text="Strength:",
    font=("Arial", 11, "bold"),
    fg="yellow",
    bg="#1e1e1e"
)

strength_label.pack(pady=5)

# Show Password

show_var = tk.BooleanVar()

show_password = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)

show_password.pack()

# Generate Password Button

generate_btn = tk.Button(
    root,
    text="Generate Strong Password",
    command=generate_password,
    bg="#00bcd4",
    fg="white",
    activebackground="#0097a7",
    relief="flat",
    cursor="hand2",
    font=("Arial", 11, "bold"),
    width=25
)

generate_btn.pack(pady=15)

# Register Button

register_btn = tk.Button(
    root,
    text="Register",
    command=register,
    width=18,
    bg="green",
    fg="white",
    activebackground="darkgreen",
    relief="flat",
    cursor="hand2",
    font=("Arial", 12, "bold")
)

register_btn.pack(pady=10)

# Login Button

login_btn = tk.Button(
    root,
    text="Login",
    command=login,
    width=18,
    bg="orange",
    fg="white",
    activebackground="darkorange",
    relief="flat",
    cursor="hand2",
    font=("Arial", 12, "bold")
)

login_btn.pack(pady=10)

# Footer

footer_main = tk.Label(
    root,
    text="Mini Cyber Security Project",
    font=("Arial", 10),
    fg="gray",
    bg="#1e1e1e"
)

footer_main.pack(side="bottom", pady=10)

root.mainloop()
