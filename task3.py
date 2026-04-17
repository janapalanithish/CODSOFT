import random
import string

def get_password_settings():
    """Prompts the user for length and complexity levels."""
    print("--- Password Generator Settings ---")
    
    # 1. Prompt for Length
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # 2. Prompt for Complexity
    print("\nSelect Complexity Level:")
    print("1. Low (Letters only)")
    print("2. Medium (Letters & Numbers)")
    print("3. High (Letters, Numbers, & Symbols)")
    
    choice = input("Choice (1-3): ")
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if choice == "1":
        char_pool = letters
    elif choice == "2":
        char_pool = letters + digits
    else:
        # Default to high complexity if input is weird or "3"
        char_pool = letters + digits + symbols

    return length, char_pool

def main():
    # Get user preferences
    length, characters = get_password_settings()

    # 3. Generate Password
    # Using random.choice in a loop is the standard 'human' way to do this
    pwd_list = []
    for _ in range(length):
        pwd_list.append(random.choice(characters))
    
    generated_password = "".join(pwd_list)

    # 4. Display the Password
    print("\n" + "="*30)
    print(f"Your Generated Password: {generated_password}")
    print("="*30)

if __name__ == "__main__":
    main()