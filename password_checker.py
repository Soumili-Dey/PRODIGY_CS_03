import re
import getpass  # For secure password input

def evaluate_password_strength(password):
    """Analyze password and return strength score and feedback"""
    
    strength = 0
    feedback = []
    
    # Length check
    length = len(password)
    if length >= 12:
        strength += 3
        feedback.append("✓ Good length (12+ characters)")
    elif length >= 8:
        strength += 2
        feedback.append("✓ Moderate length (8-11 characters)")
    else:
        feedback.append("✗ Too short (minimum 8 characters recommended)")
    
    # Character diversity checks
    criteria = [
        (r'[A-Z]', "uppercase letter"),
        (r'[a-z]', "lowercase letter"),
        (r'[0-9]', "digit"),
        (r'[^A-Za-z0-9]', "special character")
    ]
    
    for pattern, description in criteria:
        if re.search(pattern, password):
            strength += 1
            feedback.append(f"✓ Contains {description}")
        else:
            feedback.append(f"✗ Missing {description}")
    
    # Common password check
    common_passwords = ['password', '123456', 'qwerty', 'letmein', 'welcome']
    if password.lower() in common_passwords:
        strength = 0
        feedback.append("✗ Extremely weak (common password)")
    
    # Sequential/repeating characters check
    if re.search(r'(.)\1{2,}', password):
        strength -= 1
        feedback.append("✗ Avoid repeating characters")
    
    if re.search(r'(abc|123|qwe|asd|xyz)', password.lower()):
        strength -= 1
        feedback.append("✗ Avoid simple sequences")
    
    # Strength classification
    if strength >= 7:
        rating = "STRONG"
    elif strength >= 4:
        rating = "MODERATE"
    else:
        rating = "WEAK"
    
    return strength, rating, feedback

def display_results(password, strength, rating, feedback):
    """Display password analysis results"""
    
    print("\n" + "="*50)
    print("Password Strength Analysis".center(50))
    print("="*50)
    
    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength Score: {strength}/7")
    print(f"Rating: {rating}\n")
    
    print("Detailed Feedback:")
    for item in feedback:
        print(f" - {item}")
    
    print("\n" + "="*50)

def main():
    print("Password Strength Checker")
    print("------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Exit")
        
        choice = input("Enter choice (1/2): ")
        
        if choice == '1':
            password = getpass.getpass("Enter password (input hidden): ")
            
            if not password.strip():
                print("Error: Password cannot be empty")
                continue
            
            strength, rating, feedback = evaluate_password_strength(password)
            display_results(password, strength, rating, feedback)
            
            # Suggest improvements for weak passwords
            if rating == "WEAK":
                print("\nRecommendations to improve your password:")
                print("- Make it at least 12 characters long")
                print("- Use a mix of uppercase and lowercase letters")
                print("- Include numbers and special characters (!@#$%^&*)")
                print("- Avoid common words and patterns")
        
        elif choice == '2':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()