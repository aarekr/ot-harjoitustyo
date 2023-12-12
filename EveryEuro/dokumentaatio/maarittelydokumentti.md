# Vaatimusmäärittely

## Sovellus
* Sovelluksen mallina on käytetty Ramsey Solutionsin EveryDollar -sovellusta, joka on tarkoitettu menojen ja tulojen budjetointiin. Sovelluksen tavoitteena on tulojen ja menojen seuraaminen ja erityisesti hallinta, jotta käyttäjien velkojen lyhennykset ja varallisuuden kartuttaminen sujuisivat nopeammin. Jokaisella dollarilla ("every dollar") tarkoitetaan sitä, että jokaisella dollarilla (tai eurolla) on oma käyttötarkoituksensa esim. vuokra, ruoka ja säästäminen. Budjetti pyritään pitämään vähintäänkin tasapainossa sijoittamalla tulot ja menot sovellukseen.

## Käyttäjät
* Käyttäjä voi luoda (uniikin) käyttäjätunnuksen
* Käyttäjä voi kirjautua sovellukseen
* Käyttäjä voi kirjautua ulos sovelluksesta
* Sovelluksessa ei ole pääkäyttäjää

## Käyttöliittymä
* Sovellus aukeaa käyttöhetken kuukauden näkymään (tehty)
* Käyttäjä voi siirtyä navigointipalkista haluamansa kuukauden kohdalle (tehty)
* Käyttäjä voi syöttää arvioidut (planned) tulot ja menot kuukauden alussa (tehty)
* Käyttäjä voi syöttää toteutuneet (received / spent) tulot ja menot kuukauden aikana ja lopussa (tehty)
* Käyttäjä voi sulkea ohjelman ikkunassa olevasta Quit -napista tai valikosta (tehty)
* Käyttäjä voi painaa Help -nappia tai valitsemalla valikosta ja hänelle näytetään ohje miten ohjelmaa käytetään (tehty)
* Syötetyt tulot ja menot tallennetaan .csv -tiedostoon
* Käyttäjä voi avata vuosinäkymän ts. kaikki kalenterivuoden kuukaudet näkyvät tiivistettynä (nappi avaa ikkunan, tiedot puuttuvat)

## Yleistä
* Ohjelmointikieli ja versio: Python 3.8
* Käyttöliittymän toteutus: Tkinter
* Dokumentaation kieli: suomi
* Koodin kieli: englanti
* Sovelluksen kieli: englanti

## Lähteet
* Tkinter ja graafisen käyttöliittymän toteutus. Helsingin yliopisto. https://ohjelmistotekniikka-hy.github.io/python/tkinter
* Python GUI Programming With Tkinter. David Amos. https://realpython.com/python-gui-tkinter
* Programming Python. Mark Lutz. O'Reilly Media. (2011)
* Time delay Tkinter. Stackoverflow.com. https://stackoverflow.com/questions/19887729/time-delay-tkinter
