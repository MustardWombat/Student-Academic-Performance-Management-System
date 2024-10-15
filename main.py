#######################################################################################################################
#
# Student Academic Performance Management System
#
# This Python program manages student grades by reading data from files containing names and grades for English, Math,
# and Science, then organizing the data into a master list. The program offers several options through a menu, allowing
# the user to query the data. These options include finding the highest grade for a student, calculating the average
# grade for a student or a subject, providing detailed student information, identifying students with averages above a
# certain threshold, and determining which student has the highest overall or subject-specific grade. The program
# features robust error handling for file input and invalid user entries, ensuring smooth interaction and accurate
# results.
#
#######################################################################################################################

def open_file(prompt):
    """Prompt user for a file name and handle FileNotFoundError"""
    while True:
        filename = input(prompt)
        try:
            file = open(filename, 'r')
            return file
        except FileNotFoundError:
            print("Error. File does not exist")

def read_files():
    """Read the names, English, Math, and Science grades into a master list"""
    names_file = open_file("\n:~Enter a student names file ~:")
    names = [line.strip() for line in names_file.readlines()]
    names_file.close()

    # Read English grades
    english_file = open_file("\n:~Enter a English grade score file ~:")
    english_grades = [list(map(lambda x: int(x) if x else 0, line.strip().split(','))) for line in english_file]
    english_file.close()

    # Read Math grades
    math_file = open_file("\n:~Enter a Math grade score file ~:")
    math_grades = [list(map(lambda x: int(x) if x else 0, line.strip().split(','))) for line in math_file]
    math_file.close()

    # Read Science grades
    science_file = open_file("\n:~Enter a Science grade score file ~:")
    science_grades = [list(map(lambda x: int(x) if x else 0, line.strip().split(','))) for line in science_file]
    science_file.close()

    master_list = [[names[i], english_grades[i], math_grades[i], science_grades[i]] for i in range(len(names))]
    return master_list

def display_menu():
    """Display the menu options through a variable and string to be called after"""
    menu = """
        Menu : 
            1: The maximum grade a student received in a single subject
            2: The average subject grade a student received
            3: Individual information
            4: The average grade of a subject over all students
            5: The number of students with an average grade exceeding given threshold X
            6: The name of student having the highest average grade
            7: The name of student having the highest grade of given subject name
                Enter any other key(s) to exit
    """
    print(menu)

def max_grade(master_list):
    """Handle option 1: Find max grade for a student"""
    while True:
        name = input(":~Enter a person name ~:")
        student = next((student for student in master_list if student[0].lower() == name.lower()), None)
        if student:
            english_total = sum(student[1])
            math_total = sum(student[2])
            science_total = sum(student[3])

            max_score = max(english_total, math_total, science_total)
            subjects = []

            if english_total == max_score:
                subjects.append('English')
            if math_total == max_score:
                subjects.append('Math')
            if science_total == max_score:
                subjects.append('Science')

            print(f"--------------")
            print(f"Highest grade score: {max_score}")
            print(f"Subject name: {' '.join(subjects)}")
            break
        else:
            print("Invalid name or does not exist")

def average_grade_student(master_list):
    """Handle option 2: Average grade for a student"""
    while True:
        name = input(":~Enter a person name ~:")
        student = next((student for student in master_list if student[0].lower() == name.lower()), None)
        if student:
            english_total = sum(student[1])
            math_total = sum(student[2])
            science_total = sum(student[3])
            average_grade = (english_total + math_total + science_total) / 3
            print(f"--------------")
            print(f"Average grade score: {average_grade:.1f}")
            break
        else:
            print("Invalid name or does not exist")

def student_info(master_list):
    """Handle option 3: Print detailed info for a student"""
    while True:
        name = input(":~Enter a person name ~:")
        student = next((student for student in master_list if student[0].lower() == name.lower()), None)
        if student:
            print(f"--------------")
            print(f"English: {sum(student[1])}")
            print(f"Speaking: {student[1][0]} Writing: {student[1][1]} Reading: "
            f"{student[1][2]} Listening: {student[1][3]}")
            print(f"--------------")
            print(f"Math: {sum(student[2])}")
            print(f"Geometry: {student[2][0]} Arithmetic: {student[2][1]} Logic: {student[2][2]}")
            print(f"--------------")
            print(f"Science: {sum(student[3])}")
            print(f"Biology: {student[3][0]} Chemistry: {student[3][1]} Physics: {student[3][2]}")
            break
        else:
            print("Invalid name or does not exist")

def average_grade_subject(master_list):
    """Handle option 4: Average grade for a subject over all students"""
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    while True:
        subject = input(":~Enter a subject name ~:")
        total_grades = 0
        num_students = len(master_list)

        if subject == 'English':
            for student in master_list:
                total_grades += sum(student[1])
            avg_grade = total_grades / num_students
            print(f"--------------")
            print(f"Average grade score: {avg_grade:.1f}")
            break
        elif subject == 'Math':
            for student in master_list:
                total_grades += sum(student[2])
            avg_grade = total_grades / num_students
            print(f"--------------")
            print(f"Average grade score: {avg_grade:.1f}")
            break
        elif subject == 'Science':
            for student in master_list:
                total_grades += sum(student[3])
            avg_grade = total_grades / num_students
            print(f"--------------")
            print(f"Average grade score: {avg_grade:.1f}")
            break
        else:
            print("Invalid name or does not exist")

def students_above_threshold(master_list):
    """Handle option 5: Number of students above a certain grade threshold"""
    while True:
        threshold = int(input(":~Enter a grade threshold ~:"))
        if 0 <= threshold <= 100:
            break
        else:
            print("Invalid grade score")
    count = 0

    for student in master_list:
        english_total = sum(student[1])
        math_total = sum(student[2])
        science_total = sum(student[3])
        average_grade = (english_total + math_total + science_total) / 3

        if average_grade > threshold:
            count += 1

    print(f"--------------")
    print(f"The number of students having average grade score higher than {threshold} is: {count}")

def highest_average_student(master_list):
    """Handle option 6: Find student with the highest average grade"""
    highest_avg = 0
    top_student = None

    for student in master_list:
        english_total = sum(student[1])
        math_total = sum(student[2])
        science_total = sum(student[3])
        average_grade = (english_total + math_total + science_total) / 3

        if average_grade >= highest_avg:
            highest_avg = average_grade
            top_student = student

    print(f"--------------")
    print(f"Name: {top_student[0]}")
    print(f"Average grade score: {highest_avg:.1f}")

def highest_subject_grade_student(master_list):
    """Handle option 7: Find student with highest grade in a subject"""
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    while True:
        subject = input(":~Enter a subject name ~:")
        highest_score = 0
        top_student = None

        if subject == 'English':
            for student in master_list:
                total = sum(student[1])
                if total >= highest_score:
                    highest_score = total
                    top_student = student

            break
        elif subject == 'Math':
            for student in master_list:
                total = sum(student[2])
                if total > highest_score:
                    highest_score = total
                    top_student = student

            break
        elif subject == 'Science':
            for student in master_list:
                total = sum(student[3])
                if total > highest_score:
                    highest_score = total
                    top_student = student

            break
        else:
            print("Invalid name or does not exist")

    print(f"--------------")
    print(f"Name: {top_student[0]}")
    print(f"Grade score: {highest_score}")
    return

def main():
    """Main driver function"""
    master_list = read_files()

    while True:
        display_menu()
        choice = input(":~Input a choice ~:")
        if choice == '1':
            max_grade(master_list)
        elif choice == '2':
            average_grade_student(master_list)
        elif choice == '3':
            student_info(master_list)
        elif choice == '4':
            average_grade_subject(master_list)
        elif choice == '5':
            students_above_threshold(master_list)
        elif choice == '6':
            highest_average_student(master_list)
        elif choice == '7':
            highest_subject_grade_student(master_list)
        else:
            print("Thank you")
            break

if __name__ == '__main__':
    main()
