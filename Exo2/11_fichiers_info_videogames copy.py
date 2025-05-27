# fonction affichant le menu du script et renvoyant le choix du jeu video
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un jeu video")
    print(f"2. Afficher les jeux video")
    print(f"3. Réinitialiser le fichier")
    print(f"4. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2, 3 ou 4) : ")
    return choix

# fonction d'encodage des données d'un jeu video dans une liste et renvoyant celle-ci
def fn_encode_data_videogame():
    title = input("Entrez le titre du jeu video : ")
    genre = input("Entrez le genre du jeu video : ")
    date_de_sortie = input("Entrez l'année de sortie du jeu video : ")    
    plateform = input("Entrez la plateforme sur laquelle est sortie le jeu video : ")
    dev = input("Entrez le nom des développeurs du jeu video : ")
    data_videogame = [title, genre, date_de_sortie, plateform, dev]
    return data_videogame

# fonction qui récupère les données d'un jeu video sous forme de liste et les ajoute dans une liste
def fn_list_data_videogame(data_videogame, list_data_videogame):
    list_data_videogame.append(data_videogame)

# fonction qui prend une liste de jeu video et écrit les données dans un fichier texte. Les données d'un jeu sont écrits sur une même ligne séparé par des virgules
def fn_write_list_data_videogame_to_file(videogame_file, list_data_videogame):
    with open(videogame_file, "a") as file:
        for videogame in list_data_videogame:     
           file.write(", ".join(videogame) + "\n")
    return f"Les données ont été écrites dans le fichier '{videogame_file}'"

# fonction qui lit les données dans un fichier texte, les encodes dans une liste et affiche la liste
def fn_read_videogame_file(videogame_file):
    with open(videogame_file, "r") as file:
        videogames_list = file.read()
        print(videogames_list)

# fonction qui réinitialise le fichier texte
def fn_reset_videogame_file(videogame_file):
    with open(videogame_file, "w") as file:
        print(f"{videogame_file} a été réinitialisé")

# execution du script    
script_run = True
videogame_file = "11_videogames_file.txt"
while script_run:
    list_data_videogame = []
    choix = fn_menu()
    match choix:
        case "1" :
            try:
                data_videogame = fn_encode_data_videogame()
                fn_list_data_videogame(data_videogame, list_data_videogame)
                debug_msg = fn_write_list_data_videogame_to_file(videogame_file, list_data_videogame)
                print (debug_msg)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {videogame_file} n'existe pas")
            except Exception as e:
                print(f"Une erreur inattendue s'est produite : {e}")   
        case '2':
            try :
                fn_read_videogame_file(videogame_file)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {videogame_file} n'existe pas")
        case '3':
            try :
                fn_reset_videogame_file(videogame_file)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {videogame_file} n'existe pas")                
        case '4':
            script_run = False
            print(f"Fermeture de l'application")
        case _:
            print("Choix non-valide")