def fn_is_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        print(f"{annee} est une année bissextile")
    else:
        print(f"{annee} n'est pas une année bissextile")

def fn_input_annee():
    annee = int(input("Entrez une année : "))
    return annee

def fn_menu():
    print(f"1. Continuer")
    print(f"2. Quitter")
    script_continue = input()
    return script_continue

script_run = True
while script_run:    
    annee = fn_input_annee()
    fn_is_bissextile(annee)
    script_continue = fn_menu()
    if script_continue == "2":
        script_run = False
        print(f"Fermeture du script")
