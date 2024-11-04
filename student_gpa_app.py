# Name: Pascal (Student)
# File Name: student_gpa_app.py
# Description: This app accepts student names and GPAs and determines if they qualify for the Dean's List or the Honor Roll.

# Start the app loop
while True:
    # Ask for the student's last name
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
    # Check if the user wants to quit
    if last_name.upper() == 'ZZZ':
        break

    # Ask for the student's first name
    first_name = input("Enter the student's first name: ")
    
    # Ask for the student's GPA
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid input. Please enter a numeric GPA.")
        continue

    # Check if the student qualifies for the Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Check if the student qualifies for the Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or the Honor Roll.")

print("Goodbye!")