from utils.course import Course
import utils.interactions as interactions
import utils.database as database

def main():
    if database.initialize_database():
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
                year = years[choice - 1]["year"]
                sem = interactions.sem_selection()
                print("")
                
                courses = database.get_courses(year, sem)
                # find the courses in this year and semester
                choice = interactions.course_selection(courses)
                if choice != 0:
                    # show the course
                    subject_code = courses[choice - 1]["subject_code"]
                    course_code = courses[choice - 1]["course_code"]

                    my_course = database.get_course(subject_code, course_code)
                    my_course.print()
                    print("")
        # Add a course
        elif choice == 2:
            new_course = interactions.create_course()
            database.insert_course(new_course)
        # Course lookup
        elif choice == 3:
            user_input = interactions.course_lookup()
            course = database.get_course(user_input[0], user_input[1])

            if course:
                course.print()
                print()
                interactions.modify_course1(course)
            else:
                print("No such course in the database.\n")
        # Exiting
        else:
            print("Terminating operations...")
            break
        print("-------------------------------------------------------------------------------------")
        print("\nMain Menu")
        choice = interactions.main_menu()

if __name__ == "__main__":
    main()