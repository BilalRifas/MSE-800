import sqlite3

conn = sqlite3.connect('student_manager.db')

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Teacher (
    teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT
)

CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
)
''')

conn.commit()

# Close the connection when done
conn.close()

