from course import Course

def check_input_validity(answer, range_value):
    if not answer:
        return -1

    try:
        num = int(answer)
    except ValueError:
        return -1

    if 0 <= num <= range_value:
        return num
    return -1

def main_menu():
    print("1. View your courses")
    print("2. Add a course")
    print("3. Course Lookup")
    print("0. Exit")
    print("Please select one of these options: ", end="")

    while True:
        answer = input()
        value = check_input_validity(answer, 3)
        if value != -1:
            print("")
            return value
        print("Please enter a valid option: ", end="")

def course_lookup():
    print("Please enter the course identifier (e.g., MATH 217, ENGL 102, ...): ", end="")

    while True:
        user_input = input().strip()
        parts = user_input.split()
        
        # Check if there are at least two parts and the last part is an integer
        if len(parts) >= 2 and parts[-1].isdigit():
            subject_code = ' '.join(parts[:-1])
            course_code = parts[-1]
            print("")  # For a new line
            return [subject_code, course_code]
        else:
            print("Invalid input. Please enter the course identifier in the format 'SUBJECT_CODE COURSE_CODE' (e.g., MATH 217).", end=" ")

def year_selection(year_list):
    if not year_list:
        print("No years available.")

    pos = 0
    for position, row in enumerate(year_list, 1):
        print(f"{position}. {row["year"]}")
        pos = position

    print("0. Back")
    print("Please select one of these options: ", end="")

    while True:
        answer = input()
        value = check_input_validity(answer, pos)
        if value != -1:
            print("")
            return value
        print("Please enter a valid option: ", end="")

def sem_selection():
    valid_semesters = {"Fall", "Winter", "Spring", "Summer"}
    print("Please enter the semester (Fall, Winter, Spring, or Summer): ", end="")
    
    while True:
        semester = input()
        if semester in valid_semesters:
            return semester
        else:
            print("Invalid semester. Please enter the semester (Fall, Winter, Spring, or Summer): ", end="")

def course_selection(course_name_list):
    if not course_name_list:
        print("No courses available.")
        return 0

    for position, row in enumerate(course_name_list, 1):
        print(f"{position}. {row["subject_code"]} {row["course_code"]}")

    print("0. Back")

    print("Please select one of these options: ", end="")
    while True:
        
        answer = input()
        value = check_input_validity(answer, position)
        if value != -1:
            print("")
            return value
        print("Please enter a valid option: ", end="")

def create_course():

    while True:
        try:
            year = int(input("Please enter a year (e.g., 2020, 2021, 2023, ...): ").strip())
            if 1970 < year < 2048:
                break
            else:
                print("Invalid year. Please enter a valid year.")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

    semester = sem_selection()

    subject_code = input("Please enter the subject code (MATH, ENGL, ...): ")
    
    while True:
        try:
            course_code = int(input("Please enter the course code (240, 102, ...): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid course code: ", end="")

    course_title = input("Please enter the course title: ")
    letter_grade = input("Please enter your letter grade for this course (B, C, B+, ...): ")
    instructor = input("Please enter the name of your instructor: ")
    comment = input("Please enter any comment you have for this course: ")

    print("")
    return Course(subject_code, course_code, course_title, year, semester, letter_grade, instructor, comment)