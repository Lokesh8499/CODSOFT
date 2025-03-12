import random
import string

def generate_password(length):
    if length < 4:  # Ensure password length is at least 4 for security
        print("Password length should be at least 4.")
        return None
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
