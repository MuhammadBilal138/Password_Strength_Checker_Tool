import re

def check_passwor_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 chars!"
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contains a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak! Password must have caps letter"

    if not any(char.islower() for char in password):
        return "Weak! Password must have small letters"

    if not re.search(r'[!@#$%&*()-+=]', password):
        return "Medium: Password must contain a special chracter"

    return "Strong: Your Password is secure" 

def password_check():
    print("Welcome to Password Strength Checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this program.\nCLosing the program......")
            break
        
        result = check_passwor_strength(password)   
        print(result)


if __name__ == '__main__':
    password_check()