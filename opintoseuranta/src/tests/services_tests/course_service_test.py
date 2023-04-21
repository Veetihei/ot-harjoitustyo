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
        self.course_ohpe = Course(1, self.user_testaaja.username, "OhPe", 5, 5)
        self.course_tito = Course(2, self.user_testaaja.username, "TiTo", 5, 2)
        self.course_ohte = Course(3, self.user_testaaja.username, "OhTe", 5, 5)

    def test_course_service_test_works(self):
        self.assertEqual("Hello world!", "Hello world!")

    def register_user(self, user):
        return self.course_service.register(
            user.username,
            user.password,
            user.password
        )

    def login_user(self, user):
        return self.course_service.login(user.username, user.password)

    def add_new_course(self, user, course):
        return self.course_service.add_new_course(
            user.username,
            course.name,
            course.weight,
            course.grade
        )

    def test_register_works(self):
        result = self.course_service.register(
            self.user_testaaja.username,
            self.user_testaaja.password,
            self.user_testaaja.password
        )

        self.assertEqual(result, True)

    def test_register_short_name(self):
        result = self.course_service.register(
            "Ly",
            "password",
            "password"
        )

        self.assertEqual(result, "Käyttäjätunnuksen on oltava 3-10 merkkiä")

    def test_register_long_name(self):
        result = self.course_service.register(
            "Tosipitkänimi",
            "password",
            "password"
        )

        self.assertEqual(result, "Käyttäjätunnuksen on oltava 3-10 merkkiä")

    def test_register_short_password(self):
        result = self.course_service.register(
            "Testaaja",
            "a",
            "a"
        )

        self.assertEqual(result, "Salasanan on oltava 3-10 merkkiä")

    def test_register_long_password(self):
        result = self.course_service.register(
            "Testaaja",
            "tosipitkäsalasana",
            "tosipitkäsalasana"
        )

        self.assertEqual(result, "Salasanan on oltava 3-10 merkkiä")

    def test_register_different_passwords(self):
        result = self.course_service.register(
            "Testaaja",
            "salis",
            "salasana"
        )

        self.assertEqual(result, "Salasanat eivät täsmää")

    def test_register_existing_user(self):
        self.register_user(self.user_testaaja)
        result = self.register_user(self.user_testaaja)

        self.assertEqual(result, "Käyttäjätunnus on jo olemassa")

    def test_login_works(self):
        self.register_user(self.user_testaaja)
        user = self.course_service.login(
            self.user_testaaja.username, self.user_testaaja.password)

        self.assertEqual(user.username, self.user_testaaja.username)
        self.assertEqual(user.password, self.user_testaaja.password)

    def test_login_wrong_username(self):
        self.register_user(self.user_testaaja)
        user = self.course_service.login(
            "Vaara_nimi", self.user_testaaja.password)

        self.assertEqual(user, None)

    def test_login_wrong_password(self):
        self.register_user(self.user_testaaja)
        user = self.course_service.login(
            self.user_testaaja.username, "vaara_salis")

        self.assertEqual(user, None)

    def test_add_new_course(self):
        result = self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )

        self.assertEqual(result, True)

    def test_find_all_courses(self):
        courses = self.course_service.find_all_courses()
        self.assertEqual(len(courses), 0)

        self.add_new_course(self.user_testaaja, self.course_ohpe)

        courses = self.course_service.find_all_courses()
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

        self.add_new_course(self.user_testaaja, self.course_ohte)
        self.add_new_course(self.user_testaaja, self.course_tito)

        courses = self.course_service.find_all_courses()
        self.assertEqual(len(courses), 3)

    def test_add_existing_course(self):
        self.add_new_course(self.user_testaaja, self.course_ohpe)
        result = self.add_new_course(self.user_testaaja, self.course_ohpe)

        self.assertEqual(result, "Kurssi on jo lisätty")

        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 1)

    def test_add_course_high_grade(self):
        result = self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            10
        )

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)
        self.assertEqual(result, "Arvosanan on oltava 1-5 välillä")

    def test_add_negative_grade(self):
        result = self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            self.course_ohpe.weight,
            -1
        )

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)
        self.assertEqual(result, "Arvosanan on oltava 1-5 välillä")

    def test_add_course_short_name(self):
        result = self.course_service.add_new_course(
            self.user_testaaja.username,
            "A",
            self.course_ohpe.weight,
            self.course_ohpe.grade
        )

        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)
        self.assertEqual(result, "Kurssin nimi on liian lyhyt")

    def test_add_course_negative_weight(self):
        result = self.course_service.add_new_course(
            self.user_testaaja.username,
            self.course_ohpe.name,
            -10,
            self.course_ohpe.grade
        )
        courses = course_repository.find_all()
        self.assertEqual(len(courses), 0)
        self.assertEqual(result, "Opintopisteet eivät voi olla negatiivisia")

    def test_get_courses_by_username(self):
        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 0)

        self.add_new_course(self.user_testaaja, self.course_ohpe)

        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, "OhPe")

        self.add_new_course(self.user_testaaja, self.course_ohte)
        self.add_new_course(User("Toinen", "salis"), self.course_tito)

        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 2)

    def test_get_current_user(self):
        self.register_user(self.user_testaaja)

        self.login_user(self.user_testaaja)

        user = self.course_service.get_current_user()

        self.assertEqual(user.username, self.user_testaaja.username)

    def test_delete_course(self):
        self.add_new_course(self.user_testaaja, self.course_ohpe)

        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 1)

        course_id = courses[0].id

        self.course_service.delete_course(course_id)

        courses = self.course_service.get_courses_by_username(
            self.user_testaaja.username)
        self.assertEqual(len(courses), 0)

    def test_get_mean_grade(self):
        self.add_new_course(self.user_testaaja, self.course_ohpe)
        self.add_new_course(self.user_testaaja, self.course_tito)

        mean_grade = self.course_service.get_course_stats(
            self.user_testaaja.username)[0]

        self.assertEqual(mean_grade, 3.5)

        self.add_new_course(self.user_testaaja, self.course_ohte)

        mean_grade = self.course_service.get_course_stats(
            self.user_testaaja.username)[0]

        self.assertEqual(mean_grade, 4)

    def test_get_course_weights(self):
        self.add_new_course(self.user_testaaja, self.course_ohpe)
        self.add_new_course(self.user_testaaja, self.course_tito)

        courses_weight = self.course_service.get_course_stats(
            self.user_testaaja.username)[1]

        self.assertEqual(courses_weight, 10)

        self.add_new_course(self.user_testaaja, self.course_ohte)

        courses_weight = self.course_service.get_course_stats(
            self.user_testaaja.username)[1]

        self.assertEqual(courses_weight, 15)

    def test_get_courses_number(self):
        self.add_new_course(self.user_testaaja, self.course_ohpe)
        self.add_new_course(self.user_testaaja, self.course_tito)

        courses_num = self.course_service.get_course_stats(
            self.user_testaaja.username)[2]

        self.assertEqual(courses_num, 2)

        self.add_new_course(self.user_testaaja, self.course_ohte)

        courses_num = self.course_service.get_course_stats(
            self.user_testaaja.username)[2]

        self.assertEqual(courses_num, 3)

    def test_get_course_stat_no_courses(self):
        course_stats = self.course_service.get_course_stats(
            self.user_testaaja.username)

        self.assertEqual(course_stats[0], 0)
        self.assertEqual(course_stats[1], 0)
        self.assertEqual(course_stats[2], 0)
