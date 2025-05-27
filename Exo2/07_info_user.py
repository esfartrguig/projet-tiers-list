# fonction affichant le menu du script et renvoyant le choix de l'utilisateur
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un utilisateur à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2 ou 3) : ")
    return choix

# fonction d'encodage des données d'un utilisateur dans une liste et renvoyant celle-ci
def fn_encode_data_user():
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prenom : ")
    date_de_naissance = input("Entrez votre date de naissance : ")
    code_postal = input("Entrez votre code postal : ")
    data_user = [nom, prenom, date_de_naissance, code_postal]
    return data_user

# fonction qui récupère les données d'un utilisateur sous forme de liste et les ajoute dans une liste
def fn_list_data_user(data_user, list_data_user):
    list_data_user.append(data_user)

# fonction d'affichage des données de la liste de liste
def fn_display_list(list_data_user):
    num = 1
    for data in list_data_user:        
        print(f"\nUtilisateur {num}.")
        print(f"Nom : {data[0]}")
        print(f"Prenom : {data[1]}")
        print(f"Date de naissance : {data[2]}")
        print(f"Code postal : {data[3]}")
        num += 1

# fonction principal du script
def fn_app():    
    script_run = True
    list_data_user = []
    while script_run:
        choix = fn_menu()
        if choix == '1':
            data_user = fn_encode_data_user()
            fn_list_data_user(data_user, list_data_user)
        elif choix == '2':
            if list_data_user:
                fn_display_list(list_data_user)
            else:
                print("La liste est vide.")
        elif choix == '3':
            script_run = False
            print(f"Fermeture de l'application")
        else:
            print("Choix non-valide")

# exécution de la fonction principale
fn_app()