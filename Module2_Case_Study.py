
# Name: Tyree Callahan
# File Name: Module2_Case_Study.py
# Description: This program checks student GPAs to see if they
# qualify for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter student's last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")
    else:
        print(first_name, last_name, "did not qualify for either list.")

    print()

print("Program ended.")

