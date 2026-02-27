
salariu_minim = 4050
aceptare_nivel = ["junior","mid","senior"]


def cnp_validare(cnp: str) -> bool:
    """
    """
    return len(cnp) == 13 and cnp.isdigit()

def cere_cnp_valid():
    """
    """
    while True:
        cnp = input("Introduceti CNP-ul (13 cifre) sau '0' pentru meniu: ").strip()

        if cnp == "0":
            return "0"
        
        if cnp_validare(cnp):
            return cnp
        if not cnp.isdigit():
            print(f"Eroare: CNP contine caracter nerpermise (litere/simboluri).")
            continue
        elif len(cnp) != 13:
            print(f"Eroare: Lungime incorecta. Trebuie 13 cifre (ai introdus {len(cnp)}).")
            continue
        return cnp


def validare_nume(text):
    """
    """
    text = text.strip().title()
   
    for caractere in text:
        if not (caractere.isalpha() or caractere == " " or caractere == "-"):
            print(f"Eroare: '{text}' contine carcatere nepermise (cifre sau simboluri)")
            return False
        
    if len(text) < 3:
        print(f"Eroare: '{text}' este prea scrut ( minim 3 litere). ")
        return False
    
    return True

def varsta_validare(varsta):
    """
    """
    try:
        varsta = int(varsta)
        if varsta >= 18:
            return True
        else:
            print(f"Varsta trebuie sa fie peste 18 ani (ai introdus {varsta})")
    except ValueError as erroare:
        print(f"Varsta trebuie sa fie un numar valid (detaliu {erroare})")
        return False
    


def salariu_validare(salar: str) -> bool:
    """
    """
    try:
        valoare = int(salar)
        if valoare >= salariu_minim:
            return True
        else:
            print(f" Salariul trebuie sa fie mai mare de {salariu_minim} RON! (ai introdus {valoare}) ")
            return False 
    except ValueError as erroare:
        print(f"Salariu trebuie sa fie un numar valid!(detaliu: {erroare})")
        return False
    
def departament_validare(departament):
    """
    """
    if not departament.isalnum():
        print(f"Departamentul nu poate contine charactere speciale , poate sa contina doar Litere/Cifre")
        return False
    if len(departament) < 2:
        print(f"Numele departamentului este prea scurt tu ai introdus '{len(departament)}' caracter  ")
        return False

    
    return True

def senior_validare(senioritate):
    """
    """
    return senioritate.lower() in aceptare_nivel
