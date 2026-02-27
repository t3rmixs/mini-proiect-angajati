# exporteaza fluturasii de salariu intrun folder dupa care sa ii poti afisa in consola dupa CNP

import os
import validari
import json

def exporteaza_fluturas(angajati):
    """
    """
    print("\n-- Export fluturasi de salar")

    
    
    while True:
        cnp = validari.cere_cnp_valid()
           
        if cnp == "0":
            return
        
        gasit = False
        for persoana in angajati:
            if persoana["cnp"] == cnp:
                gasit = True

                brut = float(persoana["salar"])
                cas = brut * 0.10
                cass = brut * 0.25
                impozitare_baza = brut - cas - cass
                impozit = impozitare_baza * 0.10
                net = brut - cas - cass - impozit
                
                nume_fisier = "fluturasi_angajati/fluturas_" + cnp + ".json"

                date_fluturas = {
                    "Nume" : persoana['nume'],
                    "Prenume" : persoana['prenume'],
                    "CNP" : persoana['cnp'],
                    "Departament" : persoana['departament'],
                    "Salariu brut" : brut,
                    "Cas (10%)" : round(cas) /2 ,
                    "Cass (25%)" : round(cass) /2,
                    "Impozit (10%)" : round(impozit) /2,
                    "Salariu net" : round(net) /2

                }
                # date_fluturas = {
                #     "nume" : persoana['nume'],
                #     "prenume" : persoana['prenume'],
                #     "cnp" : persoana['cnp'],
                #     "departament" : persoana['departament'],
                #     "salariu brut" : brut,
                #     "cas" : round(cas) /2 ,
                #     "cass" : round(cass) /2,
                #     "impozit" : round(impozit) /2,
                #     "salariu net" : round(net) /2

                # }

                with open(nume_fisier, "w") as my_file:
                    json.dump(date_fluturas, my_file ,indent=4)
                
                print(f"Fisierul JSON pentru angajatul cu CNP-ul {cnp} a fost creat in {nume_fisier}")
                return
            
        if not gasit :
            print(f"Nu s-a gasit nici un angajat cu CNP-ul {cnp}")

                # with open(nume_fisier, "w") as my_file:
                #     my_file.write(f"Nume: {persoana['nume']}\n")
                #     my_file.write(f"Prenume: {persoana['prenume']}\n")
                #     my_file.write(f"CNP: {persoana['cnp']}\n")
                #     my_file.write(f"Departament: {persoana['departament']}\n")
                #     my_file.write(f"Salariu Brut: {brut}\n")
                #     my_file.write(f"CAS (10%): {cas}\n")
                #     my_file.write(f"CASS (25%): {cass}")
                #     my_file.write(f"Impozit (10%): {impozit}\n")
                #     my_file.write(f"Salariu Net: {net}\n")
                # print(f"Fisier creat cu success : {nume_fisier}\n") 
                # return

        # if not gasit:
        #     print(f"Nu sa gasit nici un angajat cu CNP-ul {cnp}")


def afisare_fluturas_din_fisier():
    """
    """
    print(f"\n--> Afisare fluturas de salariu dintr-un fisier exportat")

    folder = "fluturasi_angajati"

    if not os.path.exists(folder):
        print("Nu exista fisiere exportate!")
        return
     


    while True:

        cnp = validari.cere_cnp_valid()

        if cnp == "0":
            return
        
        nume_fisier = (f"{folder}/fluturas_{cnp}.json")

        if not os.path.exists(nume_fisier):
            print(f"Nu sa gasit nici un fluturas exportat pentru CNP-u: {cnp}")
            return
        
        print("-" *30)
        print(f" Fluturas salariu din fisierul {nume_fisier}")
        print("-" *30)

        with open(nume_fisier, "r" ) as fluturasi_salariu:

            date = json.load(fluturasi_salariu)

            for camp, valoare in date.items():
                print(f"{camp.upper()}: {valoare}")

        print("-"*30)
        return
    
            # continut = my_file.read()

            # for linie in continut.split("\n"):
            #     camp, valoare = linie.split(":", 1)
            #     print(f" {camp}: {valoare}")
        
        print("-" *30)
        print("Fisierul a fost gasit ")