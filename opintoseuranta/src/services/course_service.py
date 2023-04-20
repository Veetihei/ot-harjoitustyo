from entities.user import User
# from entities.courses import Course

from repositories.users_repository import (
    user_repository as default_user_repository
)
from repositories.courses_repository import (
    course_repository as default_course_repository
)


class CourseService:
    def __init__(
        self,
        user_repository=default_user_repository,
        course_repository=default_course_repository
    ):
        self._user = None
        self._user_repository = user_repository
        self._course_repository = course_repository

    def register(self, username, password, password_check):
        # Virheiden käsittely tähän
        if len(username) < 3 or len(username) > 10:
            return "Käyttäjätunnuksen on oltava 3-10 merkkiä"
        if password != password_check:
            return "Salasanat eivät täsmää"
        if len(password) < 3 or len(password) > 10:
            return "Salasanan on oltava 3-10 merkkiä"
        
        user = self._user_repository.register(User(username, password))

        self._user = user

        return True

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if user and user.password == password:
            self._user = user
            # print("Kirjauduttu")
            return user
        return None

    def get_current_user(self):
        return self._user

    def add_new_course(self, username, name, weight, value):
        # Virheiden käsittely tähän
        if len(name) < 3:
            return
        if int(weight) < 0:
            return
        if int(value) < 0 or int(value) > 5:
            return
        self._course_repository.add_new_course(username, name, weight, value)

    def get_courses_by_username(self, username):
        return self._course_repository.find_courses_by_username(username)

    def delete_course(self, course_id):
        self._course_repository.delete_course(course_id)

    def get_course_stats(self, username):
        courses = self.get_courses_by_username(username)
        weight_sum = 0
        grade_sum = 0
        courses_number = 0
        for course in courses:
            weight_sum += course.weight
            grade_sum += course.grade * course.weight
            courses_number += 1
        if weight_sum != 0:
            grade_mean = grade_sum / weight_sum
        else:
            grade_mean = 0
        return grade_mean, weight_sum, courses_number


course_service = CourseService()
