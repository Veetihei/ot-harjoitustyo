from database_connection import get_database_connection
from entities.courses import Course

class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        return self._read()
    
    def find_by_userid(self, userid):
        courses = self.find_all()

        user_courses = filter(

        )

course_repository = CourseRepository(get_database_connection())
