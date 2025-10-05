# Scenario 1: File Processing and Exception Handling

class InvalidGradeError(Exception):
    """Custom exception for invalid grade values."""
    pass

def read_student_records(filename):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

    grades = []
    for record in students:
        record = record.strip()
        if not record:
            continue  # Skip empty lines
        try:
            # Ensure the line has exactly 2 parts: name and grade
            name, grade = record.split(',')
            name, grade = name.strip(), grade.strip()
            try:
                grade = float(grade)
                grades.append(grade)
            except ValueError:
                print(f"Invalid grade for {name}: {grade}. Skipping record.")
        except ValueError:
            print(f"Invalid line format: '{record}'. Skipping record.")
    return grades

def calculate_average(grades):
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0

# Main Program
filename = "student_records.txt"
grades = read_student_records(filename)

if grades:
    average = calculate_average(grades)
    print(f"Average Grade: {average:.2f}")
else:
    print("No valid grades found. Average cannot be calculated.")
