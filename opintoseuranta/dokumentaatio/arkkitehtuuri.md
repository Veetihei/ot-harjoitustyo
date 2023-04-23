## Käyttöliittymä

Lopullisessa sovelluksess on 5 eri näkymää.

- Sisään kirjautuminen

- Rekisteröityminen

- Kurssien perusnäkymä

- Kurssin lisäys

- Kurssin muokkaus

## Tietojen tallennus

Sovellus tallentaa tiedot tietokantaan, jossa on 2 taulua seuraavasti:

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

## Luokkakaavio

Sovellus on tehty kerrosarkkitehtuurin idealla, jakamalla seuraaviin kokonaisuuksiin:

- ui

- services

- entities

- repositories

![luokkakaavio](./images/luokkakaavio.png)

## Kurssin lisääminen

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
  
  
