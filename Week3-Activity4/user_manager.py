from database import create_connection
import sqlite3

def add_user(f_name, l_name, birth_date):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student (student_Fname, student_Lname, b_date) VALUES (?, ?, ?)", (f_name, l_name, birth_date))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def add_lecturer(f_name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturer (lecturer_name, lecturer_email) VALUES (?, ?)", (f_name, email))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()   

def add_subjects(subject_code, subject_name, subject_unit, subject_udsc, lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (subject_code, subject_name, subject_unit, subject_udsc, lecturer_id) VALUES (?, ?, ?, ?, ?)", (subject_code, subject_name, subject_unit, subject_udsc, lecturer_id))
        conn.commit()
        print(" Subject added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()        

def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_subjects():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE student_Fname LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE student_NID = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
