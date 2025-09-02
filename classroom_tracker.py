def classroom_tracker(students):
    """
    This function takes in a list of tuples where each tuple contains
    a student's name and their grade in a subject.
    The function returns a dictionary that maps each student's name to their grade.
    """

    student_grades = {}

    for student in students:
        name, grade = student
        student_grades[name] = grade

    return student_grades

if __name__ == "__main__":

    students_list = [("Alice", "A"), ("Bob", "B+"), ("Charlie", "A-")]
    print(classroom_tracker(students_list))
