from entities.user import User
# from entities.courses import Course

from repositories.users_repository import (
    user_repository as default_user_repository
)
from repositories.courses_repository import (
    course_repository as default_course_repository
)


class CourseService:
    """Sovelluslogiikasta vastaava luokka
    """

    def __init__(
        self,
        user_repository=default_user_repository,
        course_repository=default_course_repository
    ):
        """Luokan konstruktori.

        Args:
            user_repository:
                UserRepository olio, jolla on luokkaa vastaavat metodit. 
                Oletusarvoisesti UserRepository olio.
            course_repository: 
                CourseRepository olio, jolla on luokkaa vastaavat metodit. 
                Oletusarvoisesti CourseRepository olio.
        """
        self._user = None
        self._user_repository = user_repository
        self._course_repository = course_repository

    def register(self, username, password, password_check):
        """Tarkastaa uuden käyttäjätunnuksen luomisen syötteet ja rekisteröi uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvastaa salasanaa
            password_check: Merkkijonoarvo, joka kuvastaa salasanaa

        Returns:
            True, jos käyttäjän rekisteröinti onnistui ja virheviestin, jos ei onnistunut.
        """
        if len(username) < 3 or len(username) > 10:
            return "Käyttäjätunnuksen on oltava 3-10 merkkiä"
        if password != password_check:
            return "Salasanat eivät täsmää"
        if len(password) < 3 or len(password) > 10:
            return "Salasanan on oltava 3-10 merkkiä"

        user = self._user_repository.find_by_username(username)

        if user:
            return "Käyttäjätunnus on jo olemassa"
        user = self._user_repository.register(User(username, password))

        self._user = user

        return True

    def login(self, username, password):
        """Kirjaa olemassa olevan käyttäjän sisään

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvastaa salasanaa

        Returns:
            Käyttäjän User oliona, jos kirjautuminen onnistui, None jos ei onnistunut
        """
        user = self._user_repository.find_by_username(username)

        if user and user.password == password:
            self._user = user
            return user
        return None

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän User oliona

        Returns:
            Kirjautuneen käyttäjän User oliona
        """
        return self._user

    def add_new_course(self, username, name, weight, grade):
        """Tarkastaa uuden kurssin luomisen syötteet ja tallentaa uuden kurssin

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta
            name: Merkkijonoarvo, joka kuvastaa kurssin nimeä
            weight: Kokonaislukuarvo, joka kuvastaa kurssin opintopisteitä
            grade: Kokonaislukuarvo, joka kuvastaa kurssin arvosanaa

        Returns:
            True, jos kurssin lisääminen onnistui, virheviesti jos ei onnistunut
        """
        if len(name) < 3:
            return "Kurssin nimi on liian lyhyt"
        try:
            if int(weight) < 0:
                return "Opintopisteet eivät voi olla negatiivisia"
            if int(grade) < 1 or int(grade) > 5:
                return "Arvosanan on oltava 1-5 välillä"
        except ValueError:
            return "Arvosanan ja opintopisteiden täytyy olla kokonaislukuja"
        
        course_exists = self._course_repository.find_by_course_name(
            name, username)

        if course_exists:
            return "Kurssi on jo lisätty"

        self._course_repository.add_new_course(username, name, weight, grade)
        return True

    def get_courses_by_username(self, username):
        """Hakee käyttäjän kaikki kurssisuoritukset

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta

        Returns:
            Kaikki käyttäjän kurssit listana
        """
        return self._course_repository.find_courses_by_username(username)

    def delete_course(self, course_id):
        """Poistaa tietyn kurssin

        Args:
            course_id: poistettavan kurssin id
        """
        self._course_repository.delete_course(course_id)

    def get_course_stats(self, username):
        """Palauttaa suoritettujen kurssien tunnusluvut

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta

        Returns:
            kurssien keskiarvo, opintopisteiden summa ja kurssien määrä
        """
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

    def find_all_courses(self):
        """Palauttaa kaikki kurssit

        Returns:
            kaikki kurssit listana
        """
        return self._course_repository.find_all()


course_service = CourseService()
