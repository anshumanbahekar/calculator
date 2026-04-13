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


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def show_menu():
    print("\n--- CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Bye Bud!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice! Try again.")
        continue

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == '1':
        result = add(num1, num2)
        symbol = '+'

    elif choice == '2':
        result = subtract(num1, num2)
        symbol = '-'

    elif choice == '3':
        result = multiply(num1, num2)
        symbol = '*'

    elif choice == '4':
        result = divide(num1, num2)
        symbol = '/'

    print(f"\nResult: {num1} {symbol} {num2} = {result}")
