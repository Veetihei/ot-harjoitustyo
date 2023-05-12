
class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää

    Attributes:
        username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta
        password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa
    """

    def __init__(self, username, password):
        """Luokan konstruktori

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa
        """
        self.username = username
        self.password = password
