from database_connection import get_database_connection
#from entities.courses import Course

class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        return

course_repository = CourseRepository(get_database_connection())
