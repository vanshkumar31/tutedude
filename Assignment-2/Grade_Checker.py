# Grade Checker
# Function to safely get a number from the user
def user_input_number(title, is_float=False):
    while True:
        try:
            if is_float:
                number = float(input(title))
            else:
                number = int(input(title))

            return number

        except ValueError:
            print("Please enter a number, not text.")


# Function to get valid marks for a subject
def get_marks(title):
    while True:

        marks = user_input_number(
            f"Enter the marks of {title} subject: ",
            is_float=True
        )

        if marks < 0:
            print("Marks should not be less than 0.")

        elif marks > 100:
            print("Marks should not be greater than 100.")

        else:
            return marks


# Function to get all subject marks
def get_subject_marks(num_subject):
    total_marks = 0

    for sub in range(num_subject):

        # Create subject title
        if sub == 0:
            title = "1st"
        elif sub == 1:
            title = "2nd"
        elif sub == 2:
            title = "3rd"
        else:
            title = f"{sub + 1}th"

        # Get valid marks
        marks = get_marks(title)

        # Add marks to total
        total_marks += marks

    return total_marks


# Function to calculate the grade
def calculate_grade(user_marks):

    if user_marks >= 90:
        return "A"

    elif user_marks >= 80:
        return "B"

    elif user_marks >= 70:
        return "C"

    elif user_marks >= 60:
        return "D"

    else:
        return "F"


# =========================
# Main Program
# =========================

print("Welcome to Grade Checker")

# Get number of subjects
num_subject = user_input_number(
    "Enter the Number of subjects: "
)

# Make sure number of subjects is greater than 0
while num_subject <= 0:
    print("Number of subjects should be greater than 0.")

    num_subject = user_input_number(
        "Enter the Number of subjects: "
    )


# Get total marks
total_marks = get_subject_marks(num_subject)


# Calculate average
user_marks = total_marks / num_subject


# Calculate grade
grade = calculate_grade(user_marks)


# Display result
print("\n===== RESULT =====")
print(f"Total Marks: {total_marks:g}")
print(f"Percentage: {user_marks:.2f}%")
print(f"You scored a {grade} Grade!")