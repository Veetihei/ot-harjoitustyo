import unittest
from repositories.users_repository import user_repository
from repositories.courses_repository import course_repository
from entities.courses import Course
from entities.user import User
from services.course_service import (
    CourseService
)


class TestCourseService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        course_repository.delete_all()
        self.course_service = CourseService()
        self.user_testaaja = User("testaaja", "salasana")
        self.course_ohpe = Course(self.user_testaaja.username, "OhPe", 5, 5)

    def test_course_service_test_works(self):
        self.assertEqual("Hello world!", "Hello world!")

    def test_register_works(self):
        user = self.course_service.register(
            self.user_testaaja.username, self.user_testaaja.password)

        self.assertEqual(user.username, self.user_testaaja.username)

    def test_login_works(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login(
            self.user_testaaja.username, self.user_testaaja.password)

        self.assertEqual(user.username, self.user_testaaja.username)
        self.assertEqual(user.password, self.user_testaaja.password)

    def test_login_wrong_username(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login(
            "Vaara_nimi", self.user_testaaja.password)

        self.assertEqual(user, None)

    def test_login_wrong_password(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login(
            self.user_testaaja.username, "vaara_salis")

        self.assertEqual(user, None)

    def test_add_new_course(self):
        self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

    def test_add_course_wrong_grade(self):
        self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            10
        )
        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)

    def test_add_course_short_name(self):
        self.course_service.add_new_course(
            self.user_testaaja.username,
            "AI",
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )
        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)

    def test_add_course_negative_weight(self):
        self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            -10,
            self.course_ohpe.grade
        )
        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)

    def test_get_courses_by_username(self):
        self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )

        courses = self.course_service.get_courses_by_username(self.user_testaaja.username)
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

    def test_get_current_user(self):
        self.course_service.register(
            self.user_testaaja.username,
            self.user_testaaja.password
        )
       
        self.course_service.login(
            self.user_testaaja.username,
            self.user_testaaja.password
        )

        user = self.course_service.get_current_user()

        self.assertEqual(user.username, self.user_testaaja.username)