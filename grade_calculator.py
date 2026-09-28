def calculate_grade(marks):
    """
    Calculate grade and display an encouraging message
    based on the student's marks.
    """

    if marks >= 90:
        return "A", "Excellent work! Keep shining!"

    elif marks >= 80:
        return "B", "Very good! Keep it up!"

    elif marks >= 70:
        return "C", "Good effort! Keep improving!"

    elif marks >= 60:
        return "D", "You passed! Keep practicing!"

    else:
        return "F", "Don't give up! Learn and try again!"


def get_valid_marks():
    """
    Ask the user for marks and validate the input.
    """

    while True:
        try:
            marks = int(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    """
    Main function of the Student Grade Calculator.
    """

    print("=" * 50)
    print("           STUDENT GRADE CALCULATOR")
    print("=" * 50)

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n" + "=" * 50)
    print("             RESULT")
    print("=" * 50)
    print(f"Student Name : {name}")
    print(f"Marks        : {marks}")
    print(f"Grade        : {grade}")
    print(f"Message      : {message}")
    print("=" * 50)


if __name__ == "__main__":
    main()