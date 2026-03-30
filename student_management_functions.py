n = 70

def main_options():
    print('='*n)
    print('STUDENTS MANAGEMENT'.center(n))
    print('='*n)
    print('1. Register new students.')
    print('2. Consult the student list.')
    print('3. Search a student')
    print('4. Update student data.')
    print('5. Delete a student.')
    print('6. Leave')
    print('='*n)

    try:
        option = int(input("Choose an option (1-6): "))
        return option
    except:
        return 0

def register_student(Students):
    choice = 'yes'

    while choice == 'yes':
        print('='*n)
        try:
            Student_ID = int(input("Student ID: "))
            if Student_ID < 0:
                print("ERROR! The student ID can not be negative.")
                continue

            name = input("Student name: ").lower()

            age = int(input("Student age: "))
            if age < 0:
                print("ERROR! The student age can not be negative.")
                continue

            program = input("Student program: ").lower()

            
            state = input("State (active/inactive): ").strip().lower()

            if state == "active" or state == "inactive":
                student = {
                                "Unique_identifier" : Student_ID,
                                "Student_name" : name,
                                "Student_age" : age,
                                "Student_program" : program,
                                "Student_state" : state
                }

                Students.append(student)

                print('='*n)
                print(f"The student '{name}' was succesfully added!")
            
            else:
                print("ERROR! You can only write active or inactive.")
                continue

            choice = input('\nDo you want to regist another student?(Yes/No): ').lower()

        except ValueError:
            print("ERROR! Only numbers are accept.")
        print('='*n)

def consult_list(Students):
    print('='*n)
    print('STUDENTS LIST'.center(n))
    print('='*n)

    if not Students:
        print("The list is empty. You need add new students.")
        input('\nPress ENTER to return to the main menu...')
        return
##
    else:
        for Student in Students:
            print(f"ID: {Student['Unique_identifier']}\nName: {Student['Student_name']}\nAge: {Student['Student_age']}\nProgram: {Student['Student_program']}\nState: {Student['Student_state']}")
            print('-'*n)

    input('\nPress ENTER to return to the main menu...')
    

def search_student(Students, Student_ID):
    for Student in Students:
        if Student["Unique_identifier"] == int(Student_ID):
            return Student
    return None

def update_student(Students, Student_ID):
    Student = search_student(Students, Student_ID)

    if not Student:
        print(f"The student with ID '{Student_ID}' was not found in the list.")
        return

    else:
        new_ID = (input("New ID (ENTER to skip): "))
        new_Name = input("New name (ENTER to skip): ")
        new_Age = (input("New age (ENTER to skip): "))
        new_Program = input("New program (ENTER to skip): ")
        new_State = input("New state (ENTER to skip): ")

        if new_ID:
            Student["Unique_identifier"] = int(new_ID)
        if new_Name:
            Student["Student_name"] = new_Name
        if new_Age:
            Student["Student_age"] = int(new_Age)
        if new_Program:
            Student["Student_program"] = new_Program
        if new_State:
            Student["Student_state"] = new_State

        print("Student data successfully updated.")

def delete_student(Students, Student_ID):
    Student = search_student(Students, Student_ID)

    if not Student:
        print(f"The student with ID '{Student_ID}' was not found on the list.")
        return

    Students.remove(Student)

    print(f"The student with ID '{Student_ID}' has been removed from the list.")
    input('\nPress ENTER to return to the main menu...')
    print("-"*n)