import unittest
from courses import Student, Course

class TestCourses(unittest.TestCase):
    def setUp(self):
        print("Testausta")
    
    def test_mean_grade(self):
        Kalle = Student("Kalle")
        kalle_courses = []
        kalle_courses.append(Course("Kalle", "OhPe", 5, 5))
        kalle_courses.append(Course("Kalle", "OhJa", 5, 4))
        self.assertEqual(Kalle.get_mean_grade(kalle_courses), 4.5)



