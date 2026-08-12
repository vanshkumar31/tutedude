def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Please Enter Number Greater than 0  "
    return x / y

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "5":
        print("Calculator exited.")
        break 
    if user_input in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "1":
            result = add(num1, num2)
            print("Result:", result)
        elif user_input == "2":
            result = subtract(num1, num2)
            print("Result:", result)
        elif user_input == "3":
            result = multiply(num1, num2)
            print("Result:", result)
        elif user_input == "4":
            result = divide(num1, num2)
            print("Result:", result)
    else:
        print("Please select an option in the range of 0 to 5")