
"""
Modulul validari contine toate functiile necesare pentru validarea datelor introduse de utilizator.
Aceste functii asigură ca datele introduse (CNP, nume, varsta, salariu, etc.) respecta formatul corect
inainte de a fi procesate sau salvate in sistem.
"""

salariu_minim: int = 4050
aceptare_nivel: list[str] = ["junior","mid","senior"]


def cnp_validare(cnp: str) -> bool:
    """
    Verifica daca un CNP introdus are formatul corect.
    
    Un CNP valid trebuie sa indeplineasca urmatoarele conditii:
    - Sa contina exact 13 caractere
    - Toate caracterele trebuie sa fie cifre (0-9)
    
    Aceasta functie nu verifica validitatea reala a CNP-ului (algoritmul de control),
    ci doar formatul de baza.
    
    Exemple:
        "1234567890123" -> True (13 cifre)
        "123456789012"  -> False (12 cifre)
        "123456789012A" -> False (contine litere)
    
    Args:
        cnp (str): Sirul de caractere care reprezinta CNP-ul de validat.
        
    Returns:
        bool: True daca CNP-ul are format valid (13 cifre), False in caz contrar.
    """
    return len(cnp) == 13 and cnp.isdigit()

def cere_cnp_valid() -> str:
    """
    Cere utilizatorului sa introduca un CNP valid si continua sa il intrebe pana cand
    acesta introduce un CNP corect sau alege sa revina la meniu.
    
    Functia afiseaza mesaje de eroare specifice pentru a ghida utilizatorul:
    - Daca CNP-ul contine litere sau simboluri
    - Daca CNP-ul nu are exact 13 cifre
    
    Utilizatorul poate introduce '0' in orice moment pentru a reveni la meniul principal.
    
    Returns:
        str: CNP-ul validat (13 cifre) sau '0' daca utilizatorul doreste sa revina la meniu.
        
    Note:
        Aceasta functie blocheaza executia pana cand utilizatorul introduce un CNP valid
        sau alege sa iasa. Este o functie de tip 'input loop'.
    """
    while True:
        cnp: str = input("Introduceti CNP-ul (13 cifre) sau '0' pentru meniu: ").strip()

        if cnp == "0":
            return "0"
        
        if cnp_validare(cnp):
            return cnp
        if not cnp.isdigit():
            print(f"Eroare: CNP contine caracter nepermise (litere/simboluri).")
            continue
        elif len(cnp) != 13:
            print(f"Eroare: Lungime incorecta. Trebuie 13 cifre (ai introdus {len(cnp)}).")
            continue
        return cnp


def validare_nume(text: str) -> bool:
    """
    Verifica daca un nume sau prenume introdus este valid.
    
    Un nume valid trebuie sa indeplineasca urmatoarele conditii:
    - Sa contina doar litere, spatii si cratime (pentru nume compuse)
    - Sa aiba minim 3 caractere (dupa eliminarea spatiilor)
    - Nu poate contine cifre sau simboluri speciale
    
    Functia normalizeaza textul prin eliminarea spatiilor de la inceput/sfarsit
    si convertirea la formatul Title (prima litera mare).
    
    Exemple:
        "Popescu"     -> True
        "Ion-Vlad"    -> True
        "Pop123"      -> False (contine cifre)
        "Al"          -> False (prea scurt)
    
    Args:
        text (str): Numele sau prenumele de validat.
        
    Returns:
        bool: True daca numele este valid, False daca contine erori.
        
    Note:
        Functia afiseaza mesaje de eroare descriptive pentru a ajuta utilizatorul
        sa inteleaga de ce numele introdus nu este acceptat.
    """
    text = text.strip().title()
   
    for caractere in text:
        if not (caractere.isalpha() or caractere == " " or caractere == "-"):
            print(f"Eroare: '{text}' contine carcatere nepermise (cifre sau simboluri)")
            return False
        
    if len(text) < 3:
        print(f"Eroare: '{text}' este prea scurt ( minim 3 litere). ")
        return False
    
    return True

def varsta_validare(varsta: str) -> bool:
    """
    Verifica daca varsta introdusa este un numar valid si respecta limita minima de 18 ani.
    
    Aceasta functie incearca sa converteasca input-ul la numar intreg si verifica:
    - Daca conversia reuseste (nu contine litere)
    - Daca varsta este mai mare sau egala cu 18 ani
    
    Exemple:
        "25"  -> True
        "17"  -> False (prea tanar)
        "abc" -> False (nu este numar)
    
    Args:
        varsta (str): Varsta introdusa de utilizator ca sir de caractere.
        
    Returns:
        bool: True daca varsta este valida (numar >= 18), False in caz de eroare.
        
    Note:
        Functia gestioneaza exceptiile ValueError pentru cazurile cand utilizatorul
        introduce text in loc de numere.
    """
    try:
        varsta: int = int(varsta)
        if varsta >= 18:
            return True
        else:
            print(f"Varsta trebuie sa fie peste 18 ani (ai introdus {varsta})")
    except ValueError as erroare:
        print(f"Varsta trebuie sa fie un numar valid (detaliu {erroare})")
        return False
    


def salariu_validare(salar: str) -> bool:
    """
    Verifica daca salariul introdus este un numar valid si respecta salariul minim legal.
    
    Salariul minim este definit in constanta 'salariu_minim' (implicit 4050 RON).
    Functia verifica:
    - Daca input-ul poate fi convertit la numar intreg
    - Daca valoarea este mai mare sau egala cu salariul minim
    
    Exemple:
        "5000" -> True (peste minim)
        "3000" -> False (sub minim)
        "abc"  -> False (nu este numar)
    
    Args:
        salar (str): Salariul introdus de utilizator ca sir de caractere.
        
    Returns:
        bool: True daca salariul este valid (>= salariu_minim), False in caz de eroare.
        
    Note:
        Mesajele de eroare includ valoarea salariului minim curent pentru a ghida
        utilizatorul catre o valoare acceptabila.
    """
    try:
        valoare: int = int(salar)
        if valoare >= salariu_minim:
            return True
        else:
            print(f" Salariul trebuie sa fie mai mare de {salariu_minim} RON! (ai introdus {valoare}) ")
            return False 
    except ValueError as erroare:
        print(f"Salariu trebuie sa fie un numar valid!(detaliu: {erroare})")
        return False
    
def departament_validare(departament: str) -> bool:
    """
    Verifica daca numele departamentului introdus este valid.
    
    Un departament valid trebuie sa:
    - Contină doar litere si cifre (fara simboluri speciale)
    - Sa aiba minim 2 caractere
    
    Exemple:
        "IT"        -> True
        "HR2024"    -> True
        "IT-C"      -> False (contine cratime)
        "A"         -> False (prea scurt)
    
    Args:
        departament (str): Numele departamentului de validat.
        
    Returns:
        bool: True daca departamentul este valid, False in caz de eroare.
        
    Note:
        Departamentele sunt stocate in format uppercase pentru consistenta.
    """
    if not departament.isalnum():
        print(f"Departamentul nu poate contine caractere speciale , poate sa contina doar Litere/Cifre")
        return False
    if len(departament) < 2:
        print(f"Numele departamentului este prea scurt tu ai introdus '{len(departament)}' caracter  ")
        return False

    
    return True

def senior_validare(senioritate: str) -> bool:
    """
    Verifica daca nivelul de senioritate introdus este unul dintre cele acceptate.
    
    Nivelurile acceptate sunt definite in lista 'aceptare_nivel':
    - junior: incepator, fara experienta sau cu experienta mica
    - mid: nivel mediu, cu experienta semnificativa
    - senior: nivel avansat, cu experienta extinsa
    
    Comparatia este case-insensitive (nu distinse intre majuscule si minuscule).
    
    Exemple:
        "junior" -> True
        "JUNIOR" -> True
        "lead"   -> False (nu este in lista)
    
    Args:
        senioritate (str): Nivelul de senioritate de validat.
        
    Returns:
        bool: True daca senioritatea este in lista de valori acceptate, False altfel.
        
    Note:
        Functia converteste input-ul la lowercase inainte de comparatie pentru
        a permite utilizatorului sa scrie cu majuscule sau minuscule.
    """
    return senioritate.lower() in aceptare_nivel
