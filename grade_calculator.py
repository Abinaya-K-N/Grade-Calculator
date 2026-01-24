# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining."
    elif marks >= 80:
        return "B", "Very good! Keep it up."
    elif marks >= 70:
        return "C", "Good effort! You can do better."
    elif marks >= 60:
        return "D", "You passed. Work harder."
    else:
        return "F", "Don’t give up. Try again."

# Get student name
student_name = input("Enter student name: ")

# Validate marks using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid input. Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter numbers only.")

# Get grade and message
grade, message = calculate_grade(marks)

# Display result
print("\nRESULT FOR", student_name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
