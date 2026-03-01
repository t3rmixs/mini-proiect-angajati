"""
Modulul calculare contine functii pentru operatiuni matematice si calcule
specifice salariilor si departamentelor.

Acest modul este responsabil pentru:
- Calcularea totalurilor de salarii
- Calcularea fluturasului de salariu (brut -> net)
- Filtrarea si calcularea pe departamente
"""

import validari
import exportare


def obtine_total_salarii(angajati: list[dict]) -> float:
    """
    Calculeaza suma totala a salariilor brute ale tuturor angajatilor.
    
    Functia parcurge lista de angajati si insumeaza valoarea campului 'salar'
    pentru fiecare angajat. Rezultatul este returnat ca numar float pentru
    precizie in calculele ulterioare.
    
    Aceasta functie este un helper folosit de alte functii care necesita
    calcularea totalurilor (ex: afiseaza_total_salarii).
    
    Exemple:
        3 angajati cu salarii [4050, 5000, 6000] -> 15050.0
    
    Args:
        angajati (list[dict]): Lista de angajati care contin campul 'salar'.
        
    Returns:
        float: Suma totala a tuturor salariilor din lista.
        
    Note:
        - Functia nu afiseaza nimic, doar returneaza valoarea
        - Salariile sunt convertite la float pentru precizie
        - Lista goala returneaza 0.0
    """
    total: float = 0.0
    for persoana in angajati:
        total += float(persoana['salar'])
    return total

def calcul_total_salarii_departament(angajati: list[dict]) -> None:
    """
    Calculeaza si afiseaza totalul salariilor pentru un departament specific.
    
    Utilizatorul introduce numele departamentului pentru care doreste sa vada
    costul total cu salariile. Functia:
    
    1. Afiseaza toate departamentele disponibile
    2. Cere utilizatorului sa introduca un departament
    3. Parcurge lista si insumeaza salariile angajatilor din acel departament
    4. Afiseaza rezultatul sau un mesaj daca departamentul nu exista
    
    Comparatia departamentelor este case-insensitive.
    
    Args:
        angajati (list[dict]): Lista de angajati pentru calcul.
        
    Returns:
        None: Functia afiseaza rezultatul direct in consola.
        
    Note:
        - Utilizatorul poate crea un departament nou daca nu exista
        - Totalul este calculat pe salariile brute
        - Departamentul este cautat dupa nume exact (dupa convertire la uppercase)
    """
    print("\n--> Calcul total salarii departament ")
    print("-"*30)

    departamente_disponibile: set = set(persoana["departament"] for persoana in angajati)

    cautare_departament: str = input(f"Introduceti un departament -> disponibile {departamente_disponibile}: ").strip().upper()

    total: float = 0
    gasit: bool = False

    for persoane in angajati:
        if persoane["departament"].upper() == cautare_departament:
            total += float(persoane["salar"])
            gasit = True
    if gasit:
        print(f"Costul total pentru departamentul {cautare_departament} este de : {total} RON")
    else:
        print("Departament negasit !")


def calcul_fluturas_salariu(angajati: list[dict]) -> None:
    """
    Calculeaza si afiseaza fluturasul de salariu detaliat pentru un angajat.
    
    Fluturasul include urmatoarele calcule conform legislatiei din Romania:
    - CAS (Contributia Asigurari Sociale): 10% din brut
    - CASS (Contributia Asigurari Sociale Sanatate): 25% din brut
    - Impozit: 10% din baza de calcul (brut - CAS - CASS)
    - Salariu Net: brut - CAS - CASS - Impozit
    
    Dupa afisarea fluturasului, utilizatorul poate alege sa:
    - Exporte datele in format JSON (in folderul 'fluturasi_angajati')
    - Anuleze exportul
    
    Args:
        angajati (list[dict]): Lista de angajati in care se cauta angajatul.
        
    Returns:
        None: Functia afiseaza fluturasul si optional exporta in fisier.
        
    Note:
        - Cautarea se face dupa CNP
        - Utilizatorul poate introduce '0' pentru a reveni la meniu
        - Fisierul exportat poate fi vizualizat ulterior prin optiunea 12 din meniu
    """
    while True:
        print("\n --> Calcul fluturasi salariu")
        cnp: str = validari.cere_cnp_valid()
        if cnp == "0":
            return
        for persoana in angajati:
            if persoana["cnp"] == cnp:
                brut: float = float(persoana["salar"])
                cas: float = brut * 0.10
                cass: float = brut * 0.25
                impozitare_baza: float = brut - cas - cass
                impozit: float = impozitare_baza * 0.10
                net: float = brut - cas - cass - impozit
                print(f"\nFluturas salarial pentru {persoana['nume']} {persoana['prenume']}")
                print(f"Salariu Brut: {brut:.2f} RON")
                print(f"CAS(10%): {cas:.2f} RON")
                print(f"CASS(25%): {cass:.2f} RON")
                print(f"Impozit(10%): {impozit:.2f} RON")
                print(f"Salariu: {net:.2f} RON")

                # intreaba daca utilizatorul vrea sa exporteze fluturasul de salariu
                while True:
                    raspuns: str = input("\nDoriti sa exportati acest fluturas in format JSON (da/nu): ").strip().lower()
                    if raspuns.isalpha() and raspuns == "da":
                        exportare.actualizare_fluturas_fisier(persoana)
                        print(f"Fluturasul a fost salvat in folderul 'fluturasi_angajati' ")
                        break
                    elif raspuns == "nu":
                        print("Exportare a fost anulata!")
                        break
                    else:
                        print("Eroare: Te rugam sa introduci doar (da/nu)")
                return
                             
        print(f"Nu am gasit nici un angajat cu CNP-ul {cnp} , incearca din nou sau '0' pentru meniu")
