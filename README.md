# Proiect Gestiune Angajati (JSON Based)

Sistem de gestionare a bazei de date a angajatilor unei firme, utilizand fisiere locale JSON pentru stocarea datelor si o interfata interactiva in terminal.

## Functionalitati

* **Gestiune Angajati:** Adaugare, cautare, modificare si stergere angajati din sistem.
* **Validare Date:** Control automat pentru formatul CNP-ului (13 cifre), salariul minim legal si unicitatea datelor.
* **Calcul Salarii:** Calcularea automata a salariului NET, CAS, CASS si a impozitului pe baza salariului brut introdus.
* **Rapoarte si Statistici:** Calcularea costului total salarial pe intreaga firma sau pe departamente specifice.
* **Export Fluturasi:** Generarea de fisiere JSON individuale pentru fiecare angajat in folderul `fluturasi_angajati`.
* **Filtrare:** Afisarea angajatilor filtrati dupa senioritate sau dupa departament.

## Structura Modulelor

* **main.py**: Punctul central al aplicatiei si gestionarea meniului principal.
* **operatiuni_date.py**: Contine logica pentru operatiunile CRUD (Adaugare, Modificare, Stergere).
* **validari.py**: Functii de verificare a input-ului (format CNP, departamente, senioritate).
* **calculare.py**: Modul dedicat calculelor matematice (taxe salariale si sume totale).
* **incarcare_salvare.py**: Gestioneaza citirea si scrierea datelor in `angajati.json`.
* **exportare.py**: Logica pentru crearea si citirea fluturasilor de salariu exportati.
* **stil.py**: Configurare culori ANSI pentru terminal si formatare mesaje (succes, eroare, info).

## Instructiuni de Utilizare

1. Asigura-te ca ai Python 3 instalat.
2. Ruleaza scriptul principal:
   ```bash
   python main.py
