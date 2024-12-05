import re
import requests
from urllib.parse import urlparse

# Helper Functions
def is_ip_address(url):
    """Check if the URL uses an IP address instead of a domain."""
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    return bool(re.search(ip_pattern, url))

def has_suspicious_keywords(url):
    """Check for phishing-related keywords in the URL."""
    keywords = ['login', 'verify', 'update', 'secure', 'account', 'signin']
    return any(keyword in url.lower() for keyword in keywords)

def has_unusual_tld(url):
    """Check if the URL uses uncommon or suspicious top-level domains."""
    suspicious_tlds = ['.xyz', '.zip', '.top', '.loan', '.click']
    return any(url.endswith(tld) for tld in suspicious_tlds)

def is_url_shortened(url):
    """Check if the URL is shortened using popular shortening services."""
    shortening_services = ['bit.ly', 't.co', 'tinyurl.com', 'goo.gl']
    domain = urlparse(url).netloc
    return any(service in domain for service in shortening_services)

def check_domain_reputation(url):
    """Check the domain reputation using an external service (e.g., VirusTotal or Google Safe Browsing API)."""
    # Placeholder for domain reputation API integration
    # Return True if the domain is found in a phishing database
    return False  # Replace with actual API response in real-world use

def calculate_phishing_score(url):
    """Assign a phishing score based on detection methods."""
    score = 0
    if is_ip_address(url):
        score += 25
    if has_suspicious_keywords(url):
        score += 20
    if has_unusual_tld(url):
        score += 20
    if is_url_shortened(url):
        score += 15
    if check_domain_reputation(url):
        score += 40
    return score

def detect_phishing(url):
    """Main detection function."""
    score = calculate_phishing_score(url)
    if score > 50:
        return "Phishing Detected! Risk Score: " + str(score)
    elif 20 < score <= 50:
        return "Suspicious! Risk Score: " + str(score)
    else:
        return "Safe! Risk Score: " + str(score)

# Main Program
if __name__ == "__main__":
    print("Phishing Link Detection Tool")
    print('************************************************')
    print('************************************************')
    print('*******#####**#****#**#####**#####**#***#*******')
    print('*******#***#**#****#****#****#******#***#*******')
    print('*******####***######****#****#####**#####*******')
    print('*******#******#****#****#********#**#***#*******')
    print('*******#******#****#**#####**#####**#***#*******')
    print('************************************************')
    print('************************************************')
    user_url = input("Enter a URL to check: ").strip()
    try:
        # Validate the URL format
        if not re.match(r'https?://', user_url):
            user_url = "http://" + user_url
        print(detect_phishing(user_url))
    except Exception as e:
        print(f"Error: {e}")
