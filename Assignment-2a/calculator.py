# Assignment 2 - Menu-Driven Calculator

# Function to safely get a number from the user
def user_input_number(title):
    while True:
        try:
            number = float(input(title))
            return number
        except ValueError:
            print("Please enter a number, not text.")
# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    # Check for division by zero before performing division
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y


# Main calculator loop
while True:

    # Display calculator menu
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get operation choice from the user
    choice = input("Enter your choice: ")

    # Exit the calculator
    if choice == "5":
        print("Calculator exited.")
        break

    # Check whether the selected operation is valid
    if choice in ["1", "2", "3", "4"]:

        # Get numbers from the user
        num1 = user_input_number("Enter first number: ")
        num2 = user_input_number("Enter second number: ")

        # Perform the selected operation
        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)

        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == "4":
            result = divide(num1, num2)
            print("Result:", result)

    else:
        print("Invalid choice. Please select an option from 1 to 5.")