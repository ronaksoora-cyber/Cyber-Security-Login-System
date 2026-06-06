# TECHNIQUE 5: FAKE URL DETECTION ENGINE

# OVERVIEW

# A rule-based phishing URL detection algorithm
# that analyzes URLs for suspicious indicators
# and calculates a Real% vs Fake% threat score.

# Detection Parameters:
# 1. Presence of '@' symbol       (+20 points)
# 2. Use of HTTP instead of HTTPS (+20 points)
# 3. Presence of hyphens '-'      (+10 points)
# 4. URL length exceeding 30 chars(+10 points)
# 5. Suspicious keywords          (+10 each):
#    - login, verify, bank, free, bonus

# Threat Classification:
#   0  - 39  : Safe Website       (Green)
#   40 - 69  : Suspicious Website (Orange)
#   70 - 100 : Dangerous Website  (Red)


# CORE DETECTION FUNCTION


def check_url(url):
    """
    Analyzes a URL for phishing indicators.
    
    Args:
        url (str): Website URL to analyze
    Returns:
        dict: Contains fake_score, real_score, verdict
    """
    fake_score = 0

# Rule 1: '@' symbol in URL
# Real domain appears AFTER '@' in such URLs
# Example: paypal.com@evil.com (real = evil.com!)
    if "@" in url:
        fake_score += 20

# Rule 2: HTTP instead of HTTPS
# No SSL encryption — data sent in plain text
    if "http://" in url:
        fake_score += 20

# Rule 3: Hyphens in domain
# Hackers use hyphens to mimic legitimate domains
# Example: sbi-bank-login.com
    if "-" in url:
        fake_score += 10

# Rule 4: Excessively long URL

# Phishing URLs are often very long to hide true domain
    if len(url) > 30:
        fake_score += 10


# Rule 5: Suspicious keywords

# Common words used in phishing URLs to create urgency
    suspicious_words = ["login", "verify", "bank",
                        "free", "bonus"]

    for word in suspicious_words:
        if word in url.lower():
            fake_score += 10

# Cap score at 100
    if fake_score > 100:
        fake_score = 100

    real_score = 100 - fake_score

# Threat classification
    if fake_score >= 70:
        verdict = "DANGEROUS"
    elif fake_score >= 40:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return {
        "url"        : url,
        "fake_score" : fake_score,
        "real_score" : real_score,
        "verdict"    : verdict
    }


# DEMONSTRATION

if __name__ == "__main__":

    test_urls = [
        "https://www.sbi.co.in/netbanking",
        "http://sbi-bank-login-verify.com",
        "http://free-bonus-verify@evil.com/login",
        "https://www.google.com",
    ]

    print("=" * 60)
    print("        FAKE URL DETECTION ENGINE")
    print("=" * 60)

    for url in test_urls:
        result = check_url(url)
        print(f"\nURL     : {result['url']}")
        print(f"Real    : {result['real_score']}%  "
        f"Fake: {result['fake_score']}%")
        print(f"Verdict : {result['verdict']}")
        print("-" * 60)