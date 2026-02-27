import operatiuni_date
import incarcare_salvare
import calculare
import incarcare_salvare
import exportare

def afisare_meniu():
    """
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

def main():
    """
    """
    lista_angajati = incarcare_salvare.incarca_fisier_angajati()

    while True:
        afisare_meniu()
        alege = input("Alege o optiune de la 0-12: ")
        
        try:
            alege_numar = (int(alege))

            if alege_numar < 0 or alege_numar > 12:
                print("Eroare: Numarul trebuie sa fie intre 1-12")
                continue
        except ValueError:
            print(f"Eroare: Trebuie sa introduceti un numar valid (ai introdus '{alege}')")
            continue

        if alege == "0":
            print("Program inchis.")
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