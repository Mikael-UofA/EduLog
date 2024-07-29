from course import Course
import interactions
import database

def main():
    if (database.initialize_database()):
        print("Terminating operations...")
        return -1
    

    print("Welcome to EduLog!")
    choice = interactions.main_menu()

    # Main Menu
    while choice != 0:
        # View courses
        if choice == 1:
            # find the years in the db
            years = database.get_years()
            choice = interactions.year_selection(years)

            if choice != 0:
                year = years[choice - 1]
                sem = interactions.sem_selection()
                
                courses = database.get_courses(year, sem)
                # find the courses in this year and semester
                choice = interactions.course_selection(courses)
                if choice != 0:
                    # show the course
                    my_course = courses[choice - 1]
                    my_course = Course(*my_course)
                    my_course.print()

        # Add a course
        elif choice == 2:
            new_course = interactions.create_course()
            # store this new course
            print("Storing new course:")
            new_course.print()

        # Course lookup
        elif choice == 3:
            course = interactions.course_lookup()
            # return this course if it exists
            print(f"Lookup result for {course[0]} {course[1]}")

        # Exiting
        else:
            print("Terminating operations...")
            break

        choice = interactions.main_menu()

if __name__ == "__main__":
    main()