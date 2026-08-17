import sqlite3

def create_connection():
    conn = sqlite3.connect("university.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Student (
        student_NID INTEGER PRIMARY KEY,
        student_Fname TEXT,
        student_Lname TEXT,
        b_date DATE
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Lecturer (
        lecturer_id INTEGER PRIMARY KEY,
        lecturer_name TEXT,
        lecturer_email TEXT UNIQUE
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollment (
        student_code INTEGER,
        lecturer_id INTEGER,
        date_of_enrollment DATE,
        course_name TEXT,
        E_CC INTEGER PRIMARY KEY
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Lecture (
        lecture_id INTEGER PRIMARY KEY,
        L_CC INTEGER,
        subject TEXT,
        time TEXT,
        date DATE,
        lecturer_id INTEGER,
        lecture_name TEXT
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
        subject_code INTEGER PRIMARY KEY,
        subject_name TEXT,
        subject_unit INTEGER,
        subject_udsc TEXT,
        lecturer_id INTEGER,
        FOREIGN KEY (lecturer_id) REFERENCES Lecturer (lecturer_id)
    )''')
    
    conn.commit()
    conn.close()
