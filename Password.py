'''A password generator is a useful tool that generates strong and
 random passwords for users. This project aims to create a
 password generator application using Python, allowing users to
 specify the length and complexity of the password.
 User Input: Prompt the user to specify the desired length of the
 password.
 Generate Password: Use a combination of random characters to
 generate a password of the specified length.
 Display the Password: Print the generated password on the screen'''

import random
import string

def generate_password(length, include_special_chars=True):
    if length < 1:
        print("Password length must be at least 1.")
        return ""
    
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
            password = generate_password(length, include_special_chars)
            if password:
                print(f"Generated password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number for the length.")
        
        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
