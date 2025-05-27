import csv

# Données des jeux vidéo
jeux = [
    ["The Legend of Zelda: Breath of the Wild", "2017"],
    ["Red Dead Redemption 2", "2018"],
    ["Cyberpunk 2077", "2020"],
    ["Elden Ring", "2022"]
]

# Écriture dans le fichier CSV
with open('jeux_video.csv', 'w', newline='') as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["Nom du jeu", "Année de sortie"])  # En-têtes
    writer.writerows(jeux)  # Données

# Lecture et affichage du fichier CSV
print("Contenu du fichier CSV :")
with open('jeux_video.csv', 'r') as fichier:
    reader = csv.reader(fichier)
    for ligne in reader:
        print(f"{ligne[0]} - {ligne[1]}")
