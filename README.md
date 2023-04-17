# OhTe-kurssin palautuskansio

Tämä on helsingin yliopiston ohjelmistotekniikka-kurssille tehty palautuskansio.

# Opintoseuranta sovellus

Opintoseuranta sovelluksen avulla voi pitää kirjaa omista opinnoistaan. Sovellukseen voi lisätä suorittamia kursseja, sekä muokata jo suoritettuja kursseja. Sovellus näyttää käyttäjällä, kuinka monta opintopistettä hän on suorittanut, millä keskiarvolla, sekä listan kaikista suorituksista. Sovellukseen voi kirjautua olemassa oolevalla käyttäjällä tai rekisteröityä uutena käyttäjänä.

## Dokumentaatio

[vaatimusmäärittely](opintoseuranta/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](opintoseuranta/dokumentaatio/tuntikirjanpito.md)

[Changelog](opintoseuranta/dokumentaatio/changelog.md)

[Arkkitehtuuri](opintoseuranta/dokumentaatio/arkkitehtuuri.md)

## Sovelluksen käyttäminen

Aloita asentamalla sovelluksen riippuvuudet komennolla:

```console
poetry install
```

Seuraavaksi alustetaan tietokanta komennolla:

```console
poetry run invoke build
```

Nyt sovelluksen voi käynnistää komennolla:

```console
poetry run invoke start
```

## Sovelluksen testaus

Sovelluksen testit pystyy suorittamaan komennolla:

```console
poetry run invoke test
```

Testikattavuusraportin saa komennolla

```console
poetry run invoke coverage-report
```
