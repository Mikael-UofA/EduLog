from utils.course import Course

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
        print("No years available.\n")
        return 0
    print("Select a year")

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

def enter_semester():
    valid_semesters = {"Fall", "Winter", "Spring", "Summer"}
    print("Please enter the semester (Fall, Winter, Spring, or Summer): ", end="")
    
    while True:
        semester = input()
        if semester in valid_semesters:
            return semester
        else:
            print("Invalid semester. Please enter the semester (Fall, Winter, Spring, or Summer): ", end="")

def enter_year():
    while True:
        try:
            year = int(input("Please enter a year (e.g., 2020, 2021, 2023, ...): ").strip())
            if 1970 < year < 2048:
                return year
            else:
                print("Invalid year. Please enter a valid year.")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

def enter_course_code():
     while True:
        try:
            course_code = int(input("Please enter the course code (240, 102, ...): "))
            return course_code
        except ValueError:
            print("Invalid input. Please enter a valid course code: ", end="")

def enter_string(num: int):
    while True:
         answer = input("Please enter a new value: ")
         if num > 5 or len(answer) > 1:
             return answer
         else:
             print("This information cannot be empty")

def course_selection(course_name_list):
    if not course_name_list:
        print("No courses available.\n")
        return 0
    print("Select a course")

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

    year = enter_year()

    semester = enter_semester()

    subject_code = input("Please enter the subject code (MATH, ENGL, ...): ")
    
    course_code = enter_course_code()

    course_title = input("Please enter the course title: ")
    letter_grade = input("Please enter your letter grade for this course (B, C, B+, ...): ")
    instructor = input("Please enter the name of your instructor: ")
    comment = input("Please enter any comment you have for this course: ")

    print("")
    return Course(subject_code, course_code, course_title, year, semester, letter_grade, instructor, comment)

def modify_course1():
    while (True):
        answer = input("Do you wish to modify this course's info (Y/N)?: ")
        
        if answer.upper() == "Y":
            return True
        if answer.upper() == "N":
            return False

def modify_course2(course: Course):
    need_to_delete = False
    while True:
        print("Select the information you wish to modify: ")
        print("1. Subject Code      2. Course Code      3. Course Title")
        print("4. Year              5. Semester         6. Instructor")
        print("7. Final Grade       8. Comment          0. Done/Cancel")

        answer = input("> ")
        while True:
            if (check_input_validity(answer, 8) != - 1):
                break
            answer = input("> ")
        
        answer = int(answer)
        if not answer:
            return answer 
        elif answer in (1, 2):
            need_to_delete = True
        
        course = modify_course3(course, answer)

def modify_course3(course: Course, option: int):
    match option:
        case 1:
            print("Selected to motify 'subject code':")
            print(f"Previous value: {course.subject_code}")
            answer = enter_string(option)
            course.subject_code = answer
        case 2:
            print("Selected to motify 'course code':")
            print(f"Previous value: {course.course_code}")
            answer = enter_course_code()
            course.course_code = answer
        case 3:
            print("Selected to motify 'course title':")
            print(f"Previous value: {course.title}")
            answer = enter_string(option)
            course.title = answer
        case 4:
            print("Selected to motify 'year':")
            print(f"Previous value: {course.year}")
            answer = enter_year()
            course.year = answer
        case 5:
            print("Selected to motify 'semester':")
            print(f"Previous value: {course.semester}")
            answer = enter_semester()
            course.semester = answer
        case 6:
            print("Selected to motify 'instructor':")
            print(f"Previous value: {course.instructor}")
            answer = enter_string(option)
            course.instructor = answer
        case 7:
            print("Selected to motify 'final grade':")
            print(f"Previous value: {course.letter_grade}")
            answer = enter_string(option)
            course.letter_grade = answer
        case _:
            print("Selected to motify 'comment':")
            print(f"Previous value: {course.comment}")
            answer = enter_string(option)
            course.comment = answer
        
    return course
        

            


        
    