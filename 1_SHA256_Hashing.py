# TECHNIQUE 1: SHA-256 CRYPTOGRAPHIC HASHING

import hashlib

# OVERVIEW

# SHA-256 (Secure Hash Algorithm - 256 bit) is a
# cryptographic hash function that converts any
# input string into a fixed 256-bit (64 character)
# hexadecimal string.

# Key Properties:
# 1. Deterministic   - Same input always produces same output
# 2. One-way         - Hash cannot be reversed to original
# 3. Collision-free  - No two inputs produce the same hash
# 4. Avalanche Effect- Small input change = completely different hash

def hash_password(password):
    """
    Converts plain text password into SHA-256 hash.
    
    Args:
        password (str): Plain text password
    Returns:
        str: 64-character hexadecimal hash string
    """
    # .encode() converts string to bytes (required by hashlib)
    # .hexdigest() returns hash as readable hexadecimal string
    return hashlib.sha256(password.encode()).hexdigest()

# DEMONSTRATION

if __name__ == "__main__":
    
    password = "Ronak@123"
    hashed   = hash_password(password)
    
    print("=" * 55)
    print("       SHA-256 HASHING DEMONSTRATION")
    print("=" * 55)
    print(f"Original Password : {password}")
    print(f"SHA-256 Hash      : {hashed}")
    print(f"Hash Length       : {len(hashed)} characters")
    print("-" * 55)
    
    # Verifying deterministic property
    print("Verification      :", 
    hash_password("Ronak@123") == hashed)
    print("=" * 55)