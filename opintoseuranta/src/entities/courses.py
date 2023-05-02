
class Course:
    """Luokka, joka kuvastaa yksittäistä kurssia

    Attributes:
        id: Kurrsin yksilöivä id
        username: Kurssin suorittajan käyttäjätunnus
        name: Kurssin nimi
        weight: kurssin opintopisteet
        grade: Kurssin arvosana
    """
    def __init__(self, id, username, name, weight, grade):
        """Luokan konstruktori

        Args:
            id: Kurrsin yksilöivä id
            username: Kurssin suorittajan käyttäjätunnus
            name: Kurssin nimi
            weight: kurssin opintopisteet
            grade: Kurssin arvosana
        """
        self.id = id
        self.username = username
        self.name = name
        self.weight = weight
        self.grade = grade
