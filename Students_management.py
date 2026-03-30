from student_management_functions import main_options, register_student, consult_list, search_student, update_student, delete_student

n = 70
Students = []

option = main_options()

while option != 6:
    if option == 1:
        register_student(Students)

    elif option == 2:
        consult_list(Students)

    elif option == 3:
        try:
            Student_ID = int(input("Student ID: "))
            if Student_ID < 0:
                print("ERROR! The ID can't be less than 0")
                continue

            Student = search_student(Students, Student_ID)

            if Student:
                print("-"*n)
                print(f"ID: {Student['Unique_identifier']}\nName: {Student['Student_name']}\nAge: {Student['Student_age']}\nProgram: {Student['Student_program']}\nState: {Student['Student_state']}")
                print("-"*n)
                
            else:
                print("The student wasn't found")
            input('\nPress ENTER to return to the main menu...')

        except ValueError:
            print("ERROR! The ID must be a number")

    elif option == 4:
        ID = input("Student ID: ")
        update_student(Students, ID)

    elif option == 5:
        ID = input("Student ID: ")
        delete_student(Students, ID)
    else:
        print("\nERROR! That option isn't exist. Try again..\n")
        input('\nPress ENTER to return to the main menu...')

    option = main_options()

print("="*n)
print("\nThanks for use the program, See you later!".center(n))
print("="*n)