class Course:
    def __init__(self, subject_code, course_code, course_title, year, semester, letter_grade, instructor, comment):
        self.subject_code = subject_code
        self.course_code = course_code
        self.course_title = course_title
        self.year = year
        self.semester = semester
        self.letter_grade = letter_grade
        self.instructor = instructor
        self.comment = comment

    def print(self):
        print(f"{self.subject_code} {self.course_code}: {self.course_title}\n"
              f"{self.semester} Semester\n"
              f"Taught by {self.instructor}, Grade: {self.letter_grade}\n Notes: {self.comment}")