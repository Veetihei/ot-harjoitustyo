from database_connection import get_database_connection
from entities.courses import Course


def get_course_by_row(row):
    return Course(row["username"], row["name"], row["weight"], row["grade"]) if row else None


class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_new_course(self, course):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into courses (username, name, weight, grade) values (?, ?, ?, ?)",
            (course.username, course.name, course.weight, course.grade)
        )

        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from courses"
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))
    
    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from courses"
        )

        self._connection.commit()

    def find_courses_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from courses where username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))


course_repository = CourseRepository(get_database_connection())
