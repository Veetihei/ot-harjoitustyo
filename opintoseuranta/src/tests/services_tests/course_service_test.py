import unittest
from repositories.users_repository import user_repository
from entities.courses import Course
from entities.user import User
from services.course_service import (
    CourseService
)

class TestCourseService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.course_service = CourseService()
        self.user_testaaja = User("testaaja", "salasana")

    def test_course_service_test_works(self):
        self.assertEqual("Hello world!", "Hello world!")

    def test_register_works(self):
        user = self.course_service.register(self.user_testaaja.username, self.user_testaaja.password)

        self.assertEqual(user.username, self.user_testaaja.username)

    def test_login_works(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login(self.user_testaaja.username, self.user_testaaja.password)

        self.assertEqual(user.username, self.user_testaaja.username)
        self.assertEqual(user.password, self.user_testaaja.password)
    
    def test_login_wrong_username(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login("Vaara_nimi", self.user_testaaja.password)

        self.assertEqual(user, None)

    def test_login_wrong_password(self):
        user_repository.register(self.user_testaaja)
        user = self.course_service.login(self.user_testaaja.username, "vaara_salis")

        self.assertEqual(user, None)
            
