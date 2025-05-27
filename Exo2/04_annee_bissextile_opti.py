def fn_is_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        print(f"{annee} est une année bissextile")
    else:
        print(f"{annee} n'est pas une année bissextile")

annee = 2003
fn_is_bissextile(annee)