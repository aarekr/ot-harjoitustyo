# Changelog

## Viikko 1
* Harjoitustyön aiheen valinta
* Mallisovellukseen tutustuminen
* Oman työn suunnittelu

## Viikko 2
* Ohjelman runko luotu
* Käyttöliittymälle moduuli
* Ensimmäinen testi kirjoitettu

## Viikko 3
* Käyttäjä näkee marraskuun budjetti-ikkunan
* Käyttäjä voi syöttää arvioidut tulot ja kolme menoerää
* Käyttäjä voi syöttää toteutuneet tulot ja kolmen menoerää
* Käyttäjä voi painaa nappia, joka ilmoittaa paljon vielä budjetoitavissa
* Teksti- ja numerokentille luotu testit

## Viikko 4
* Pylint otettu käyttöön
* Invoke toimii ohjelman aloituksessa, testeissä ja pylint -tarkistuksessa
* Luokka Month ja hakemisto entitites luotu. Osa ui.py:n toiminnoista siirretty month.py -tiedostoon.
* Kuukausi-ikkunan sisältö jaettu neljään päällekkäin olevaan kehykseen (frame)
* Ikkunan yläreunassa navigointipalkki, jossa jokaiselle kuukaudelle oma nappi. Kuukauden vaihto marraskuusta tammikuuhun on kovakoodattuna ja kuukauden vaihto näkyy budjetointi-ikkunassa.
* Helmikuusta voi muodostaa olion.
* Menossa oleva kuukausi haetaan kalenterista (datetime).

## Viikko 5
* Ikkunassa on Quit -nappi, jota painamalla voi sulkea ohjelman
* Service -moduuli luotu ja toimintoja siirretty sen vastuulle
* Kaikki kuukausinapit toimivat ja hakevat halutun kuukauden tiedot
* Menu Bar lisätty: Quit ja Help toimivat
* Työkalupalkki sivun alareunassa
* Rent / mortgage ja Saving -erät

## Viikko 6
* Menu Bar, Toolbar, Help -ikkuna, sarake- ja riviotsikoiden luonti siirretty käyttöliittymästä service:n vastuulle.
* Käyttäjä voi nyt muuttaa 'planned' -lukuja ja ne ovat tallennettuina niin kauan kuin ohjelma on käynnissä
* Käyttäjä voi nyt muuttaa 'received/spent' -lukuja ja ne ovat tallennettuina niin kauan kuin ohjelma on käynnissä
* Help Window muutettu tekstikentästä ikkunaksi ja sen voi sulkea
* Year overview -nappi toimii ja avaa ikkunan. Dataa ei ikkunassa vielä ole.
* Docstring -dokumentointi
* Käyttöohjeen alustava versio
* Muuttujien nimiin ja funktioihin selvennyksiä ja parannettu luettavuutta

## Viikko 7
* Year overview -ikkuna ja analyysit valmiina
* Käyttäjä voi tallentaa budjettinsa .csv -tiedostoon ja avata sen
* Testit tiedoston avaamiselle ja tallentamiselle
* Syötekentille on lisätty validoinnit ja ne hyväksyvät vain kokonaisluvut
* Testit syötekentille
* Käyttäjältä varmistetaan, että haluaa sulkea ohjelman
* Kuukauden avaaminen näyttää heti valitun kuukauden tiedot
* Numerot sijoitetaan syötekenttien oikeaan reunaan
* ui.py:n start ja ui_helper:n show_year_summary -metodeja lyhennetty merkittävästi
* Dokumentaatio kirjoitettu loppuun
* Release ja palautus
