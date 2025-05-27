# définition des fonctions
def fn_poser_question(question) :
    """Une fonction qui affiche la question,
       les choix possibles de réponse et qui demande à
       l'utilisateur son choix.

       La fonction retourne ``True`` si l'utilisateur a choisi
       la bonne réponse
    """
    print(f"\n{question.get("libelle")}")
    n = 1
    for choix in question.get("choix"):
        print(f"{n}'. '{choix}")
        n+=1
    answer_incorrect = True
    while answer_incorrect:
        try:
            reponse_utilisateur = int(input("Entrez votre réponse : "))
        except ValueError :
            print("Erreur : Veuillez entrez un nombre correspondant à votre réponse")
        else:
            if reponse_utilisateur in range(1,5):                
                answer_incorrect = False
            else:
                print("La réponse doit être un nombre compris entre 1 et 4")
            
    if (reponse_utilisateur-1) == question.get("reponse"):
        return True
    else:
        return False
    
def fn_main():
    print(f"QCM sur les Jeux Video : Edition 2010'")
    answer_incorrect = True
    while answer_incorrect:
        start_qcm = input("Voulez-vous lancer le QCM ? (O/N)")
        if start_qcm not in ["O", "N", "o", "n"]:
            print("Erreur : Veuillez répondre 'O' ou 'N'")
        else:
            answer_incorrect = False
    if start_qcm.lower() == 'o':
        # initialisation des variables
        qcm = [] # Le contenu du QCM à définir
        question01 = {"libelle" : "Quel jeu, sorti en 2013, a révolutionné le genre de la survie en monde ouvert ?", 
                    "choix" : [
                        "The Witcher 3: Wild Hunt",
                        "Grand Theft Auto V",
                        "The Last of Us",
                        "Red Dead Redemption 2"
                    ],
                    "reponse" : 2}
        question02 = {"libelle" : "Dans quel jeu peut-on incarner un chasseur de monstres dans un monde ouvert rempli de créatures mythiques ?", 
                    "choix" : [
                        "Nioh",
                        "Dark Souls III",
                        "Bloodborne",
                        "Monster Hunter: World"
                    ],
                    "reponse" : 3}
        question03 = {"libelle" : "Quel jeu indépendant, sorti en 2016, a séduit les joueurs avec son gameplay innovant mêlant plateformes et énigmes ?", 
                    "choix" : [
                        "Inside",
                        "Limbo",
                        "Braid",
                        "Portal 2"
                    ],
                    "reponse" : 0}
        question04 = {"libelle" : "Dans quel jeu peut-on explorer un monde post-apocalyptique infesté de zombies ?", 
                    "choix" : [
                        "The Last of Us",
                        "Fallout 4",
                        "Dying Light",
                        "Les trois réponses précédentes"
                    ],
                    "reponse" : 3}
        qcm.append(question01)
        qcm.append(question02)
        qcm.append(question03)
        qcm.append(question04)
        score = 0

        # execution du programme
        # on parcourt la liste des questions et on calcule le score de l'utilisateur
        for question in qcm:
            if fn_poser_question(question):
                score += 2.5

        # on affiche le score
        print("Vous avez obtenu un score de ", score)
    
    else:
        print("Fermeture du programme")

fn_main()