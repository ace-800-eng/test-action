#!/usr/bin/env python3
"""
Simple Calculator Application
Performs basic arithmetic operations: addition, subtraction, multiplication, division
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def calculator():
    """Main calculator function with user interface"""
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()

    while True:
        choice = input("Enter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("Thank you for using the calculator. DUR DUR DUR!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}\n")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}\n")
                elif choice == '3':
                    print(f"\n{num1} * {num2} = {multiply(num1, num2)}\n")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    calculator()

