class Student:
    def __init__(self, name):
        self.name = name

    def get_mean_grade(self, courses):
        points = 0
        grades = 0
        for course in courses:
            points += course.points
            grades += course.points * course.grade
        return grades / points

class Course:
    def __init__(self, student_name, name, points, grade):
        self.student_name = student_name
        self.name = name
        self.points = points
        self.grade = grade


    
