from database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden connection olio
        """
        self._connection = connection

    def find_all(self):
        """Etsii ja palauttaa kaikki käyttäjät

        Returns:
            Palauttaa kaikki käyttäjät listana User olioita
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))

    def register(self, user):
        """Lisää tietokantaan uuden käyttäjän

        Args:
            user: User-olio, joka sisältää käyttäjätunnuksen ja salasanan

        Returns:
            Palauttaa käyttäjän User-oliona
        """
        cursor = self._connection.cursor()

        cursor.execute("insert into users (username, password) values (?, ?)",
                       (user.username, user.password))

        self._connection.commit()

        return user

    def find_by_username(self, username):
        """Etsii tietokannasta käyttäjän käyttäjätunnuksen perusteella

        Args:
            username: Käyttäjätunnus

        Returns:
            Palauttaa User-oliona käyttäjän, tai None jos käyttäjää ei ole
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from users"
        )

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
