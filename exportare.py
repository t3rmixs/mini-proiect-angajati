"""
Modulul exportare gestioneaza operatiunile de export si import al fluturasilor
de salariu in format JSON.

Acest modul permite:
- Exportul fluturasului de salariu pentru un angajat
- Actualizarea fluturasului existent
- Afisarea fluturasului din fisierul JSON
"""

import os
import validari
import json

def exporteaza_fluturas(angajati: list[dict]) -> None:
    """
    Exporta fluturasul de salariu al unui angajat in format JSON.
    
    Functia calculeaza toate componentele salariului (brut, CAS, CASS, impozit, net)
    si salveaza intr-un fisier JSON structurat in folderul 'fluturasi_angajati'.
    
    Numele fisierului este generat automat pe baza CNP-ului:
    Format: fluturasi_angajati/fluturas_{CNP}.json
    
    Datele exportate includ:
    - Nume si prenume
    - CNP
    - Departament
    - Salariu brut
    - CAS (10%)
    - CASS (25%)
    - Impozit (10%)
    - Salariu net
    
    Args:
        angajati (list[dict]): Lista de angajati in care se cauta angajatul.
        
    Returns:
        None: Functia creeaza fisierul JSON si afiseaza confirmare.
        
    Note:
        - Cautarea se face dupa CNP
        - Utilizatorul poate introduce '0' pentru a anula
        - Fisierul este suprascris daca deja exista pentru acel CNP
        - Datele numerice sunt rotunjite la 2 zecimale
    """
    print("\n-- Export fluturasi de salar")

    while True:
        cnp: str = validari.cere_cnp_valid()
           
        if cnp == "0":
            return
        
        gasit: bool = False
        for persoana in angajati:
            if persoana["cnp"] == cnp:
                gasit = True

                brut: float = float(persoana["salar"])
                cas: float = brut * 0.25
                cass: float = brut * 0.10
                impozitare_baza: float = brut - cas - cass
                impozit: float = impozitare_baza * 0.10
                net: float = brut - cas - cass - impozit
                
                nume_fisier: str = "fluturasi_angajati/fluturas_" + cnp + ".json"

                date_fluturas: dict = {
                    "Nume" : persoana['nume'],
                    "Prenume" : persoana['prenume'],
                    "cnp" : persoana['cnp'],
                    "Departament" : persoana['departament'],
                    "Salariu brut" : brut,
                    "Cas (10%)" : round(cas) /2 ,
                    "Cass (25%)" : round(cass) /2,
                    "Impozit (10%)" : round(impozit) /2,
                    "Salariu net" : round(net) /2
                }

                with open(nume_fisier, "w") as my_file:
                    json.dump(date_fluturas, my_file ,indent=4)
                
                print(f"Fisierul JSON pentru angajatul cu CNP-ul {cnp} a fost creat in {nume_fisier}")
                return
            
        if not gasit :
            print(f"Nu s-a gasit nici un angajat cu CNP-ul {cnp}")


def actualizare_fluturas_fisier(persoana: dict) -> None:
    """
    Actualizeaza sau creeaza fisierul JSON cu fluturasul de salariu.
    
    Aceasta functie este folosita intern de alte module pentru a salva
    fluturasul fara interactiune directa cu utilizatorul. Este apelata
    automat dupa:
    - Exportul manual al fluturasului
    - Modificarea datelor unui angajat (daca fisierul exista)
    
    Calculele sunt identice cu cele din calcul_fluturas_salariu:
    - CAS: 25% din brut
    - CASS: 10% din brut
    - Impozit: 10% din baza de calcul
    
    Args:
        persoana (dict): Dictionar cu datele complete ale angajatului.
                        Trebuie sa contina: nume, prenume, cnp, departament, salar.
        
    Returns:
        None: Functia scrie direct in fisierul JSON.
        
    Note:
        - Folderul 'fluturasi_angajati' trebuie sa existe
        - Fisierul este suprascris complet de fiecare data
        - Nu se afiseaza mesaje de confirmare (este o functie interna)
    """
    brut: float = float(persoana["salar"])
    cas: float = brut * 0.25
    cass: float = brut * 0.10
    impozitare_baza: float = brut - cas - cass
    impozit: float = impozitare_baza * 0.10
    net: float = brut - cas - cass - impozit
    cnp: str = persoana["cnp"]

    nume_fisier: str = f"fluturasi_angajati/fluturas_{cnp}.json"

    date_fluturas: dict = {
        "Nume": persoana['nume'],
        "Prenume": persoana['prenume'],
        "CNP": persoana['cnp'],
        "Departament": persoana['departament'],
        "Salariu brut": brut,
        "Cas (25%)": round(cas, 2),
        "Cass (10%)": round(cass, 2),
        "Impozit (10%)": round(impozit, 2),
        "Salariu net": round(net, 2)
    }

    with open(nume_fisier, "w") as my_file:
        json.dump(date_fluturas, my_file, indent=4)


def afisare_fluturas_din_fisier() -> None:
    """
    Citeste si afiseaza continutul unui fluturas de salariu din fisier JSON.
    
    Aceasta functie permite utilizatorului sa vizualizeze fluturasii exportati
    anterior, fara a fi nevoie sa se afle angajatul in baza de date curenta.
    
    Procesul este urmatorul:
    1. Verifica daca folderul 'fluturasi_angajati' exista
    2. Cere CNP-ul angajatului al carui fluturas se doreste
    3. Citeste fisierul JSON corespunzator
    4. Afiseaza toate campurile intr-un format tabelar
    
    Args:
        None: Functia nu primeste parametri, citeste din fisier.
        
    Returns:
        None: Functia afiseaza continutul fisierului in consola.
        
    Note:
        - Utilizatorul poate introduce '0' pentru a reveni la meniu
        - Daca fisierul nu exista, se afiseaza un mesaj de eroare
        - Toate campurile sunt afisate cu numele in uppercase
    """
    print(f"\n--> Afisare fluturas de salariu dintr-un fisier exportat")

    folder: str = "fluturasi_angajati"

    if not os.path.exists(folder):
        print("Nu exista fisiere exportate!")
        return

    while True:

        cnp: str = validari.cere_cnp_valid()

        if cnp == "0":
            return
        
        nume_fisier: str = (f"{folder}/fluturas_{cnp}.json")

        if not os.path.exists(nume_fisier):
            print(f"Nu sa gasit nici un fluturas exportat pentru CNP-u: {cnp}")
            return
        
        print("-" *30)
        print(f" Fluturas salariu din fisierul {nume_fisier}")
        print("-" *30)

        with open(nume_fisier, "r" ) as fluturasi_salariu:

            date: dict = json.load(fluturasi_salariu)

            for camp, valoare in date.items():
                print(f"{camp.upper()}: {valoare}")

        return
