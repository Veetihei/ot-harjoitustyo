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
    """Kursseihin liittyvistä tietokantaoperaatioista vastaava luokka
    """
    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden connection olio
        """
        self._connection = connection

    def add_new_course(self, username, name, weight, grade):
        """Lisää uuden kurssin tietokantaan

        Args:
            username: Merkkijonoarvo, kuvastaa käyttäjän käyttäjätunnusta
            name: Merkkijonoarvo, kuvastaa kurssin nimeä
            weight: Kokonaisluku, kuvastaa kurssin opintopisteitä
            grade: Kokonaisluku, kuvastaa kurssin arvosanaa
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into courses (username, name, weight, grade) values (?, ?, ?, ?)",
            (username, name, weight, grade)
        )

        self._connection.commit()

    def find_all(self):
        """Etsii ja palauttaa kaikki kurssit tietokannasta

        Returns:
            Palauttaa listana kaikki kurssit
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from courses",
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))

    def delete_all(self):
        """Poistaa kaikki kurssit tietokannasta
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from courses"
        )

        self._connection.commit()

    def find_by_course_name(self, name, username):
        """Etsii ja palauttaa tietyn käyttäjän tietyn kurssin

        Args:
            name: Merkkijonoarvo, joka kuvastaa kurssin nimeä
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta

        Returns:
            Palauttaa kurssin, jos se löytyi, None jos kurssia ei löytynyt
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from courses where name = ? and username = ?",
            (name, username)
        )

        row = cursor.fetchone()

        return get_course_by_row(row)

    def find_courses_by_username(self, username):
        """Etsii ja palauttaa käyttäjän kaikki kurssit

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta

        Returns:
            Palauttaa listana kaikki käyttäjän kurssit
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from courses where username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return list(map(get_course_by_row, rows))

    def delete_course(self, course_id):
        """Poistaa tietyn kurssin tietokannasta

        Args:
            course_id: Poistettavan kurssin id
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from courses where id = ?",
            (course_id,)
        )
        self._connection.commit()


course_repository = CourseRepository(get_database_connection())
