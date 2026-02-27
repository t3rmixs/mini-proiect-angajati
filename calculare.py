import validari

# def calcul_total_salarii_companie(angajati):
#     """
#     """
#     print("\n --> Cost Total salarii ")

#     total= 0
#     for persoana in angajati:
#         total += float(persoana["salar"])

#     print(f"Cost total lunar salarii este {total} RON")


def obtine_total_salarii(angajati):
    """
    """
    total = 0.0
    for persoana in angajati:
        total += float(persoana['salar'])
        
    return total

def calcul_total_salarii_departament(angajati):
    """
    """
    print("\n--> Calcul total salarii departament ")
    print("-"*30)

    departamente_disponibile = set(persoana["departament"] for persoana in angajati)
    # if departamente_disponibile:
    #     print("--> Departamente disponibile: ")
    #     for depart in sorted(departamente_disponibile):
    #         print(f"-----> {depart}")
    # else:
    #     print("Nu exista angajati in baza de date!")
    #     return
    cautare_departament = input(f"Introduceti un departament (disponibile {departamente_disponibile}) sau creaza unu nou: ").strip().upper()

    total = 0
    gasit = False

    for persoane in angajati:
        if persoane["departament"].upper() == cautare_departament:
            total += float(persoane["salar"])
            gasit = True
    if gasit:
        print(f"Costul total pentru departamentul {cautare_departament} este de : {total} RON")
    else:
        print("Departament negasit !")


def calcul_fluturas_salariu(angajati):
    """
    """
    while True:
        print("\n --> Calcul fluturasi salariu")
        cnp = validari.cere_cnp_valid()
        if cnp == "0":
            return
        for persoana in angajati:
            if persoana["cnp"] == cnp:
                brut = float(persoana["salar"])
                cas = brut * 0.10
                cass = brut * 0.25
                impozitare_baza = brut - cas - cass
                impozit = impozitare_baza * 0.10
                net = brut - cas - cass - impozit
                print(f"\nFluturas salarial pentru {persoana['nume']} {persoana['prenume']}")
                print(f"Salariu Brut: {brut} RON")
                print(f"CAS(10%): {cas} RON")
                print(f"CASS(25%): {cass} RON")
                print(f"Impozit(10%): {impozit} RON")
                print(f"Salariu: {net} RON")
                return
            
            
        print(f"Nu am gasit nici un angajat cu CNP-ul {cnp} , inceacra din nou sau '0' pentru meniu")
