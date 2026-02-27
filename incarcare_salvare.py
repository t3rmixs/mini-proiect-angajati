import os
import json

nume_fisier = "angajati.json"

def incarca_fisier_angajati():
    if not os.path.exists(nume_fisier):
        return []
    try:
        with open(nume_fisier, "r", encoding="utf-8") as my_file:
            date = json.load(my_file)
            return date
    except (json.JSONDecodeError, IOError) as erroare_incarcare:
        print(f"Ai o mica eroare la citirea fisierului : {erroare_incarcare}")
        return []
    
def salveaza_fisier_angajati(angajati): 
    """
    """
    try:
        with open(nume_fisier, "w" , encoding="utf-8") as my_file:
            json.dump(angajati, my_file, indent=4)
        return True
    except IOError as error_save:
        print(f"Ai o mica eroare la salvarea fisierului : {error_save}")
        return False
    

