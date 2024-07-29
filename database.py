import sqlite3
from course import Course

db = 'real.db'

def initialize_database():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS course (
        subject_code TEXT,
        course_code  INTEGER,
        title        TEXT,
        year         INTEGER,
        semester     TEXT,
        letter_grade TEXT,
        instructor   TEXT,
        comment      TEXT,
        PRIMARY KEY (
            subject_code,
            course_code
        )
    ) WITHOUT ROWID, STRICT;
    """

    with sqlite3.connect(f'{db}') as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='course';")
        # If the table does not exist, create it
        if not c.fetchone():
            try: 
                c.execute(sql_create_table)
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")
                return 1
        
    return 0

def get_course(subject_code, course_code):
    """Retrieve a row from the course table based on subject_code and course_code and convert it to a Course object."""
    sql_select_row = "SELECT * FROM course WHERE subject_code = ? AND course_code = ?"
    
    conn = sqlite3.connect(f'{db}')
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_row, (subject_code, course_code))
        row = cursor.fetchone()
        if row:
            return Course(*row)
        else:
            return None
    except sqlite3.Error as e:
        print(f"Error retrieving row: {e}")
    finally:
        conn.close()
    return

def get_years():
    with sqlite3.connect(f'{db}') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
    
    c.execute("SELECT DISTINCT year FROM course;")
    return c.fetchall()

def get_courses(year, semester):
    with sqlite3.connect(f'{db}') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
    
    c.execute("SELECT subject_code, course_code FROM course WHERE year = ? AND semester = ?", (year, semester))
    return c.fetchall()

def insert_course(course):
    sql_insert = """
    INSERT INTO course (subject_code, course_code, title, year, semester, letter_grade, instructor, comment)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    with sqlite3.connect(f'{db}') as conn:
        try:
            c = conn.cursor()
            c.execute(sql_insert, (
                course.subject_code,
                course.course_code,
                course.title,
                course.year,
                course.semester,
                course.letter_grade,
                course.instructor,
                course.comment
            ))
            conn.commit()
            print("Course added successfully.\n")
        except sqlite3.Error as e:
            print(f"Error adding course: {e}\n")
    return

