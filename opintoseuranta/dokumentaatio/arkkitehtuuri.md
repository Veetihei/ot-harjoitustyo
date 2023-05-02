## Käyttöliittymä

Sovelluksessa on 6 eri näkymää.

- Sisäänkirjautuminen

- Rekisteröityminen

- Kurssien perusnäkymä

- Kurssin lisäys

- Kurssin muokkaus

- Virheen ilmoitus

Jokainen näkymä on tehty omana luokkanaan. Sovelluksessa on aina näkyvillä vain yksi näkymä kerrallaan, jonka näyttämisestä ja vaihtamisesta vastaa UI luokka. Käyttöliittymä vastaa vain näkymistä, eikä se juurikaan sisällä sovelluslogiikkaa, joka hoidetaan CourseService luokan kautta.

## Tietojen tallennus

Sovellus tallentaa tiedot SQLite tietokantaan, jossa on 2 taulua seuraavasti:

```mermaid
classDiagram
  Kurssi "*" --> "1" Käyttäjä
  class Kurssi{
    id
    nimi
    op
    arvosana
  }
  class Käyttäjä{
    username
    password
  }
```

Tietokanta alustetaan initialize_database.py-tiedostossa, ja sen käyttämisestä vastaavat luokat CourseRepository ja UserRepository.

## Luokkakaavio

Sovellus on tehty kerrosarkkitehtuurin idealla, jakamalla seuraaviin kokonaisuuksiin:

- ui

- services

- entities

- repositories

![luokkakaavio](./images/luokkakaavio.png)

## Päätoiminnallisuudet

#### Uuden käyttäjän rekisteröiminen

Näkymässä käyttäjä syöttää käyttäjätunnuksen, sekä salasanan 2 kertaa. Kun käyttäjä painaa "Tee tunnus" Sovellus toimii seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CourseService
  participant UserRepository
  User->>UI: Click "Tee tunnus"
  UI->>CourseService: register("Kalle", "salasana123", "salasana123")
  CourseService->>CourseService: Check valid input
  CourseService->>UserRepository: register("Kalle", "salasana123")
  UserRepository-->>CourseService: True
  CourseService-->>UI: True
  UI->>UI: Initialize course view
```

Sovellus tarkastaa aluksi, onko käyttäjän syötteissä virheitä. Jos ei ole, sovellus tallentaa tietokantaan uuden käyttäjän ja siirtyy kurssinäkymään.

#### Sisäänkirjautuminen

Kun käyttäjä on kirjautuu sisään, etenee sovellus seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CourseService
  participant UserRepository
  User->>UI: Click "Kirjaudu sisään"
  UI->>CourseService: login("Kalle", "salasana123")
  CourseService->>UserRepository: find_by_username("Kalle")
  UserRepository-->>CourseService: User
  CourseService->>CourseService: check password
  CourseService-->>UI: True
  UI->>UI: Initialize course view
```

Sovellus hakee aluksi tietokannasta, onko käyttäjää olemassa. Jos käyttäjä on olemassa tarkastetaan, että salasana on oikea, jonka jälkeen siirrytään kurssinäkymään.

#### Kurssin lisääminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CourseService
  participant CourseRepository
  User->>UI: Click "Lisää kurssi"
  UI->>CourseService: add_course("OhPe", 5, 5)
  CourseService->>CourseService: Check valid input
  CourseService->>CourseRepository: add_course("Username", "OhPe", 5, 5)
  CourseRepository-->>CourseService: True
  CourseService-->>UI: True
  UI->>UI: Initialize course view
```
