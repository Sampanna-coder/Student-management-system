# ======================================================#
#              STUDENT MANAGEMENT SYSTEM
# ======================================================#

students = []  # List to store student records

# Function to add a student


def add_student():
    print("\n==== ADD NEW STUDENT ====")
    # input() collects information from the keyboard.
    student_id = input("Enter the student ID: ")
    name = input("Enter the Student Name: ")
    age = input("Enter the Student Age: ")
    course = input("Enter the Student Course: ")

    # Dictionary to store student details
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    # append() adds the new student dictionary to our students lists.
    students.append(student)

    print("\nStudent added successfully!")

    # Function to display all students

def view_students():

        print("\n=====ALL STUDENTS=====")
        # len() counts how many students are in the lists. If the length is zero
        # there is no students on record.
        if len(students) == 0:
            print("No students record found.")
            return  # return stops this function here.
            # A for loop visits each student's information in the list.
        for student in students:
            print("------------------------------")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print("------------------------------")

     # function to search for a student.

def search_student():
        print("\n==========SEARCH STUDENT==========")
        search_id = input("Enter the student ID to search: ")
        for student in students:                              # Check every student in students list.
            if student['id'] == search_id:
                print("------------------------------")

                                                                #Displlaying matching student details.
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Course: {student['course']}")
                print("------------------------------")         #Stop searching after finding.
                return
        print("Student not found.")

        # function to delete a student by their ID.

def delete_student():
            print("\n =============DELETE STUDENT=============")
            delete_id = input("Enter Student ID: ")

            for student in students:

                if student['id'] == delete_id:
                    students.remove(student)                        #Removes the student from the list.
                    print("Student deleted successfully!")
                    return

                print("Student not found.")

        # Main Application

while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add student")
            print("2. View students")
            print("3. Search student")
            print("4. Delete student")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
