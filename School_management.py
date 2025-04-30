import mysql.connector
# Connecting to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your pass',
    database='management_system'
)
cursor = conn.cursor()
# Creating tables if not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        grade INT,
        sec VARCHAR(10),
        percentage FLOAT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        subject VARCHAR(50),
        salary FLOAT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        installment INT,
        amount FLOAT
    )
''')
# Defining a function to add a student
def add_student():
    try:
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        sec = input("Enter student section: ")
        percentage = float(input("Enter student percentage: "))
        cursor.execute("INSERT INTO students (name, grade, sec, percentage) VALUES (%s, %s, %s, %s)",
                       (name, grade, sec, percentage))
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to get student details
def get_student():
    try:
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        sec = input("Enter student section: ")
        cursor.execute("SELECT * FROM students WHERE name = %s AND grade = %s AND sec = %s",
                       (name, grade, sec))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No student found.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to delete a student
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to increase teacher's salary
def increase_salary():
    try:
        teacher_id = int(input("Enter teacher ID: "))
        increase_amount = float(input("Enter salary increase amount: "))
        cursor.execute("UPDATE teachers SET salary = salary + %s WHERE id = %s", (increase_amount, teacher_id))
        conn.commit()
        print("Salary increased successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to update fees
def update_fees():
    try:
        installment = int(input("Enter installment number (1, 2, 3, 4): "))
        new_amount = float(input("Enter new fee amount: "))
        cursor.execute("UPDATE fees SET amount = %s WHERE installment = %s", (new_amount, installment))
        conn.commit()
        print("Fees updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to update a student's details
def update_student():
    try:
        student_id = int(input("Enter the student ID to update: "))
        print("1. Update Name")
        print("2. Update Grade")
        print("3. Update Section")
        print("4. Update Percentage")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter new name: ")
            cursor.execute("UPDATE students SET name = %s WHERE id = %s", (new_name, student_id))
        elif choice == '2':
            new_grade = int(input("Enter new grade: "))
            cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id))
        elif choice == '3':
            new_section = input("Enter new section: ")
            cursor.execute("UPDATE students SET sec = %s WHERE id = %s", (new_section, student_id))
        elif choice == '4':
            new_percentage = float(input("Enter new percentage: "))
            cursor.execute("UPDATE students SET percentage = %s WHERE id = %s", (new_percentage, student_id))
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Student information updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to list all students
def list_students():
    try:
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No teachers found.")
    except Exception as e:
        print(f"Error: {e}")
# Defining a function to list all teachers
def list_teachers():
    try:
        cursor.execute("SELECT * FROM teachers")
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No teachers found.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to update a teacher's details
def update_teacher():
    try:
        teacher_id = int(input("Enter the teacher ID to update: "))
        print("1. Update Name")
        print("2. Update Subject")
        print("3. Update Salary")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter new name: ")
            cursor.execute("UPDATE teachers SET name = %s WHERE id = %s", (new_name, teacher_id))
        elif choice == '2':
            new_subject = input("Enter new subject: ")
            cursor.execute("UPDATE teachers SET subject = %s WHERE id = %s", (new_subject, teacher_id))
        elif choice == '3':
            new_salary = float(input("Enter new salary: "))
            cursor.execute("UPDATE teachers SET salary = %s WHERE id = %s", (new_salary, teacher_id))
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Teacher information updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to count records
def count_records():
    try:
        cursor.execute("SELECT COUNT(*) FROM students")
        student_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM teachers")
        teacher_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM fees")
        fee_count = cursor.fetchone()[0]

        print(f"Total Students: {student_count}")
        print(f"Total Teachers: {teacher_count}")
        print(f"Total Fee Installments: {fee_count}")
    except Exception as e:
        print(f"Error: {e}")

# Defining a function to generate a summary report
def generate_report():
    print("\n--- Summary Report ---")
    count_records()
    print("\nStudents List:")
    list_students()
    print("\nTeachers List:")
    list_teachers()
    print("\nFee Installments:")
    view_fees()

# Function to search students by grade and section
def search_students():
    try:
        grade = int(input("Enter grade: "))
        section = input("Enter section: ")
        cursor.execute("SELECT * FROM students WHERE grade = %s AND sec = %s", (grade, section))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No students found.")
    except Exception as e:
        print(f"Error: {e}")

# Main menu
try:
    while True:
        print("\nSchool Management System")
        print("1. Students Management")
        print("2. Teacher Management")
        print("3. Fee Department")
        print("4. Summary Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nStudents Management")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Fetch Student")
            print("4. List All Students")
            print("5. Update Student Details")
            print("6. Search Students by Grade and Section")
            print("7. Back to Main Menu")

            student_choice = input("Enter your choice: ")

            if student_choice == '1':
                add_student()
            elif student_choice == '2':
                delete_student()
            elif student_choice == '3':
                get_student()
            elif student_choice == '4':
                list_students()
            elif student_choice == '5':
                update_student()
            elif student_choice == '6':
                search_students()
            elif student_choice == '7':
                pass
            else:
                print("Invalid choice. Please enter a valid option.")

        elif choice == '2':
            print("\nTeacher Management")
            print("1. Add Teacher")
            print("2. Delete Teacher")
            print("3. List All Teachers")
            print("4. Update Teacher Details")
            print("5. Search Teacher")
            print("6. Back to Main Menu")

            teacher_choice = input("Enter your choice: ")

            if teacher_choice == '1':
                add_teacher()
            elif teacher_choice == '2':
                delete_teacher()
            elif teacher_choice == '3':
                list_teachers()
            elif teacher_choice == '4':
                update_teacher()
            elif teacher_choice == '5':
                search_teacher()
            elif teacher_choice == '6':
                pass
            else:
                print("Invalid choice. Please enter a valid option.")

        elif choice == '3':
            print("\nFee Department")
            print("1. Add Fee Installment")
            print("2. Delete Fee Installment")
            print("3. View All Fee Installments")
            print("4. Back to Main Menu")

            fee_choice = input("Enter your choice: ")

            if fee_choice == '1':
                add_fee()
            elif fee_choice == '2':
                delete_fee()
            elif fee_choice == '3':
                view_fees()
            elif fee_choice == '4':
                pass
            else:
                print("Invalid choice. Please enter a valid option.")

        elif choice == '4':
            generate_report()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a valid option.")
finally:
    cursor.close()
    conn.close()
