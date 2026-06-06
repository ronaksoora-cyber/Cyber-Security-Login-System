# TECHNIQUE 2: REAL-TIME PASSWORD STRENGTH ANALYZER

# OVERVIEW

# A real-time password strength evaluation system
# that analyzes passwords based on 4 security
# parameters and classifies them as:
# Weak / Medium / Strong

# Evaluation Parameters:
# 1. Minimum length  >= 8 characters
# 2. Contains digits (0-9)
# 3. Contains uppercase letters (A-Z)
# 4. Contains special characters (!@#$%^&*)

def check_strength(password):
    """
    Evaluates password strength using 4-parameter scoring.
    
    Args:
        password (str): Password to evaluate
    Returns:
        str: Strength level - 'Weak', 'Medium', or 'Strong'
    """
    score = 0

    # Parameter 1: Length check
    if len(password) >= 8:
        score += 1

    # Parameter 2: Digit presence check
    if any(char.isdigit() for char in password):
        score += 1

    # Parameter 3: Uppercase letter check
    if any(char.isupper() for char in password):
        score += 1

    # Parameter 4: Special character check
    if any(char in "!@#$%^&*" for char in password):
        score += 1

    # Classification based on score
    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    else:
        return "Strong"


# DEMONSTRATION

if __name__ == "__main__":

    test_passwords = [
        "ronak",
        "ronak123",
        "Ronak123",
        "Ronak@123",
    ]

    print("=" * 45)
    print("   PASSWORD STRENGTH ANALYZER")
    print("=" * 45)
    print(f"{'Password':<20} {'Strength'}")
    print("-" * 45)

    for pwd in test_passwords:
        strength = check_strength(pwd)
        print(f"{pwd:<20} {strength}")

    print("=" * 45)