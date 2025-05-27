# Les années sont bissextiles si elles sont multiples de quatre, mais pas si elles sont multiples de cent, à l'exception des années multiples de quatre cents qui, elles, sont également bissextiles.

def fn_input_annee():
    annee = int(input("Entrez une année : "))
    return annee

def fn_is_annee_bissextile(annee):
    if annee%4 == 0:
        if annee%100 == 0:
            if annee%400 == 0:
                print(f"L'année {annee} est bissextile")
            else:
                print(f"L'année {annee} n'est pas bissextile")
        else:
            print(f"L'année {annee} est bissextile")
    else:
        print(f"L'année {annee} n'est pas bissextile")

annee = fn_input_annee()
fn_is_annee_bissextile(annee)