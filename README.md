# EveryEuro
Aineopintojen harjoitustyö: Ohjelmistotekniikka (periodi 2) 2023

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## EveryEuro Budget
* Harjoitustyön aihe: EveryEuro -budjetointisovellus
* Ramsey Solutionsin [EveryDollar](https://www.ramseysolutions.com/ramseyplus/everydollar) -sovelluksen kaltainen tulojen ja menojen budjetointiin tarkoitettu sovellus
* Sovellus luotu Python 3.8 -versiolla

## Dokumentaatio
* [Käyttöohje](https://github.com/aarekr/ot-harjoitustyo/tree/main/EveryEuro/dokumentaatio/kayttoohje.md)
* [Määrittelydokumentti](https://github.com/aarekr/ot-harjoitustyo/tree/main/EveryEuro/dokumentaatio/maarittelydokumentti.md)
* [Arkkitehtuurikuvaus](https://github.com/aarekr/ot-harjoitustyo/blob/main/EveryEuro/dokumentaatio/arkkitehtuuri.md)
* [Testausdokumentti](https://github.com/aarekr/ot-harjoitustyo/tree/main/EveryEuro/dokumentaatio/testausdokumentti.md)
* [Tuntikirjanpito](https://github.com/aarekr/ot-harjoitustyo/tree/main/EveryEuro/dokumentaatio/tuntikirjanpito.md)
* [Changelog](https://github.com/aarekr/ot-harjoitustyo/tree/main/EveryEuro/dokumentaatio/changelog.md)

## Asennus ja käynnistäminen
1. Asenna riippuvuudet:
```bash
poetry install
```
Näytöllä saattaa näkyä virheilmoitus README.md -tiedoston puuttumisesta mutta sen voi ohittaa.

2. Käynnistä ohjelma:
```bash
poetry run invoke start
```

## Testit
1. Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```

2. Testikattavuusraportin voi generoida:
```bash
poetry run invoke coverage
```
ja tämän jälkeen
```bash
poetry run invoke coverage-report
```
Raportti (index.html) löytyy _htmlcov_-hakemistosta.

## Pylint
Komento:
```bash
poetry run invoke lint
```
