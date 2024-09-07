import secrets
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Ask user for input
try:
    length = int(input("Enter the desired password length: "))
    print(f"Password length: {length}")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    print(f"Include uppercase: {use_uppercase}")
    
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    print(f"Include digits: {use_digits}")
    
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    print(f"Include special characters: {use_special}")

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number for password length.")
