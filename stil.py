# Culori de baza (Coduri ANSI)
ROSU = "\033[31m"
VERDE = "\033[32m"
GALBEN = "\033[33m"
ALBASTRU = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"
MAGENTA = "\033[35m"

def eroare(mesaj: str):
    """Afiseaza mesaje de eroare cu rosu."""
    print(f"{ROSU}{BOLD}[!] EROARE: {mesaj}{RESET}")

def succes(mesaj: str):
    """Afiseaza confirmari cu verde."""
    print(f"{VERDE}{BOLD}[OK] {mesaj}{RESET}")

def titlu(mesaj: str):
    """Afiseaza un titlu de sectiune cu galben si linii de separare."""
    print(f"{GALBEN}{BOLD}{'='*40}")
    print(f" {mesaj.upper()}")
    print(f"{'='*40}{RESET}")

def info(mesaj: str):
    """Afiseaza informatii de sistem sau ghidaj cu cyan."""
    print(f"{CYAN}{BOLD}>>> {mesaj}{RESET}")

def evidentiaza(text) -> str:
    """Returneaza textul colorat cu albastru pentru a fi folosit in interiorul unui print."""
    return f"{ALBASTRU}{BOLD}{text}{RESET}"

def atentionare(mesaj: str):
    """Afiseaza mesaje de avertizare cu galben/portocaliu."""
    print(f"{GALBEN}{BOLD}[!] ATENTIE: {mesaj}{RESET}")