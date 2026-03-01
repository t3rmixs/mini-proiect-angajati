"""
Modulul main este punctul de intrare principal al aplicatiei de gestionare a angajatilor.

Acest modul:
- Incarca datele angajatilor la pornire
- Afiseaza meniul principal cu toate optiunile
- Dirijeaza utilizatorul catre functiile corespunzatoare in functie de alegere
- Salveaza datele la iesirea din aplicatie

Structura aplicatiei este modulara, fiecare functionalitate fiind
implementata in module separate pentru o mai buna organizare.
"""

import operatiuni_date
import incarcare_salvare
import calculare
import incarcare_salvare
import exportare

def afisare_meniu() -> None:
    """
    Afiseaza meniul principal al aplicatiei cu toate optiunile disponibile.
    
    Meniul contine 13 optiuni (0-12) grupate logic:
    
    Gestionare angajati (1-5):
    - Adaugare, cautare, modificare, stergere, afisare toti
    
    Calcule si rapoarte (6-10):
    - Total salarii companie/departament
    - Fluturas salariu
    - Filtrare dupa senioritate/departament
    
    Export/Import (11-12):
    - Export fluturas JSON
    - Afisare fluturas din fisier
    
    Iesire (0):
    - Inchiderea aplicatiei
    
    Returns:
        None: Functia afiseaza meniul direct in consola.
        
    Note:
        - Meniul este afisat la fiecare iteratie a buclei principale
        - Liniile de separare (-) ajuta la lizibilitate
        - Numerotarea incepe de la 0 pentru consistenta cu input-ul
    """
    print("-"*30)
    print(" --> Gestioneaza compania ")
    print("-"*30)
    print("0. Iesire")  
    print("1. Adauga angajat")
    print("2. Cautare angajat (dupa CNP)")
    print("3. Modificare angajat (dupa CNP)")
    print("4. Sterge un angajat (dupa CNP)")
    print("5. Afisare toti angajatii")
    print("6. Calcul cost total salarii companie")
    print("7. Calcul cost total salarii pe departament")
    print("8. Calcul fluturas salariar (dupa CNP)")
    print("9. Afisare angajati pe baza senioritatii")
    print("10. Afisare angajati pe baza departamentului")
    print("11. Export fluturas salariu")
    print("12. Afisare fluturas din fisier")
    print("-"*40)

def main() -> None:
    """
    Functia principala a aplicatiei care coordoneaza intreaga executie.
    
    Fluxul de executie este urmatorul:
    
    1. INCARCARE DATE:
       - Se incarca angajatii din fisierul JSON (daca exista)
       - Lista goala daca este prima rulare
    
    2. BUCLA PRINCIPALA:
       - Afiseaza meniul
       - Cere optiunea de la utilizator
       - Valideaza input-ul (trebuie sa fie numar intre 0-12)
       - Executa functia corespunzatoare optiunii alese
    
    3. IESIRE:
       - La optiunea 0, bucla se intrerupe
       - Mesaj de confirmare la inchidere
    
    Validarea input-ului include:
    - Verificarea daca este numar intreg
    - Verificarea daca este in intervalul 0-12
    - Mesaje de eroare descriptive pentru input invalid
    
    Returns:
        None: Functia ruleaza pana la iesirea utilizatorului.
        
    Note:
        - Functia este apelata doar daca fisierul este rulat direct
        - Toate erorile de input sunt prinse si tratate graceful
        - Datele sunt salvate automat dupa fiecare modificare
    """
    lista_angajati: list[dict] = incarcare_salvare.incarca_fisier_angajati()
    
    while True:
        afisare_meniu()
        alege: str = input("Alege o optiune de la 0-12: ").strip()
        
        try:
            alege_numar: int = int(alege)

            if alege_numar < 0 or alege_numar > 12:
                print(f"Eroare: Numarul trebuie sa fie intre 1-12 , tu ai ales {alege_numar}")
                continue
        except ValueError:
            print(f"Eroare: Trebuie sa introduceti un numar valid (ai introdus '{alege}')")
            continue

        if alege == "0":
            print(f"Program inchis, ai ales '{alege}' ")
            break
        elif alege == "1":
            operatiuni_date.adaugare_angajat(lista_angajati)
        elif alege == "2":
            operatiuni_date.cautare_angajat(lista_angajati)
        elif alege == "3":
            operatiuni_date.modificare_angajat(lista_angajati)
        elif alege == "4":
            operatiuni_date.sterge_angajat(lista_angajati)
        elif alege == "5":
            operatiuni_date.afisare_toti_angajatii(lista_angajati)
        elif alege == "6":
            operatiuni_date.afiseaza_total_salarii(lista_angajati)
        elif alege == "7":
            calculare.calcul_total_salarii_departament(lista_angajati)
        elif alege == "8":
            calculare.calcul_fluturas_salariu(lista_angajati)
        elif alege == "9":
            operatiuni_date.afiseaza_dupa_senioritate(lista_angajati)
        elif alege == "10":
            operatiuni_date.afisare_dupa_departament(lista_angajati)
        elif alege == "11":
            exportare.exporteaza_fluturas(lista_angajati)
        elif alege == "12":
            exportare.afisare_fluturas_din_fisier()  

if __name__ == "__main__":
    main()