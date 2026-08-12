# Assignment 2 - Menu-Driven Calculator

# Function for checking where user enter number or not why function follow the DRY principle
def user_input_number(title):
    while True:
        try:
            number = float(input(title))
            return number
        except ValueError:
            print("Please enter a number, not text.")

''' basic operation function add, sub,multi and divide 
In divide we check for denominator , it should not equal to 0 
if denominator equal to zero it generate the error 

why function because the assignment say
''' 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero. \nPlease Enter Number Greater than 0  "
    return x / y


while True:

    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    user_input = input("Enter your choice: ")

    if user_input == "5":
        print("Calculator exited.")
        break # use to exit from the while loop why in the top so if user want to exist we dont need to check other condition
        '''
        now as per the user CHOICE perform the action 
        also add the without function approch
        '''
    if user_input in ["1", "2", "3", "4"]:

        num1 = user_input_number("Enter first number: ")
        num2 = user_input_number("Enter second number: ")

        if user_input == "1":
            result = add(num1, num2)
            print("Result:", result)
            # print(f"Result : {num1 + num2 }")

        elif user_input == "2":
            result = subtract(num1, num2)
            print("Result:", result)
            # print(f"Result : {num1 - num2 }")

        elif user_input == "3":
            result = multiply(num1, num2)
            print("Result:", result)
            # print(f"Result : {num1 * num2 }")

        elif user_input == "4":
            result = divide(num1, num2)
            print("Result:", result)
            # if num2 ==0:
            #     print("Please Enter Number Greater than 0 ")
            #     break
            # print(f"Result : {num1 / num2 }")
    else:
        print("Invalid choice. \nPlease select an option from 1 to 5.")
'''

Note About Assignment Requirements

The attached Assignment 2 brief may differ from the requirements communicated by the mentor. This repository follows the mentor's specified requirements.

'''