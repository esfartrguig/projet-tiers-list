import csv
import os
from pathlib import Path
import random
import string

# Dossiers et fichiers
DATA_DIR = Path("data")
TIERS_FILE = DATA_DIR / 'tiers.csv'
ELEMENTS_FILE = DATA_DIR / 'elements.csv'

class GestionTiersElements:
    def __init__(self):
        self.init_files()
    
    def init_files(self):
        """Initialise les fichiers CSV dans un dossier dédié"""
        DATA_DIR.mkdir(exist_ok=True)
        
        if not TIERS_FILE.exists():
            with open(TIERS_FILE, 'w', newline='', encoding='ascii') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'nom_categorie'])
        
        if not ELEMENTS_FILE.exists():
            with open(ELEMENTS_FILE, 'w', newline='', encoding='ascii') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'nom_element', 'description'])
    
    def generer_id(self):
        """Génère un ID aléatoire"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    def verifier_ascii(self, texte):
        """Vérifie que le texte ne contient que des caractères ASCII"""
        try:
            texte.encode('ascii')
            return True
        except UnicodeEncodeError:
            return False
    
    def afficher_categories(self):
        """Affiche toutes les catégories"""
        with open(TIERS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            print("\nListe des catégories:")
            for row in reader:
                print(f"ID: {row['id']}, Nom: {row['nom_categorie']}")
            print()
    
    def creer_categorie(self):
        """Crée une nouvelle catégorie"""
        nom_categorie = input("Entrez le nom de la catégorie : ")
        
        if not self.verifier_ascii(nom_categorie):
            print("Erreur: Seuls les caractères ASCII sont autorisés!")
            return
        
        id_categorie = self.generer_id()
        
        with open(TIERS_FILE, 'a', newline='', encoding='ascii') as file:
            writer = csv.writer(file)
            writer.writerow([id_categorie, nom_categorie])
        print("Catégorie créée avec succès!")
    
    def modifier_categorie(self):
        """Modifie une catégorie existante"""
        self.afficher_categories()
        id_categorie = input("Entrez l'ID de la catégorie à modifier : ")
        nouveau_nom = input("Entrez le nouveau nom de la catégorie : ")
        
        if not self.verifier_ascii(nouveau_nom):
            print("Erreur: Seuls les caractères ASCII sont autorisés!")
            return
        
        categories = []
        with open(TIERS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] == id_categorie:
                    row['nom_categorie'] = nouveau_nom
                categories.append(row)
        
        with open(TIERS_FILE, 'w', newline='', encoding='ascii') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nom_categorie'])
            writer.writeheader()
            writer.writerows(categories)
        print("Catégorie modifiée avec succès!")
    
    def supprimer_categorie(self):
        """Supprime une catégorie et ses éléments associés"""
        self.afficher_categories()
        id_categorie = input("Entrez l'ID de la catégorie à supprimer : ")
        
        # Supprimer la catégorie
        categories = []
        with open(TIERS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            categories = [row for row in reader if row['id'] != id_categorie]
        
        with open(TIERS_FILE, 'w', newline='', encoding='ascii') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nom_categorie'])
            writer.writeheader()
            writer.writerows(categories)
        
        # Supprimer les éléments associés
        elements = []
        with open(ELEMENTS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            elements = [row for row in reader if row['id'] != id_categorie]
        
        with open(ELEMENTS_FILE, 'w', newline='', encoding='ascii') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nom_element', 'description'])
            writer.writeheader()
            writer.writerows(elements)
        
        print("Catégorie et éléments associés supprimés avec succès!")
    
    def ajouter_element(self):
        """Ajoute un élément à une catégorie"""
        self.afficher_categories()
        id_categorie = input("Entrez l'ID de la catégorie pour l'élément : ")
        
        # Vérifier que la catégorie existe
        with open(TIERS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            categories = [row['id'] for row in reader]
            if id_categorie not in categories:
                print("Erreur: Cette catégorie n'existe pas!")
                return
        
        nom_element = input("Entrez le nom de l'élément : ")
        description = input("Entrez la description de l'élément : ")
        
        if not self.verifier_ascii(nom_element) or not self.verifier_ascii(description):
            print("Erreur: Seuls les caractères ASCII sont autorisés!")
            return
        
        with open(ELEMENTS_FILE, 'a', newline='', encoding='ascii') as file:
            writer = csv.writer(file)
            writer.writerow([id_categorie, nom_element, description])
        print("Élément ajouté avec succès!")
    
    def afficher_elements_par_categorie(self):
        """Affiche les éléments d'une catégorie spécifique"""
        self.afficher_categories()
        id_categorie = input("Entrez l'ID de la catégorie à afficher : ")
        
        # Récupérer le nom de la catégorie
        nom_categorie = ""
        with open(TIERS_FILE, 'r', encoding='ascii') as file:
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
        with open(ELEMENTS_FILE, 'r', encoding='ascii') as file:
            reader = csv.DictReader(file)
            elements_trouves = False
            for row in reader:
                if row['id'] == id_categorie:
                    print(f"Nom: {row['nom_element']}, Description: {row['description']}")
                    elements_trouves = True
            
            if not elements_trouves:
                print("Aucun élément trouvé pour cette catégorie.")
        print()
    
    def menu_principal(self):
        """Affiche le menu principal"""
        while True:
            print("\nGestion des Tiers et Éléments")
            print("1. Afficher toutes les catégories")
            print("2. Gérer les catégories")
            print("3. Gérer les éléments")
            print("4. Quitter")
            
            choix = input("Votre choix : ")
            
            match choix:
                case '1':
                    self.afficher_categories()
                case '2':
                    self.menu_categories()
                case '3':
                    self.menu_elements()
                case '4':
                    print("Au revoir!")
                    return
                case _:
                    print("Choix invalide!")
    
    def menu_categories(self):
        """Affiche le menu des catégories"""
        while True:
            print("\nGestion des Catégories")
            print("1. Créer une catégorie")
            print("2. Modifier une catégorie")
            print("3. Supprimer une catégorie")
            print("4. Afficher toutes les catégories")
            print("5. Retour au menu principal")
            
            sous_choix = input("Votre choix : ")
            
            match sous_choix:
                case '1':
                    self.creer_categorie()
                case '2':
                    self.modifier_categorie()
                case '3':
                    self.supprimer_categorie()
                case '4':
                    self.afficher_categories()
                case '5':
                    break
                case _:
                    print("Choix invalide!")
    
    def menu_elements(self):
        """Affiche le menu des éléments"""
        while True:
            print("\nGestion des Éléments")
            print("1. Ajouter un élément à une catégorie")
            print("2. Afficher les éléments d'une catégorie")
            print("3. Retour au menu principal")
            
            sous_choix = input("Votre choix : ")
            
            match sous_choix:
                case '1':
                    self.ajouter_element()
                case '2':
                    self.afficher_elements_par_categorie()
                case '3':
                    break
                case _:
                    print("Choix invalide!")

if __name__ == "__main__":
    gestion = GestionTiersElements()
    gestion.menu_principal()
