import unittest
from repositories.courses_repository import course_repository
from entities.courses import Course
from entities.user import User

class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()
        self.user_testaaja = User("testaaja", "salis")
        self.course_ohpe = Course(self.user_testaaja.username, "OhPe", 5, 5)
        self.course_tito = Course(self.user_testaaja.username, "TiTo", 5, 3)

    def test_add_new_course(self):
        course_repository.add_new_course(self.course_ohpe)
        courses = course_repository.find_all()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

    def test_find_courses_by_username(self):
        course_repository.add_new_course(self.course_ohpe)
        course_repository.add_new_course(self.course_tito)

        courses = course_repository.find_courses_by_username(self.user_testaaja.username)

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].grade, 5)
        self.assertEqual(courses[1].name, "TiTo")
        self.assertEqual(courses[1].weight, 5)

    #     user_repository.register(self.user_testaaja)
    #     users = user_repository.find_all()

    #     self.assertEqual(len(users), 1)
    #     self.assertEqual(users[0].username, self.user_testaaja.username)

    # def test_find_all_2_new_users(self):
    #     user_repository.register(self.user_kayttaja)
    #     user_repository.register(self.user_testaaja)

    #     users = user_repository.find_all()

    #     self.assertEqual(len(users), 2)
    #     self.assertEqual(users[0].username, self.user_kayttaja.username)
    #     self.assertEqual(users[1].username, self.user_testaaja.username)
    #     self.assertEqual(users[0].password, self.user_kayttaja.password)

    # def test_find_by_username(self):
    #     user_repository.register(self.user_kayttaja)
    #     user_repository.register(self.user_testaaja)

    #     user = user_repository.find_by_username(self.user_testaaja.username)

    #     self.assertEqual(user.username, self.user_testaaja.username)
    #     self.assertEqual(user.password, self.user_testaaja.password)

    # def test_delete_all(self):
    #     user_repository.register(self.user_kayttaja)
    #     user_repository.register(self.user_testaaja)

    #     user_repository.delete_all()

    #     users = user_repository.find_all()

    #     self.assertEqual(len(users), 0)
