import validari
import incarcare_salvare
import calculare


def adaugare_angajat(angajati):
    """
    """
    print("\n ---> Adagua un angajat ")

    cnp = validari.cere_cnp_valid()
    for persoana in angajati:
        if persoana["cnp"] == cnp:
            print(f"Eroare: Acest {cnp} CNP a fost deja introdus pentru alta persoana")
            return
    
    while True:
        nume = input("Nume: ").capitalize()
        if validari.validare_nume(nume):
            nume = nume.capitalize()
            break
    
    while True:
        prenume = input("Prenume: ").strip()
        if validari.validare_nume(prenume):
            prenume = prenume.title()
            break

    while True:
        varsta = input("Varsta necsara >18: ")
        if validari.varsta_validare(varsta):
            break
        print("Eroare: Varsta trebuie sa fie numerica si > 18 ani.")

    while True:
        salar = input("Salariu Brut (minim 4050): ")
        if validari.salariu_validare(salar):
            break
        print(f"Eroare: Salariu trebuie sa fie mai mare de {validari.salariu_minim} RON.")
    
    departamente_disponibile = set(persoana["departament"] for persoana in angajati)
    departament = input(f"Departament (disponibile {departamente_disponibile} ) sau creaza unul nou: ").strip().upper()

    while True:
        senioritate = input(f"Senerioaritate (acceptate {validari.aceptare_nivel}): ").lower()
        if validari.senior_validare(senioritate):
            break
        print(f"Eroare: Senioritatea trebuie sa fie (disponibile {validari.aceptare_nivel}) .")

    angajat_nou = {
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
        print("Nu sa putut salva !")



def cautare_angajat(angajati):
    """
    """
    print("\n ---> Cauta angajat ")

    while True:
        cnp = validari.cere_cnp_valid()
        if cnp == "0":
            return

        gasit = False
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
    

def modificare_angajat(angajati):
    print("--> Modifica un angajat")
    while True:
        cnp = validari.cere_cnp_valid()
        if cnp == "0":
            return
        for persoana in angajati:
            if persoana["cnp"] == cnp:

                print(f"----> Mofica datele pentru '{persoana['nume']} {persoana['prenume']}'")

                cnp_nou = input("Introdu un cnp nou sau apasa 'enter' pentru a il pastra: ").strip()
                if cnp_nou:
                    while not validari.cnp_validare(cnp_nou):
                        cnp_nou = input("Introdu un cnp nou valid sau apasa 'enter' pentru a il pastra: ").strip()
                        if not cnp_nou:
                            break
                    if cnp_nou:
                        persoana["cnp"] = cnp_nou

                nume_nou = input("Introdu un nume nou sau apasa 'enter' pentru a il pastra: ").strip().title()
                if nume_nou:
                    while not validari.validare_nume(nume_nou):
                        nume_nou = input("Introdu un nume nou valid sau apasa 'enter' pentru a il pastra: ").strip().title()
                        if not nume_nou:
                            break
                    if nume_nou:
                        persoana["nume"] = nume_nou.title()


                prenume_nou = input("Introdu un prenume nou sau apasa 'enter' pentru a il pastra : ").strip().title()
                if prenume_nou:
                    while not validari.validare_nume(prenume_nou):
                        prenume_nou = input("Introdu un prenume nou valid sau apasa 'enter' pentru a il pastra: ").strip().title()
                        if not prenume_nou:
                            break
                    if prenume_nou:
                        persoana["prenume"] = prenume_nou.title()


                varsta_noua = input("Introdu o varsta noua sau apasa 'enter' pentru a il pastra: ")
                if varsta_noua:
                    while not validari.varsta_validare(varsta_noua):
                        varsta_noua = input("Introdu o varsta noua sau apasa 'enter' pentru a il pastra: ")
                        if not varsta_noua:
                            break
                    if varsta_noua:
                        persoana["varsta"] = int(varsta_noua)
                
                salariu_nou = input(f"Introdu un salariu nou (minim {validari.salariu_minim}) sau apasa 'enter' pentru a il pastra: ")
                if salariu_nou:
                    while not validari.salariu_validare(salariu_nou):
                        salariu_nou = input(f"Introdu un salariu nou (minim {validari.salariu_minim}) sau apasa 'enter' pentru a il pastra: ")
                        if not salariu_nou:
                            break
                    if salariu_nou:
                        persoana["salar"] = float(salariu_nou)
                

                departamente_disponibile = set(persoana["departament"] for persoana in angajati)

                departament_nou = input(f"Introdu un departament nou (disponibile {departamente_disponibile}) sau creaza unu nou: ").strip().upper()
                if departament_nou:
                    while not validari.departament_validare(departament_nou):
                        departament_nou = input(f"Introdu un departament nou (disponibile {departamente_disponibile}) sau creaza unu nou: ").strip().upper()
                        if not departament_nou:
                            break
                    if departament_nou:
                        persoana["departament"] = departament_nou
                
                senioritate_noua = input(f"Introdu o senioritate noua (disponibile {validari.aceptare_nivel}) sau apasa 'enter' pentru a il pastra: ").strip().lower()
                if senioritate_noua:
                    while not validari.senior_validare(senioritate_noua):
                        senioritate_noua = input(f"Introdu o senioritate noua (disponibile {validari.aceptare_nivel}) sau apasa 'enter' pentru a il pastra : ").strip().lower()
                        if not senioritate_noua:
                            break
                    if senioritate_noua:
                        persoana["senioritate"] = senioritate_noua

                if incarcare_salvare.salveaza_fisier_angajati(angajati):
                    print(f"Datele pentru angajatul '{persoana['nume']} {persoana['prenume']}' au fost salvate cu success!")
                return
        print(f"Nu sa gasit nici un angajat cu CNP-ul '{cnp}' ")

def sterge_angajat(angajati):
    """
    """
    print("--> Sterge un angajat")

    while True:
        cnp = validari.cere_cnp_valid()

        if cnp == "0":
            return
        gasit = False

        for persoana, angajat in enumerate(angajati):
            if angajat['cnp'] == cnp:
                gasit = True

                while True:
                    confirmare = input(f"Sigur doriti sa stergeti angajatul '{angajat['nume']} {angajat['prenume']}' (da/nu): ").strip().lower()
                    if confirmare.lower() == "da":
                        angajati.pop(persoana)
                        if incarcare_salvare.salveaza_fisier_angajati(angajati):
                            print(f"Angajatul '{angajat['nume']} {angajat['prenume']}' sters cu success!")
                        else:
                            print("Eroare la salvare!")
                        return
                    elif confirmare == "nu":
                        print(f"Operatiune oprita!")
                        break
                    else:
                        print(f"Eroare: Intodu (da/nu) tu ai introdus '{confirmare}' Inceacra din nou sau apasa '0' pentru meniu")
        if not gasit:        
            print(f"Nu sa gasit nici un angajat cu CNP-ul '{cnp}' \n")

def afisare_toti_angajatii(angajati):
    """
    """

    print(f"\n --> Lista de angajati | Total de [{len(angajati)}] angajati")

    if not angajati:
        print("Nu exista nici un angajat")
        return
    
    for persoane in angajati:
        print(f"{persoane['nume']} {persoane['prenume']} | CNP: {persoane['cnp']} | Departament: {persoane['departament']} | Senioritate: {persoane['senioritate']}" )


def afiseaza_total_salarii(angajati):
    print("-"*30)
    total = calculare.obtine_total_salarii(angajati)
    print(f"Cost total lunar salarii este {total} RON")

def afiseaza_dupa_senioritate(angajati):
    """
    """
    print("\n--> Angajati dupa senioritate")
    while True:

        nivel = input(f"Ce nivel cauti (disponibile {validari.aceptare_nivel}) sau '0' pentru meniu: ").lower()
        if nivel == "0":
            return
        
        if not validari.senior_validare(nivel):
            print(f"Nivel invalid nivele disponibile {validari.aceptare_nivel}")
            continue
        break

    gasit = False
        
    for persoana in angajati:
        if persoana["senioritate"].lower() == nivel:
            print("-"*40)
            print(f"\n Angajatul : {persoana['nume']} {persoana['prenume']} in departamentul - {persoana['departament']} - {persoana['senioritate']}")
            gasit = True

    if not gasit:
        print(f"Nu exista nici un angajat pe nivelul '{nivel}'")
    
def afisare_dupa_departament(angajati):
    """
    """
    print("\n---> Afisare dupa departament")
    print("-"*30)

    departamente_disponibile = set(persoana["departament"] for persoana in angajati)

    departament_cautat = input(f"Introdu un departament (disponibile {departamente_disponibile}): ").strip().upper()
    gasit = False
    for persoana in angajati:
        if persoana["departament"].upper() == departament_cautat:
            print(f" {persoana['nume']} {persoana['prenume']} | {persoana['departament']} |{persoana['senioritate']}")
            gasit = True

    if not gasit:
        print(f"Nu exista angajati in departamentul {departament_cautat}")