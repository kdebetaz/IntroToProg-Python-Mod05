# ---------------------------------------- #
# Title: Assignment05
# Description: This assignment demonstrates data processing with dictionaries and exception handling.
# Change Log: Katie Debetaz, 11/8/2024, Created Script
# ---------------------------------------- #

import json

# Define Constants
MENU = """ 
---- Course Registration Program ----
Select from the following menu:  
1. Register a student for a course
2. Show current data  
3. Save data to a file
4. Exit the program
----------------------------------------- 
"""
FILE_NAME = "Enrollments.json"

# Define Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
json_data:str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

try:
    # Loading data from json
    file = open(FILE_NAME, "r")
    student_data = json.load(file)

    # Assigning variables to existing data
    for student in student_data:
        student_first_name = {student['FirstName']}
        student_last_name = {student['LastName']}
        course_name = {student['CourseName']}
        students.append(student)

    file.close()
except Exception as e:
    print('Unknown exception',e)
finally:
    if file and not file.closed:
        file.close()

# Processing options for MENU
while True:
    print(MENU)
    menu_choice = input("Please enter your choice: ")

    # Input for student name and course
    if menu_choice == "1":
        try:
            student_first_name = input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must be alphabetic, please enter student's first name.")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be alphabetic, please enter student's last name.")
            course_name = input("Enter the name of the course: ")
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)

    # Print saved data as a formatted string
    elif menu_choice == "2":
        print("The current data is:")
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")

    # Export data to json
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
            print('The following was saved to json:')
            for student in students:
                print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")
        except Exception as e:
            print('Error exporting data to json')
        finally:
            if file and not file.closed:
                file.close()
    # End program
    elif menu_choice == "4":
        print("Program ended")
        break

    # Validate input
    else:
        print("Choice invalid, please try again.")