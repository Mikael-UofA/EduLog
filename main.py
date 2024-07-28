from course import Course
from interactions import main_menu, year_selection, sem_selection, course_selection, create_course, course_lookup;
def main():
    choice = main_menu()

    while choice != 0:
        if choice == 1:
            # find the years in the db
            choice = year_selection(["I", "II", "III", "IV"])

            if choice != 0:
                sem = sem_selection()
                # find the courses in this year and semester
                choice = course_selection(["Course1", "Course2", "Course3"])

                if choice != 0:
                    # show the course
                    print(f"Showing details for {['Course1', 'Course2', 'Course3'][choice-1]}")
        elif choice == 2:
            new_course = create_course()
            # store this new course
            print("Storing new course:")
            new_course.print()
        elif choice == 3:
            course = course_lookup()
            # return this course if it exists
            print(f"Lookup result for {course[0]} {course[1]}")
        else:
            print("Terminating operations...")
            break

        choice = main_menu()

if __name__ == "__main__":
    main()