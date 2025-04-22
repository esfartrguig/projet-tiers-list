import csv
import os

# Fichiers CSV
TIERS_FILE = 'tiers.csv'
ELEMENTS_FILE = 'elements.csv'

# Initialisation des fichiers CSV s'ils n'existent pas
def init_files():
    if not os.path.exists(TIERS_FILE):
        with open(TIERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nom_categorie'])
    
    if not os.path.exists(ELEMENTS_FILE):
        with open(ELEMENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nom_element', 'description'])

# Fonctions pour les tiers (catégories)
def creer_categorie():
    id_categorie = input("Entrez l'ID de la catégorie : ")
    nom_categorie = input("Entrez le nom de la catégorie : ")
    
    with open(TIERS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_categorie, nom_categorie])
    print("Catégorie créée avec succès!")

def modifier_categorie():
    afficher_categories()
    id_categorie = input("Entrez l'ID de la catégorie à modifier : ")
    nouveau_nom = input("Entrez le nouveau nom de la catégorie : ")
    
    categories = []
    with open(TIERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == id_categorie:
                row['nom_categorie'] = nouveau_nom
            categories.append(row)
    
    with open(TIERS_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nom_categorie'])
        writer.writeheader()
        writer.writerows(categories)
    print("Catégorie modifiée avec succès!")

def supprimer_categorie():
    afficher_categories()
    id_categorie = input("Entrez l'ID de la catégorie à supprimer : ")
    
    # Supprimer la catégorie
    categories = []
    with open(TIERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        categories = [row for row in reader if row['id'] != id_categorie]
    
    with open(TIERS_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nom_categorie'])
        writer.writeheader()
        writer.writerows(categories)
    
    # Supprimer les éléments associés
    elements = []
    with open(ELEMENTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        elements = [row for row in reader if row['id'] != id_categorie]
    
    with open(ELEMENTS_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nom_element', 'description'])
        writer.writeheader()
        writer.writerows(elements)
    
    print("Catégorie et éléments associés supprimés avec succès!")

def afficher_categories():
    with open(TIERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        print("\nListe des catégories:")
        for row in reader:
            print(f"ID: {row['id']}, Nom: {row['nom_categorie']}")
        print()

# Fonctions pour les éléments
def ajouter_element():
    afficher_categories()
    id_categorie = input("Entrez l'ID de la catégorie pour l'élément : ")
    
    # Vérifier que la catégorie existe
    with open(TIERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        categories = [row['id'] for row in reader]
        if id_categorie not in categories:
            print("Erreur: Cette catégorie n'existe pas!")
            return
    
    nom_element = input("Entrez le nom de l'élément : ")
    description = input("Entrez la description de l'élément : ")
    
    with open(ELEMENTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_categorie, nom_element, description])
    print("Élément ajouté avec succès!")

def afficher_elements_par_categorie():
    afficher_categories()
    id_categorie = input("Entrez l'ID de la catégorie à afficher : ")
    
    # Récupérer le nom de la catégorie
    nom_categorie = ""
    with open(TIERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == id_categorie:
                nom_categorie = row['nom_categorie']
                break
    
    if not nom_categorie:
        print("Erreur: Catégorie non trouvée!")
        return
    
    # Afficher les éléments
    print(f"\nÉléments de la catégorie '{nom_categorie}':")
    with open(ELEMENTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        elements_trouves = False
        for row in reader:
            if row['id'] == id_categorie:
                print(f"Nom: {row['nom_element']}, Description: {row['description']}")
                elements_trouves = True
        
        if not elements_trouves:
            print("Aucun élément trouvé pour cette catégorie.")
    print()

# Menu principal
def menu():
    init_files()
    
    while True:
        print("\nGestion des Tiers et Éléments")
        print("1. Gérer les catégories")
        print("2. Gérer les éléments")
        print("3. Quitter")
        
        choix = input("Votre choix : ")
        
        if choix == '1':
            while True:
                print("\nGestion des Catégories")
                print("1. Créer une catégorie")
                print("2. Modifier une catégorie")
                print("3. Supprimer une catégorie")
                print("4. Afficher toutes les catégories")
                print("5. Retour au menu principal")
                
                sous_choix = input("Votre choix : ")
                
                if sous_choix == '1':
                    creer_categorie()
                elif sous_choix == '2':
                    modifier_categorie()
                elif sous_choix == '3':
                    supprimer_categorie()
                elif sous_choix == '4':
                    afficher_categories()
                elif sous_choix == '5':
                    break
                else:
                    print("Choix invalide!")
        
        elif choix == '2':
            while True:
                print("\nGestion des Éléments")
                print("1. Ajouter un élément à une catégorie")
                print("2. Afficher les éléments d'une catégorie")
                print("3. Retour au menu principal")
                
                sous_choix = input("Votre choix : ")
                
                if sous_choix == '1':
                    ajouter_element()
                elif sous_choix == '2':
                    afficher_elements_par_categorie()
                elif sous_choix == '3':
                    break
                else:
                    print("Choix invalide!")
        
        elif choix == '3':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide!")

if __name__ == "__main__":
    menu()