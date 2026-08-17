from database import create_table
from user_manager import add_lecturer, add_subjects, add_user, view_lecturers, view_subjects, view_users, search_user, delete_user

def menu():
    print("\n==== User Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by First Name")
    print("4. Delete Student by ID")
    print("5. Add Lecturer")
    print("6. View All Lecturers")
    print("7. Add Subject")
    print("8. View All Subjects")
    print("9. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            add_user(name, last_name, birth_date)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter first name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter Student NID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter lecturer name: ")
            email = input("Enter lecturer email: ")
            add_lecturer(name, email)
        elif choice == '6':
            lecturers = view_lecturers()
            for lecturer in lecturers:
                print(lecturer)
        elif choice == '7':
                    subject_code = input("Enter subject code: ")
                    subject_name = input("Enter subject name: ")
                    subject_unit = input("Enter subject unit: ")
                    subject_udsc = input("Enter subject description: ")
                    lecturer_id = int(input("Enter lecturer ID: "))
                    add_subjects(subject_code, subject_name, subject_unit, subject_udsc, lecturer_id)
        elif choice == '8':
                    subjects = view_subjects()
                    for subject in subjects:
                        print(subject)        
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
