import csv

# fonction affichant le menu du script et renvoyant le choix de la recette
def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations de la recette")
    print(f"2. Afficher les recettes")
    print(f"3. Réinitialiser le fichier")
    print(f"4. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2, 3 ou 4) : ")
    return choix

# fonction d'encodage des données de la recette dans un dictionnaire et renvoyant celle-ci
def fn_encode_data_recipe():
    title = input("Entrez le titre de la recette : ")
    list_ingredients_complete = False
    list_ingredients = []
    while not list_ingredients_complete:
        ingredient = input("Entrez un ingrédient : ")
        quantity = input(f"Entrez la quantité nécessaire pour {ingredient} avec l'unité : ")
        dict_ing_qte = {"ingrédient":ingredient, "quantité": quantity}
        list_ingredients.append(dict_ing_qte)
        add_ingredient = input("Voulez-vous ajouter un ingrédient ? (o/n) : ")
        if add_ingredient == "n":
            list_ingredients_complete = True
    preparation_time = input("Entrez le temps de préparation de la recette en minute : ")
    recette = {"titre": title, "ingrédients": list_ingredients, "temps de préparation": preparation_time}
    return recette

# fonction qui récupère les données de la recette sous forme de liste et les ajoute dans une liste
def fn_list_data_recipe(data_recipe, list_data_recipe):
    list_data_recipe.append(data_recipe)

# fonction qui prend une liste de recettes et écrit les données dans un fichier csv. Les données d'un jeu sont écrits sur une même ligne séparé par des virgules
def fn_write_list_data_recipe_to_file(recipe_file, list_data_recipe):
    with open (recipe_file, 'w', newline='', encoding='utf-8') as file:
        for recipe in list_data_recipe:
            fieldnames = ['titre', 'ingrédients', 'temps de préparation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            ingredients_str = ';'.join([f"{ing['ingrédient']} ({ing['quantité']})" for ing in recipe['ingrédients']])
            writer.writerow({'titre': recipe['titre'], 'ingrédients': ingredients_str, 'temps de préparation': recipe['temps de préparation']})

# fonction qui lit les données dans un fichier csv, les encodes dans une liste et affiche la liste
def fn_read_recipe_file(recipe_file):
    with open(recipe_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"\nTitre : {row['titre']}")
            # print(f"Ingrédients : {row['ingrédients']}")
            for i, ingredient in enumerate(row['ingrédients'].split(';')):
                print(f"Ingrédient {i+1} : {ingredient}")
            print(f"Temps de préparation : {row['temps de préparation']} minutes")
            input("Appuyez sur une touche pour continuer")

# fonction qui réinitialise le fichier csv
def fn_reset_recipe_file(recipe_file):
    with open(recipe_file, "w") as file:
        print(f"{recipe_file} a été réinitialisé")

# execution du script    
script_run = True
recipe_file = "14_recettes.csv"
while script_run:
    list_data_recipe = []
    choix = fn_menu()
    match choix:
        case "1" :
            try:
                data_recipe = fn_encode_data_recipe()
                fn_list_data_recipe(data_recipe, list_data_recipe)
                debug_msg = fn_write_list_data_recipe_to_file(recipe_file, list_data_recipe)
                print (debug_msg)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {recipe_file} n'existe pas")
            except Exception as e:
                print(f"Une erreur inattendue s'est produite : {e}")   
        case '2':
            try :
                fn_read_recipe_file(recipe_file)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {recipe_file} n'existe pas")
        case '3':
            try :
                fn_reset_recipe_file(recipe_file)
            except FileNotFoundError:
                print(f"\nERREUR : Le fichier {recipe_file} n'existe pas")                
        case '4':
            script_run = False
            print(f"Fermeture de l'application")
        case _:
            print("Choix non-valide")