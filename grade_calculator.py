# Student Grade Calculator

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"


print("=" * 35)
print("     STUDENT GRADE CALCULATOR")
print("=" * 35)

# Input validation using while loop
while True:
    marks = int(input("Enter student marks (0-100): "))

    if 0 <= marks <= 100:
        break

    print("Invalid input! Marks must be between 0 and 100.")
    print("Please try again.\n")

grade = get_grade(marks)

print("\n" + "=" * 20)
print("RESULT")
print("=" * 20)
print(f"Marks : {marks}")
print(f"Grade : {grade}")

if grade == "A":
    print("Excellent! Keep up the great work!")
elif grade == "B":
    print("Good job! Keep pushing for even better results!")
else:
    print("Keep trying! Success comes with practice and effort!")

print("=" * 20)