import random
import string

def generate_password(length, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("\n----- Password Generator -----")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("⚠ Length must be greater than zero.")
            return

        symbol_choice = input("Include special symbols? (y/n): ").strip().lower()
        use_symbols = True if symbol_choice == 'y' else False

        password = generate_password(length, use_symbols)
        print(f"🔐 Generated Password: {password}")

    except ValueError:
        print("⚠ Please enter a valid number.")

password_generator()
