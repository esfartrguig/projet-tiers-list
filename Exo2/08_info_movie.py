# fonction affichant le menu du script et renvoyant le choix du film
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'un film à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2 ou 3) : ")
    return choix

# fonction d'encodage des données d'un film dans une liste et renvoyant celle-ci
def fn_encode_data_movie():
    title = input("Entrez le titre du film : ")
    genre = input("Entrez le genre du film : ")
    date_de_sortie = input("Entrez l'année de sortie du film : ")    
    director = input("Entrez le réalisateur du film : ")
    note_imdb = input("Entrez la note IMDB du film : ")
    data_movie = [title, genre, date_de_sortie, director, note_imdb]
    return data_movie

# fonction qui récupère les données d'un film sous forme de liste et les ajoute dans une liste
def fn_list_data_movie(data_movie, list_data_movie):
    list_data_movie.append(data_movie)

# fonction d'affichage des données de la liste de liste
def fn_display_list(list_data_movie):
    num = 1
    for data in list_data_movie:        
        print(f"\nfilm {num}.")
        print(f"Titre : {data[0]}")
        print(f"Genre : {data[1]}")
        print(f"Date de sortie : {data[2]}")
        print(f"Réalisateur : {data[3]}")
        print(f"Note IMDB : {data[3]}")
        num += 1

# fonction principal du script
def fn_app():    
    script_run = True
    list_data_movie = []
    while script_run:
        choix = fn_menu()
        match choix:
            case "1" :
                data_movie = fn_encode_data_movie()
                fn_list_data_movie(data_movie, list_data_movie)
            case '2':
                if list_data_movie:
                    fn_display_list(list_data_movie)
                else:
                    print("La liste est vide.")
            case '3':
                script_run = False
                print(f"Fermeture de l'application")
            case _:
                print("Choix non-valide")

# exécution de la fonction principale
fn_app()