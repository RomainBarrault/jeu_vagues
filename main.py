from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["joueur"]
mechant = db["mechant"]
joueur = db["joueur"]

supp = mechant.delete_many({})
supp = joueur.delete_many({})

mechants = [
    {"nom": "squelette","pv": 12,"atk": 5},
    {"nom": "zombie", "pv": 18, "atk": 4},
    {"nom": "loup-garou", "pv": 25, "atk": 7},
    {"nom": "demon", "pv": 30, "atk": 10},
    {"nom": "araignee_geante", "pv": 20, "atk": 5}
]
ajouter_mechants = mechant.insert_many(mechants)

joueurs = [
    {"nom": "guerrier", "pv": 30, "atk": 7},
    {"nom": "archer", "pv": 20, "atk": 9},
    {"nom": "mage", "pv": 15, "atk": 12},
    {"nom": "assassin", "pv": 18, "atk": 14},
    {"nom": "alchimiste", "pv": 23, "atk": 6},
    {"nom": "chaman", "pv": 22, "atk": 7}
]
ajouter_joueurs = joueur.insert_many(joueurs)

choix = 0
joueur_dans_jeu = joueurs

print(joueur_dans_jeu)

#menu
    # tant que infini
        # montrer les différent choix
        # demander le choix au joueur
        # retourner le choix


       
# choix menu            

    # si le choix est un nombre et compris entre 1 et 3
        # transformer choix en chaine de caractère
        # si c'est 1 print le choix choisi et lancer choix joueur
            #écrire lancement du jeu
        # sinon si c'est 2 lancer leaderboard 
             #écrire entrer dans le leaderbord
        # sinon ecrire quitter
    #sinon
        # print que le choix n'est pas bon


#choix_joueur(joueurs_dans_jeu)
    # tant que infini
        # joueur_choisis
        # si le nombre de joueur est égal à trois
            # print 
            # return joueur_choisis
        # sinon
            # montrer les différents joueur disponible avec leurs atouts
            # demander le choix au joueur 
            # si le choix est un chiffre et compris entre le nombre de joueur dans le jeu
            # ajouter sur mongo(joueur_choisi = joueur_choisis.insert_many(joueur_choisis))
            # print le joueur choisi 
            



# def main():
    #menu(choix)
    #choix_joueur(joueurs_dans_jeu)
#main()