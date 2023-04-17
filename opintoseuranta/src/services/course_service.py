from entities.user import User
from entities.courses import Course

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

    def register(self, username, password):
        # Virheiden käsittely tähän
        user = self._user_repository.register(User(username, password))

        self._user = user

        return user

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
        #Virheiden käsittely tähän
        course = self._course_repository.add_new_course(Course(username, name, weight, value))
        return
    
    def get_courses_by_username(self, username):
        return self._course_repository.find_courses_by_username(username)

course_service = CourseService()
