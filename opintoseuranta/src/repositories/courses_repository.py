from database_connection import get_database_connection
from entities.courses import Course


def get_course_by_row(row):
    return Course(
        row["id"],
        row["username"],
        row["name"],
        row["weight"],
        row["grade"]) if row else None


class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_new_course(self, username, name, weight, grade):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into courses (username, name, weight, grade) values (?, ?, ?, ?)",
            (username, name, weight, grade)
        )

        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from courses",
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from courses"
        )

        self._connection.commit()

    def find_by_course_name(self, name, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from courses where name = ? and username = ?",
            (name, username)
        )

        row = cursor.fetchone()

        return get_course_by_row(row)

    def find_courses_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from courses where username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))

    def delete_course(self, course_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from courses where id = ?",
            (course_id,)
        )
        self._connection.commit()


course_repository = CourseRepository(get_database_connection())
