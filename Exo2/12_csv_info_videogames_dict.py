import csv

# Création du dictionnaire de jeux vidéo
jeux = [
    {"nom": "The Legend of Zelda: Breath of the Wild", "annee": 2017},
    {"nom": "Red Dead Redemption 2", "annee": 2018},
    {"nom": "Super Mario Odyssey", "annee": 2017},
    {"nom": "God of War", "annee": 2018}
]

# Écriture dans le fichier CSV
with open('jeux.csv', 'w', newline='', encoding='utf-8') as fichier:
    writer = csv.DictWriter(fichier, fieldnames=['nom', 'annee'])
    writer.writeheader()
    writer.writerows(jeux)

# Lecture et affichage du fichier CSV
print("Contenu du fichier CSV :")
with open('jeux.csv', 'r', encoding='utf-8') as fichier:
    reader = csv.DictReader(fichier)
    for ligne in reader:
        print(f"Jeu : {ligne['nom']}, Année : {ligne['annee']}")