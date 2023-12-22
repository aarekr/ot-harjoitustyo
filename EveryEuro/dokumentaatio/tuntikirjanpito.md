# Tuntikirjanpito

## Viikko 1

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
07.11. |  1h  | EveryDollar -sovellukseen tutustuminen ja työn suunnittelu |


## Viikko 2

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
14.11. |  4h  | Määrittelydokumentti ja tuntikirjanpito luotu. Tkinteriin tutustuminen. Ohjelma avautuu ikkunaan ja siinä on yksinkertaisia tekstikomponentteja. Yksi testi kirjoitettu. |


## Viikko 3

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
18.11. |  2h  | ui.py -moduulin importtausongelma ratkaistu. Numeroiden syöttökentät ja left to budget luotu. |
19.11. |  1h  | Testit numerokentille ja left to budget -komponenteille. |
20.11. |  2h  | Testikattavuusraportti ja Changelog. tests-hakemistossa nyt __init__.py. Sarakkeet 'Type' ja 'Planned' nimetty. 'Actual' -sarake hahmoteltu. |
21.11. |  2h  | Actual -sarake ja numerokentät. Planned -muuttujien uudelleennimeäminen ja testien päivitys. Invokeen tutustuminen. |


## Viikko 4

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
25.11. |  2h  | Hakemisto entities ja luokka Month. Logiikkaa erotettu käyttöliittymästä. Pylint otettu käyttöön. |
26.11. |  2h  | Tkinterin widgettien opettelua. Testi toiminnolle calculate balance. Welcome View:n kehittämistä. Kuukausi-ikkunan sisältö jaettu neljään kehykseen. |
27.11. |  3h  | Budjetointi-ikkunan yläreunassa on kuukausille navigointinapit. Vaihto marraskuusta tammikuuhun on kovakoodattuna. Calculate balance -toiminto hajosi. Helmikuu-olion luonti kovakoodattuna. |
28.11. |  3h  | Arkkitehtuurin dokumentointi. Menossa oleva kuukausi haetaan datetime -toiminnolla. MAR-nappia painamalla luodaan Maaliskuu-olio ja sille budjetointilukemat (kovakoodattu). |


## Viikko 5

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
02.12. | 5,5h | Quit -nappi sulkee ikkunan. Planned entry -kenttien ja kuukausien vaihdon parissa työskentely. Maaliskuun ja huhtikuun tiedot ilmestyvät entry -kenttiin kun näitä kuukausinappeja painetaan (kovakoodattu ja toistoa). |
03.12. | 3,5h | Service -moduuli luotu. Kuukausinapit toimivat ja hakevat halutun kuukauden tiedot ikkunaan. |
04.12. |  3h  | Menu Bar lisätty. Quit lopettaa ohjelman ja Help ohjeistaa ohjelman käytössä. Open on kesken. |
05.12. |  6h  | Työkalupalkki sivun alareunassa. Rent/mortgage ja Saving -erät lisätty. Toimintoja siirretty käyttöliittymästä service -moduuliin. Lisää testejä. |


## Viikko 6

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
09.12. |  3h  | Menu Bar, Toolbar, Help -ikkuna sekä sarake- ja riviotsikoiden luonti siirretty käyttöliittymästä service:n vastuulle. Käyttäjä voi nyt muuttaa 'planned' -lukuja. |
10.12. | 2,5h | Käyttäjä voi syöttää, muuttaa ja tallentaa 'received/spent' -lukuja. Help Window muutettu tekstikentästä ikkunaksi. Year overview -nappi avaa ikkunan. |
11.12. | 2,5h | Lisää testejä. Docstring -dokumentointi. Progressbar Year overview -ikkunassa. |
12.12. |  3h  | Muuttujien ja funktioiden nimien selvennyksiä. Puuttuneet Docstringit lisätty. Help Window -tekstit taulukossa ja ne käydään läpi for -silmukalla. Käyttöohjeen alustava versio. |


## Viikko 7

 Pvm   | Aika | Aktiviteetti |
-------|------|--------------|
13.12. |  3h  | Käyttöliittymän start -metodista siirretty toimintoja ulos. ui_helper -moduulin vastuulle siirretty osa toiminnoista. Year overview:n kehittämistä. |
14.12. |  3h  | Year overview ikkuna ja analyysit tehty. Tutkittu Dash ja Matplotlib -kirjastojen käyttömahdollisuutta työssä. |
15.12. |  2h  | Käyttäjä voi tallentaa budjettinsa .csv -tiedostoon ja avata sen (toolbarin napit). |
16.12. | 3,5h | Syötekenttien validointi - vain kokonaisluvut hyväksytään. Koodin siistiminen ja yhtenäistäminen. Kuukauden avaaminen näyttää heti valitun kuukauden tiedot. Käyttäjältä varmistetaan, että haluaa sulkea ohjelman. Testit tiedostojen avaamiselle ja tallentamiselle. |
17.12. | 1,5h | Lisää testejä tiedostojen avaamiselle ja tallentamiselle. Testit syötekentille. |
19.12. |  3h  | Ikkunan yläosan kuukausinapit luodaan nyt for -silmukalla. Käyttöliittymästä siirretty useita toimintoja ulos. Käyttöliittymän koodia refaktoroitu. |
20.12. |  1h  | Numerot ovat nyt kenttien oikeassa reunassa. ui_helper -moduulin refaktorointia. |
21.12. | 2,5h | ui_helper.py:n show_year_summary -metodi jaettu osiin. Yritetty korjata year_overview:n receivedspent -taulukon 0-arvot-ongelmaa. |
22.12. | 7,5h | Tiedostojen refaktorointia, vielä joitakin toimintoja siirretty oikeisiin paikkoihin. Testausdokumentti luotu. Dokumentaatio kirjoitettu loppuun. Release ja palautus. |


## Yhteensä
 Viikko  |  Aika  |
---------|--------|
|   1    |    1h  |
|   2    |    4h  |
|   3    |    7h  |
|   4    |   10h  |
|   5    |   18h  |
|   6    |   11h  |
|   7    |   27h  |
| Summa  |   78h  |
