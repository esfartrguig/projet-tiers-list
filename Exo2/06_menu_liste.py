def afficher_menu():
    print("\nMenu :")
    print("1. Ajouter une information à la liste")
    print("2. Afficher le contenu de la liste")
    print("3. Quitter le programme")


def main():
    liste_informations = []
    script_run = True
    while script_run:
        afficher_menu()
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
       
        if choix == '1':
            info = input("Entrez une information à ajouter : ")
            liste_informations.append(info)
            print(f"{info} a été ajouté à la liste.")
       
        elif choix == '2':
            if liste_informations:
                print("Contenu de la liste :")
                for index, item in enumerate(liste_informations, start=1):
                    print(f"{index}. {item}")
            else:
                print("La liste est vide.")
       
        elif choix == '3':
            print("D'acc, bye")
            script_run = False

main()