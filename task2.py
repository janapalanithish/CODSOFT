def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    print("--- Simple Python Calculator ---")
    
    while True:
        # 1. Get user input for numbers
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # 2. Prompt for operation choice
        print("\nSelect Operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ")

        # 3. Perform calculation and display results
        if choice == '1':
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
            
        elif choice == '3':
            print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
            
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")

        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        else:
            print("Invalid operation choice. Please try again.")

        # Ask if the user wants another go
        again = input("\nDo another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()