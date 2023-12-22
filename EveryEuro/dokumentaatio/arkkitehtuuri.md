# Arkkitehtuuri

## Rakenne
Ohjelman rakenne:

Tiedostossa ui on sovelluksen käyttöliitymä ja sen aputiedosto. Entities -hakemisto sisältää kuukausien hallintaan liittyvät tiedot. Services -hakemisto sisältää ohjelman logiikan.

![](./kuvat/main_window.png)

## Käyttöliittymä
Käyttöliittymä sisältää:
* Ohjelman pääikkunan, jossa lukujen syöttäminen tapahtuu
* Vaihtaminen kuukaudesta toiseen vaihtaa pääikkunassa näkyvät tiedot
* Help -ikkuna sisältää ohjeen miten ohjelmaa käytetään
* Year overview -ikkuna sisältää vuoden lukujen yhteenvedon ja niihin liittyvät kommentit

## Sovelluslogiikka
Sovelluslogiikan muodostavat luokat User ja Month. Jokaiseen käyttäjään liittyy 12 kuukautta.
```mermaid
  classDiagram
    Month "12" --> "1" User
    class User{
    }
    class Month{
        id
        income
        rent / mortgage
        bills
        spending
        debt service
        saving
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

## Tietojen tallennus
Käyttäjä tallentaa tietonsa CSV-tiedostoon. Tiedoston voi myöhemmin avata ja tietoja muuttaa.

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
  Service->>UI: 12 months
  User->>UI: click "Month"
  UI->>Service: get_and_display_chosen_month_data(month_number)
  Month->>UI: month
  UI->>Service: open_data_from_file()
  Service->>File: open file
  File->>Service: file contents
  Service->>UI: 12 month data
  UI->>Service: save_data_to_file()
  Service->>File: budjet data
  User->>UI: click "Help"
  UI->>UI: open_help_window()
  User->>UI: click "Year overview"
  UI->>UI: open_year_overview_window()
  UI->>Service: calculate_year_figures(table_all_months_receivedspent)
  Service->>UI: figures analyzed
```
