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
        print(f"\nfilm {num}")
        print(f"Titre : {data[0]}")
        print(f"Genre : {data[1]}")
        print(f"Date de sortie : {data[2]}")
        print(f"Réalisateur : {data[3]}")
        print(f"Note IMDB : {data[4]}")
        num += 1

def fn_write_list_data_movie_to_file(movie_file, list_data_movie):
    with open(movie_file, "a") as file:
        for movie in list_data_movie:      
            m = 0
            for data in movie:
                index_last_element = len(movie) - 1
                if m != index_last_element:
                    file.write(f"{data}, ")
                else:
                    file.write(f"{data}\n")
                m += 1
    return f"Les données ont été écrites dans le fichier '{movie_file}'"

def fn_read_movie_file(movie_file):
    with open(movie_file, "r") as file:
        movies_list = file.read()
        print(movies_list)

# fonction principal du script
def fn_app():    
    script_run = True
    movie_file = "10_movies_file.txt"
    while script_run:
        list_data_movie = []
        choix = fn_menu()
        match choix:
            case "1" :
                data_movie = fn_encode_data_movie()
                fn_list_data_movie(data_movie, list_data_movie)
                debug_msg = fn_write_list_data_movie_to_file(movie_file, list_data_movie)
                print (debug_msg)
            case '2':
                try :
                    fn_read_movie_file(movie_file)
                except FileNotFoundError:
                    print(f"\nERREUR : Le fichier {movie_file} n'existe pas")
                # if list_data_movie:
                #     fn_display_list(list_data_movie)                    
                # else:
                #     print("La liste est vide.")
            case '3':
                script_run = False
                print(f"Fermeture de l'application")
            case _:
                print("Choix non-valide")

# exécution de la fonction principale
fn_app()