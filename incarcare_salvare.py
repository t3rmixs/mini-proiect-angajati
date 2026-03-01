"""
Modulul incarcare_salvare gestioneaza operatiunile de citire si scriere a datelor
din/in fisierul JSON principal (angajati.json).

Acest modul asigura persistenta datelor intre sesiuni ale aplicatiei.
"""

import os
import json

nume_fisier = "angajati.json"

def incarca_fisier_angajati() -> list[dict]:
    """
    Incarca datele angajatilor din fisierul JSON de stocare.
    
    Aceasta functie este apelata la pornirea aplicatiei pentru a restaura
    datele salvate anterior. Gestioneaza mai multe scenarii:
    
    1. Fisierul nu exista -> returneaza lista goala (prima rulare)
    2. Fisierul este corupt -> afiseaza eroare si returneaza lista goala
    3. Fisierul este valid -> returneaza lista de angajati
    
    Formatul fisierului JSON este o lista de dictionare, fiecare dictionar
    reprezentand un angajat cu urmatoarele campuri:
    - cnp, nume, prenume, varsta, salar, departament, senioritate
    
    Returns:
        list[dict]: Lista de dictionare cu datele angajatilor sau lista goala
                    daca fisierul nu exista sau este corupt.
                    
    Note:
        - Fisierul este citit cu encoding UTF-8 pentru suport caractere speciale
        - Erorile de tip JSONDecodeError si IOError sunt prinse si tratate graceful
        - Nu se opreste executia aplicatiei in caz de eroare de citire
    """
    if not os.path.exists(nume_fisier):
        return []
    try:
        with open(nume_fisier, "r", encoding="utf-8") as my_file:
            date: list[dict] = json.load(my_file)
            return date
    except (json.JSONDecodeError, IOError) as erroare_incarcare:
        print(f"Ai o mica eroare la citirea fisierului : {erroare_incarcare}")
        return []


def salveaza_fisier_angajati(angajati: list[dict]) -> bool:
    """
    Salveaza lista curenta de angajati in fisierul JSON de stocare.
    
    Aceasta functie este apelata dupa fiecare operatiune care modifica datele:
    - Adaugare angajat nou
    - Modificare date angajat existent
    - Stergere angajat
    
    Datele sunt formatate cu indent=4 pentru a fi usor de citit manual daca
    este necesar (debugging sau editare manuala).
    
    Args:
        angajati (list[dict]): Lista completa de angajati care trebuie salvata.
                               Fiecare element este un dictionar cu datele angajatului.
        
    Returns:
        bool: True daca salvarea a reusit cu succes, False daca a aparut o eroare
              (de exemplu: permisiuni insuficiente, disk plin, etc.)
              
    Note:
        - Fisierul este suprascris complet de fiecare data (nu append)
        - Encoding UTF-8 asigura suport pentru caractere romanesti
        - In caz de eroare, mesajul este afisat dar aplicatia continua
    """
    try:
        with open(nume_fisier, "w" , encoding="utf-8") as my_file:
            json.dump(angajati, my_file, indent=4)
        return True
    except IOError as error_save:
        print(f"Ai o mica eroare la salvarea fisierului : {error_save}")
        return False
    

