import unittest
from repositories.courses_repository import course_repository
from entities.courses import Course
from entities.user import User


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()
        self.user_testaaja = User("testaaja", "salis")
        self.course_ohpe = Course(1, self.user_testaaja.username, "OhPe", 5, 5)
        self.course_tito = Course(2, self.user_testaaja.username, "TiTo", 5, 3)

    def test_add_new_course(self):
        course_repository.add_new_course(
            self.course_ohpe.username, 
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )
        courses = course_repository.find_all()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

    def test_find_courses_by_username(self):
        course_repository.add_new_course(
            self.course_ohpe.username, 
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )
        course_repository.add_new_course(
            self.course_tito.username, 
            self.course_tito.name,
            self.course_tito.weight,
            self.course_tito.grade
        )

        courses = course_repository.find_courses_by_username(
            self.user_testaaja.username)

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].grade, 5)
        self.assertEqual(courses[1].name, "TiTo")
        self.assertEqual(courses[1].weight, 5)

    def test_delete_course_by_id(self):
        course_repository.add_new_course(
            self.course_ohpe.username, 
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 1)

        course_id = courses[0].id

        course_repository.delete_course(course_id)

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)


