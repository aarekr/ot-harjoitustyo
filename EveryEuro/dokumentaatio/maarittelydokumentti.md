# Vaatimusmäärittely

## Sovellus
* Sovelluksen mallina on käytetty Ramsey Solutionsin EveryDollar -sovellusta, joka on tarkoitettu menojen ja tulojen budjetointiin. Sovelluksen tavoitteena on tulojen ja menojen seuraaminen ja erityisesti hallinta, jotta käyttäjien velkojen lyhennykset ja varallisuuden kartuttaminen sujuisivat nopeammin. Jokaisella dollarilla ("every dollar") tarkoitetaan sitä, että jokaisella dollarilla (tai eurolla) on oma käyttötarkoituksensa esim. vuokra, ruoka ja säästäminen. Budjetti pyritään pitämään vähintäänkin tasapainossa sijoittamalla tulot ja menot sovellukseen.

## Käyttäjät
* Käyttäjätunnusta ei sovelluksessa luoda. Ohjelmaa käytetään omalta kotikoneelta. Budjettitiedoston tallennuspaikan käyttäjä voi valita itse.

## Käyttöliittymä
- [x] Sovellus aukeaa käyttöhetken kuukauden näkymään
- [x] Käyttäjä voi siirtyä navigointipalkista haluamansa kuukauden kohdalle
- [x] Käyttäjä voi syöttää arvioidut (planned) tulot ja menot kuukauden alussa
- [x] Käyttäjä voi syöttää toteutuneet (received / spent) tulot ja menot kuukauden aikana ja lopussa
- [x] Ohjelman käyttöohjeen voi avata painamalla Help -nappia tai valikosta
- [x] Tallennetun budjetin voi avata painamalla Open -nappia tai valikosta
- [x] Syötetyt tulot ja menot voi tallentaa .csv -tiedostoon painamalla Save -nappia tai valikosta
- [x] Year overview -nappia painamalla käyttäjä näkee vuosiyhteenvedon
- [x] Ohjelman voi sulkea ikkunassa olevasta Quit -napista tai valikosta

## Jatkokehistyideoita
* Käyttäjätunnusten luonti mahdollistaisi useamman budjetoijan ohjelmankäytön samalta koneelta
* Sovelluksen yhteydessä voisi tiedostojen sijaan käyttää tietokantaa, jossa ylläpidetään käyttäjätilejä ja budjetteja
* Nykyisen yhden kokonaisen vuoden rakenteen voisi korvata Ramsey Solutionsin EveryDollar -sovelluksen tavoin jatkuvaksi ts. joulukuusta voi siirtyä seuraavan vuoden tammikuuhun luomatta erillistä vuotta/tiedostoa

## Yleistä
* Ohjelmointikieli ja versio: Python 3.8
* Käyttöliittymän toteutus: Tkinter
* Dokumentaation kieli: suomi
* Koodin kieli: englanti
* Sovelluksen kieli: englanti

## Laajat kielimallit
* Työssä ei ole käytetty laajoja kielimalleja.

## Lähteet
* Tkinter ja graafisen käyttöliittymän toteutus. Helsingin yliopisto. https://ohjelmistotekniikka-hy.github.io/python/tkinter
* Python GUI Programming With Tkinter. David Amos. https://realpython.com/python-gui-tkinter
* Programming Python. Mark Lutz. O'Reilly Media. (2011)
* Time delay Tkinter. Stackoverflow.com. https://stackoverflow.com/questions/19887729/time-delay-tkinter
* How to Pass Arguments to Tkinter Button Command? GeeksforGeeks. https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command
* Textbox (Entry) in Tk (tkinter). PythonAssets. https://pythonassets.com/posts/textbox-entry-in-tk-tkinter
