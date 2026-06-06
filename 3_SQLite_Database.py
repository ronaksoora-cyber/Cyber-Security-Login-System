# TECHNIQUE 3: DATABASE SECURITY WITH SQLite3

import sqlite3
import hashlib

# OVERVIEW

# SQLite3 is a lightweight, serverless, file-based
# database engine built into Python.

# Security Implementation:
# 1. Passwords stored as SHA-256 hashes (never plain text)
# 2. Parameterized queries prevent SQL Injection attacks
# 3. Single .db file — no server configuration required


# Database Schema:
# Table: users
#   - id       : INTEGER PRIMARY KEY AUTOINCREMENT
#   - username : TEXT
#   - password : TEXT (SHA-256 hash)


# DATABASE CONNECTION

# Creates users.db file if it doesn't exist
conn   = sqlite3.connect("users.db")
cursor = conn.cursor()

# TABLE CREATION

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
conn.commit()

# CORE FUNCTIONS

def hash_password(password):
    """Converts plain text password to SHA-256 hash."""
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    """
    Registers a new user with hashed password.
    Uses parameterized query to prevent SQL Injection.
    
    Args:
        username (str): Chosen username
        password (str): Plain text password (will be hashed)
    """
    hashed = hash_password(password)
    
    # Parameterized query (?) prevents SQL Injection
    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?)",
        (username, hashed)
    )
    conn.commit()
    print(f"[SUCCESS] User '{username}' registered successfully!")


def login_user(username, password):
    """
    Authenticates user by comparing hashed passwords.
    
    Args:
        username (str): Username to authenticate
        password (str): Plain text password to verify
    Returns:
        bool: True if authenticated, False otherwise
    """
    hashed = hash_password(password)
    
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )
    
    user = cursor.fetchone()
    
    if user:
        print(f"[SUCCESS] Login successful! Welcome, {username}")
        return True
    else:
        print("[ERROR] Invalid credentials!")
        return False


# DEMONSTRATION

if __name__ == "__main__":

    print("=" * 50)
    print("     SQLite3 DATABASE DEMONSTRATION")
    print("=" * 50)

    # Register a new user
    register_user("ronak", "Ronak@123")

    print("-" * 50)

    # Valid login attempt
    login_user("ronak", "Ronak@123")

    # Invalid login attempt
    login_user("ronak", "wrongpassword")

    print("=" * 50)