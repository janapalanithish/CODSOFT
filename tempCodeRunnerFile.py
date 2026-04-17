import random
import string

def generate_password():
    print("--- Password Generator ---")
    
    # 1. Get user input for length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Note: Short passwords are less secure. Setting length to 8.")
            length = 8
    except ValueError:
        print("Invalid input. Defaulting to 12 characters.")
        length = 12

    # 2. Define character pools
    # We use the string module just like in your checker
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_chars = letters + digits + symbols
    
    # 3. Generate the password
    # This list comprehension is a very common way humans write this in Python
    password = "".join(random.choice(all_chars) for i in range(length))
    
    # 4. Display the result
    print("-" * 30)
    print(f"Generated Password: {password}")
    print("-" * 30)

if __name__ == "__main__":
    generate_password()