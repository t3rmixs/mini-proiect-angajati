"""
Modulul operatiuni_date contine toate functiile pentru operatiunile CRUD
(Create, Read, Update, Delete) asupra datelor angajatilor.

Acesta este modulul principal de interactiune cu datele, fiind apelat
din meniul principal al aplicatiei.
"""

import os
import json
import exportare
import validari
import incarcare_salvare
import calculare


def adaugare_angajat(angajati: list[dict]) -> None:
    """
    Adauga un angajat nou in baza de date a companiei.
    
    Procesul de adaugare include urmatoarele etape:
    1. Validarea CNP-ului (unicitate si format corect)
    2. Introducerea si validarea numelui si prenumelui
    3. Introducerea si validarea varstei (minim 18 ani)
    4. Introducerea si validarea salariului (minim salariu minim legal)
    5. Selectarea sau crearea unui departament
    6. Selectarea nivelului de senioritate (junior/mid/senior)
    7. Salvarea datelor in fisierul JSON
    
    Functia verifica daca CNP-ul exista deja in baza de date pentru a evita
    duplicatele. Daca CNP-ul este deja inregistrat, operatiunea este anulata.
    
    Args:
        angajati (list[dict]): Lista curenta de angajati la care se adauga noul angajat.
        
    Returns:
        None: Functia modifica lista 'angajati' in-place si salveaza in fisier.
        
    Note:
        - Utilizatorul poate introduce '0' la CNP pentru a anula operatiunea
        - Datele sunt salvate automat dupa adaugarea cu succes
        - Toate input-urile sunt validate inainte de a fi acceptate
    """
    print("\n ---> Adagua un angajat ")

    cnp: str = validari.cere_cnp_valid()
    if cnp == "0":
        return "0"

    for persoana in angajati:
        if persoana["cnp"] == cnp:
            print(f"Eroare: Acest {cnp} CNP a fost deja introdus pentru alta persoana")
            return
    
    while True:
        nume: str = input("Nume: ").capitalize()
        if validari.validare_nume(nume):
            nume = nume.capitalize()
            break
    
    while True:
        prenume: str = input("Prenume: ").strip()
        if validari.validare_nume(prenume):
            prenume = prenume.title()
            break

    while True:
        varsta: str = input("Varsta necsara >18: ")
        if validari.varsta_validare(varsta):
            break
        print("Eroare: Varsta trebuie sa fie numerica si > 18 ani.")

    while True:
        salar: str = input("Salariu Brut (minim 4050): ")
        if validari.salariu_validare(salar):
            break
        print(f"Eroare: Salariu trebuie sa fie mai mare de {validari.salariu_minim} RON.")
    
    departamente_disponibile: set = set(persoana["departament"] for persoana in angajati)
    departament: str = input(f"Departament (disponibile {departamente_disponibile} ) sau creaza unul nou: ").strip().upper()

    while True:
        senioritate: str = input(f"Senerioaritate (acceptate {validari.aceptare_nivel}): ").lower()
        if validari.senior_validare(senioritate):
            break
        print(f"Eroare: Senioritatea trebuie sa fie (disponibile {validari.aceptare_nivel}) .")

    angajat_nou: dict = {
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta": int(varsta),
        "salar": float(salar),
        "departament": departament,
        "senioritate": senioritate
    }
    angajati.append(angajat_nou)
    
    if incarcare_salvare.salveaza_fisier_angajati(angajati):
        print("-"*30)
        print(f"Angajatul {angajat_nou['nume']} {angajat_nou['prenume']} a fost adaugat cu success!")
    else: 
        print("Nu s-a putut salva !")



def cautare_angajat(angajati: list[dict]) -> None:
    """
    Cauta si afiseaza datele complete ale unui angajat pe baza CNP-ului.
    
    Functia parcurge lista de angajati si compara CNP-ul introdus cu CNP-ul
    fiecarui angajat. La gasirea unei potriviri, afiseaza toate informatiile:
    - Nume complet
    - CNP
    - Varsta
    - Salariu brut
    - Departament
    - Nivel de senioritate
    
    Args:
        angajati (list[dict]): Lista de angajati in care se face cautarea.
        
    Returns:
        None: Functia afiseaza rezultatele direct in consola.
        
    Note:
        - Cautarea este exacta (CNP-ul trebuie sa match-eze perfect)
        - Utilizatorul poate introduce '0' pentru a reveni la meniu
        - Daca nu se gaseste angajatul, se afiseaza un mesaj de eroare
    """
    print("\n ---> Cauta angajat ")

    while True:
        cnp: str = validari.cere_cnp_valid()
        if cnp == "0":
            return

        gasit: bool = False
        for persoana in angajati: 
            if persoana["cnp"] == cnp:
                print(f"\nDate gasite pentru : '{persoana['nume']} {persoana['prenume']}'")
                print(f"CNP: {persoana['cnp']}")
                print(f"Varsta: {persoana['varsta']}")
                print(f"Salariu: {persoana['salar']} RON")
                print(f"Departament: {persoana['departament']}")
                print(f"Senioritate: {persoana['senioritate']}")
                gasit = True
                return
        if not gasit:
            print(f"CNP-ul {cnp} nu a fost gasit!")
    

def modificare_angajat(angajati: list[dict]) -> None:
    """
    Permite modificarea oricaror date ale unui angajat existent.
    
    Utilizatorul poate actualiza urmatoarele campuri (optional):
    - CNP (cu actualizarea fisierului fluturas asociat)
    - Nume
    - Prenume
    - Varsta
    - Salariu
    - Departament
    - Senioritate
    
    Pentru fiecare camp, utilizatorul poate:
    - Introduce o valoare noua
    - Apasa ENTER pentru a pastra valoarea existenta
    
    Daca CNP-ul este modificat, fisierul JSON al fluturasului de salariu
    este redenumit pentru a reflecta noul CNP.
    
    Args:
        angajati (list[dict]): Lista de angajati care contine angajatul de modificat.
        
    Returns:
        None: Functia modifica datele in-place si salveaza in fisier.
        
    Note:
        - Toate noile valori sunt validate inainte de a fi acceptate
        - CNP-ul nou trebuie sa fie unic (nu poate apartine altui angajat)
        - Modificarile sunt salvate automat in fisierul JSON
        - Fisierul fluturas este actualizat daca exista
    """
    print("--> Modifica un angajat")
    while True:
        cnp: str = validari.cere_cnp_valid()
        if cnp == "0":
            return
        for persoana in angajati:
            if persoana["cnp"] == cnp:

                print(f"----> Mofica datele pentru '{persoana['nume']} {persoana['prenume']}'")

                cnp_vechi: str = persoana["cnp"]
                cnp_nou: str = input("Introdu un cnp nou sau apasa 'enter' pentru a-l pastra: ").strip()

                if cnp_nou:
                    while not validari.cnp_validare(cnp_nou):
                        cnp_nou = input("Introdu un cnp nou valid sau apasa 'enter' pentru a-l pastra: ").strip()
                        if not cnp_nou:
                            break
                    if cnp_nou:
                        toate_cnpuriile: list = [persoana["cnp"] for persoana in angajati]
                        if cnp_nou in toate_cnpuriile:
                            print(f"Eroare: CNP-ul '{cnp_nou}' apartine deja a altui angajat! ")
                        else:
                            persoana["cnp"] = cnp_nou

                            cale_veche: str = f"fluturasi_angajati/fluturas_{cnp_vechi}.json"
                            cale_noua: str = f"fluturasi_angajati/fluturas_{cnp_nou}.json"

                            if os.path.exists(cale_veche):
                                with open (cale_veche, "r") as my_file:
                                    date_fluturas: dict = json.load(my_file)

                                date_fluturas["cnp"] = cnp_nou
                                
                                with open(cale_noua, "w") as my_file:
                                    json.dump(date_fluturas, my_file, indent=4)

                                os.remove(cale_veche)
                                print(f" Fisierul fluturas a fost redenumit din '{cnp_vechi}' in '{cnp_nou}' ")


                nume_nou: str = input("Introdu un nume nou sau apasa 'enter' pentru a-l pastra: ").strip().title()
                if nume_nou:
                    while not validari.validare_nume(nume_nou):
                        nume_nou = input("Introdu un nume nou valid sau apasa 'enter' pentru a-l pastra: ").strip().title()
                        if not nume_nou:
                            break
                    if nume_nou:
                        persoana["nume"] = nume_nou.title()


                prenume_nou: str = input("Introdu un prenume nou sau apasa 'enter' pentru a-l pastra: ").strip().title()
                if prenume_nou:
                    while not validari.validare_nume(prenume_nou):
                        prenume_nou = input("Introdu un prenume nou valid sau apasa 'enter' pentru a-l pastra: ").strip().title()
                        if not prenume_nou:
                            break
                    if prenume_nou:
                        persoana["prenume"] = prenume_nou.title()


                varsta_noua: str = input("Introdu o varsta noua sau apasa 'enter' pentru a-l pastra: ")
                if varsta_noua:
                    while not validari.varsta_validare(varsta_noua):
                        varsta_noua = input("Introdu o varsta noua sau apasa 'enter' pentru a-l pastra: ")
                        if not varsta_noua:
                            break
                    if varsta_noua:
                        persoana["varsta"] = int(varsta_noua)
                
                salariu_nou: str = input(f"Introdu un salariu nou (minim {validari.salariu_minim}) sau apasa 'enter' pentru a-l pastra: ")
                if salariu_nou:
                    while not validari.salariu_validare(salariu_nou):
                        salariu_nou = input(f"Introdu un salariu nou (minim {validari.salariu_minim}) sau apasa 'enter' pentru a-l pastra: ")
                        if not salariu_nou:
                            break
                    if salariu_nou:
                        persoana["salar"] = float(salariu_nou)
                

                departamente_disponibile: set = set(persoana["departament"] for persoana in angajati)

                departament_nou: str = input(f"Introdu un departament nou (disponibile {departamente_disponibile}) sau creaza unu nou: ").strip().upper()
                if departament_nou:
                    while not validari.departament_validare(departament_nou):
                        departament_nou = input(f"Introdu un departament nou (disponibile {departamente_disponibile}) sau creaza unu nou: ").strip().upper()
                        if not departament_nou:
                            break
                    if departament_nou:
                        persoana["departament"] = departament_nou
                
                senioritate_noua: str = input(f"Introdu o senioritate noua (disponibile {validari.aceptare_nivel}) sau apasa 'enter' pentru a-l pastra: ").strip().lower()
                if senioritate_noua:
                    while not validari.senior_validare(senioritate_noua):
                        senioritate_noua = input(f"Introdu o senioritate noua (disponibile {validari.aceptare_nivel}) sau apasa 'enter' pentru a-l pastra : ").strip().lower()
                        if not senioritate_noua:
                            break
                    if senioritate_noua:
                        persoana["senioritate"] = senioritate_noua

                if incarcare_salvare.salveaza_fisier_angajati(angajati):
                    print("-"*30)
                    print(f"Datele pentru angajatul '{persoana['nume']} {persoana['prenume']}' au fost salvate cu success!")
            
                    #incearca sa salvezi in fluturas daca exista 
                    cale_fluturas: str = f"fluturasi_angajati/fluturas_{persoana['cnp']}.json"
                    if os.path.exists(cale_fluturas):
                        exportare.actualizare_fluturas_fisier(persoana)
                        print(f"Fluturasul a fost actualizat pentru fostul CNP-ul '{cnp}' in noul CNP : {cnp_nou} ")
                    return
        print(f"Nu s-a gasit nici un angajat cu CNP-ul: '{cnp}' ")


def sterge_angajat(angajati: list[dict]) -> None:
    """
    Sterge un angajat din baza de date dupa confirmarea utilizatorului.
    
    Procesul de stergere include:
    1. Cautarea angajatului dupa CNP
    2. Afisarea numelui angajatului pentru confirmare
    3. Cererea de confirmare explicita (da/nu)
    4. Optional: stergerea fisierului fluturas asociat
    5. Salvarea modificarii in fisierul JSON
    
    Functia protejeaza impotriva stergerilor accidentale prin:
    - Cererea de confirmare explicita
    - Afisarea numelui complet inainte de stergere
    - Optiunea de a pastra fisierul fluturas daca se doreste
    
    Args:
        angajati (list[dict]): Lista de angajati din care se sterge angajatul.
        
    Returns:
        None: Functia modifica lista in-place si salveaza in fisier.
        
    Note:
        - Utilizatorul poate introduce '0' pentru a anula operatiunea
        - Fisierul fluturas poate fi sters sau pastrat la alegere
        - Dupa stergere, datele nu mai pot fi recuperate
    """
    print("--> Sterge un angajat")

    while True:
        cnp: str = validari.cere_cnp_valid()

        if cnp == "0":
            return "0"
        
        gasit: bool = False

        for index, angajat in enumerate(angajati):
            if angajat['cnp'] == cnp:
                gasit = True

                while True:
                    confirmare: str = input(f"Sigur doriti sa stergeti angajatul '{angajat['nume']} {angajat['prenume']}' (da/nu): ").strip().lower()
                    if confirmare.lower() == "da":

                        fluturas_fisier: str = f"fluturasi_angajati/fluturas_{cnp}.json"

                        if os.path.exists(fluturas_fisier):
                            sterge_fluturas: str = input("Fluturas gasit , vrei sa stergi acest fisier? (da/nu): ").strip().lower()
                            if sterge_fluturas == "da":
                                os.remove(fluturas_fisier)
                                print("-"*30)
                                print(f"Fluturasul pentru '{angajat['nume']} {angajat['prenume']}' cu CNP-ul {angajat['cnp']} a fost sters.")
                            else:
                                print(f"Fisierul a ramas inca pe disk tu ai ales {sterge_fluturas}")

                        angajati.pop(index)
                        if incarcare_salvare.salveaza_fisier_angajati(angajati):
                            print("-"*30)
                            print(f"Angajatul '{angajat['nume']} {angajat['prenume']}' sters cu success!")
                        else:
                            print("Eroare la salvare!")
                        return
                    elif confirmare == "nu":
                        print(f"Operatiune oprita!")
                        break
                    else:
                        print(f"Eroare: Intodu (da/nu) tu ai introdus '{confirmare}' Incearca din nou sau apasa '0' pentru meniu")
        if not gasit:        
            print(f"Nu s-a gasit nici un angajat cu CNP-ul '{cnp}' \n")


def afisare_toti_angajatii(angajati: list[dict]) -> None:
    """
    Afiseaza o lista sumara cu toti angajatii din companie.
    
    Pentru fiecare angajat sunt afisate:
    - Numele complet (nume + prenume)
    - CNP
    - Departament
    - Nivel de senioritate
    
    La inceputul listei este afisat numarul total de angajati.
    
    Args:
        angajati (list[dict]): Lista de angajati de afisat.
        
    Returns:
        None: Functia afiseaza rezultatele direct in consola.
        
    Note:
        - Daca lista este goala, se afiseaza un mesaj informativ
        - Formatul este compact pentru a permite vizualizarea rapida
    """

    print(f"\n --> Lista de angajati | Total de  [ {len(angajati)} ] angajati in companie")

    if not angajati:
        print("Nu exista nici un angajat")
        return
    
    for persoane in angajati:
        print(f"{persoane['nume']} {persoane['prenume']} | CNP: {persoane['cnp']} | Departament: {persoane['departament']} | Senioritate: {persoane['senioritate']}" )


def afiseaza_total_salarii(angajati: list[dict]) -> None:
    """
    Calculeaza si afiseaza costul total lunar cu salariile pentru toti angajatii.
    
    Functia insumeaza salariile brute ale tuturor angajatilor din lista
    si afiseaza rezultatul intr-un format usor de citit.
    
    Aceasta informatie este utila pentru:
    - Bugetarea lunara a companiei
    - Planificarea financiara
    - Raportari catre management
    
    Args:
        angajati (list[dict]): Lista de angajati pentru calcul.
        
    Returns:
        None: Functia afiseaza rezultatul direct in consola.
        
    Note:
        - Calculul este facut pe salariile brute (inainte de taxe)
        - Functia foloseste helper-ul din modulul calculare
    """  
    print("-"*30)
    total: float = calculare.obtine_total_salarii(angajati)
    print(f"Cost total lunar salarii este {total} RON")


def afiseaza_dupa_senioritate(angajati: list[dict]) -> None:
    """
    Filtreaza si afiseaza angajatii pe baza nivelului de senioritate.
    
    Utilizatorul poate selecta unul dintre nivelurile disponibile:
    - junior: angajati la inceput de drum
    - mid: angajati cu experienta medie
    - senior: angajati cu experienta avansata
    
    Functia afiseaza doar angajatii care corespund nivelului selectat,
    impreuna cu informatii despre departamentul lor.
    
    Args:
        angajati (list[dict]): Lista de angajati pentru filtrare.
        
    Returns:
        None: Functia afiseaza rezultatele direct in consola.
        
    Note:
        - Utilizatorul poate introduce '0' pentru a reveni la meniu
        - Daca nu exista angajati pe nivelul selectat, se afiseaza un mesaj
        - Comparatia este case-insensitive
    """
    print("\n--> Angajati dupa senioritate")
    while True:

        nivel: str = input(f"Ce nivel cauti, disponibile -> {validari.aceptare_nivel}  sau '0' pentru meniu: ").lower()
        if nivel == "0":
            return
        
        if not validari.senior_validare(nivel):
            print(f"Nivel invalid nivele disponibile {validari.aceptare_nivel}")
            continue
        break

    gasit: bool = False
        
    for persoana in angajati:
        if persoana["senioritate"].lower() == nivel:
            print("-"*40)
            print(f"\n Angajatul : {persoana['nume']} {persoana['prenume']} este '{persoana['senioritate']}' in departamentul '{persoana['departament']}' ")
            gasit = True

    if not gasit:
        print(f"Nu exista nici un angajat pe nivelul '{nivel}'")
    
def afisare_dupa_departament(angajati: list[dict]) -> None:
    """
    Filtreaza si afiseaza angajatii pe baza departamentului din care fac parte.
    
    La inceput sunt afisate toate departamentele disponibile pentru a ajuta
    utilizatorul sa aleaga corect. Comparatia este case-insensitive.
    
    Pentru fiecare angajat gasit sunt afisate:
    - Numele complet
    - Departament
    - Nivel de senioritate
    
    Args:
        angajati (list[dict]): Lista de angajati pentru filtrare.
        
    Returns:
        None: Functia afiseaza rezultatele direct in consola.
        
    Note:
        - Departamentele sunt afisate intr-un set (fara duplicate)
        - Input-ul este convertit la uppercase pentru comparatie
        - Daca departamentul nu exista, se afiseaza un mesaj informativ
    """
    print("\n---> Afisare dupa departament")
    print("-"*30)

    departamente_disponibile: set = set(persoana["departament"] for persoana in angajati)

    departament_cautat: str = input(f"Introdu un departament , disponibile -> {departamente_disponibile} : ").strip().upper()
    gasit: bool = False
    for persoana in angajati:
        if persoana["departament"].upper() == departament_cautat:
            print(f" {persoana['nume']} {persoana['prenume']} | {persoana['departament']} | {persoana['senioritate']}")
            gasit = True

    if not gasit:
        print(f"Nu exista nici un angajat in departamentul '{departament_cautat}'")