# Arkkitehtuuri

## Ohjelman rakenne
Hakemistossa ui on sovelluksen käyttöliitymä ja sen aputiedosto. Entities -hakemisto sisältää kuukausien hallintaan liittyvät tiedot. Services -hakemisto sisältää ohjelman logiikan.

![](./kuvat/arkkitehtuuri.png)

## Käyttöliittymä
Käyttöliittymä sisältää:
* Ohjelman pääikkunan, jossa lukujen syöttäminen tapahtuu
* Vaihtaminen kuukaudesta toiseen vaihtaa pääikkunassa näkyvät tiedot
* Help -ikkuna sisältää ohjeen miten ohjelmaa käytetään
* Year overview -ikkuna sisältää vuoden lukujen yhteenvedon ja niihin liittyvät kommentit

## Sovelluslogiikka
Sovelluslogiikan muodostavat service -moduuli ja luokka Month. Käyttäjään liittyy 12 kuukautta.
```mermaid
  classDiagram
    Month "12" --> "1" User
    class Month{
        id
        income
        rent / mortgage
        bills
        spending
        debt service
        saving
    }
    class User{
    }
```

Service -moduuli tarjoaa sovellukselle seuraavat toiminnot:
* create_all_months_table()
* get_month_name(month_number)
* get_month_number_and_name(month_name)
* calculate_left_to_budget(income, rent, bills, spending, debt_service, saving)
* calculate_year_figures(table_all_months_receivedspent)
* get_planned_values(table_all_months_planned, month_number)
* update_entry_field_value(entry_field, new_value)
* open_data_from_file()
* save_data_to_file(table_all_months_planned, table_all_months_receivedspent)
* quit_program(root)

## Tiedot kahdessa taulukossa
* Tulojen ja menoerien hallintaan on kaksi taulukkoa, joista toinen sisältää planned -luvut ja toinen received/spent -luvut.

## Tietojen tallennus
Käyttäjä tallentaa budjettinsa CSV-tiedostoon. Tiedoston voi myöhemmin avata ja tietoja muuttaa.

## Päätoiminnallisuudet

### Kuukausibudjetin luominen
Eri kuukausille voi luoda budjetin valitsemalla ikkunan yläreunasta haluttu kuukausi, syöttämällä luvut Planned -sarakkeen syötekenttiin ja klikkaamalla Save planned -nappia. Toteutuneet tulot ja menot syötetään Received/Spent -sarakkeen kenttiin ja tallennetaan klikkaamalla Save rec./spent.
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Service
  participant Month
  participant File
  UI->>Service: create_all_months_table()
  Service->>Month: create 12 months
  Month->>Service: 12 month objects
  Service->>UI: 12 months table
  User->>UI: click "month" button
  UI->>Service: get_and_display_chosen_month_data(month_number)
  Service->>UI: updated field values
  User->>UI: click Open
  UI->>Service: open_data_from_file()
  Service->>File: open file
  File->>Service: file contents
  Service->>UI: 12 month data
  User->>UI: click "Save"
  UI->>Service: save_data_to_file()
  Service->>File: budget data
  User->>UI: click "Help"
  UI->>UI: open_help_window()
  User->>UI: click "Year overview"
  UI->>UI: open_year_overview_window()
  UI->>Service: calculate_year_figures(table_all_months_receivedspent)
  Service->>UI: figures analyzed
```
