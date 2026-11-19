from pymongo import MongoClient
import time
client = MongoClient("mongodb://localhost:27017")
db = client["joueur"]
mechant = db["mechant"]
joueur = db["joueur"]
joueur_jouer = db["joueur_jouer"]
scores = db["scores"]

# supprimer toute les données de la db
supp = mechant.delete_many({})
supp = joueur.delete_many({})
supp = joueur_jouer.delete_many({})


mechants = [
    {"nom": "squelette","pv": 12,"atk": 5},
    {"nom": "zombie", "pv": 18, "atk": 4},
    {"nom": "loup-garou", "pv": 25, "atk": 7},
    {"nom": "demon", "pv": 30, "atk": 10},
    {"nom": "araignee_geante", "pv": 20, "atk": 5}
]
#ajouter les mechants dans la db
ajouter_mechants = mechant.insert_many(mechants)



joueurs = [
    {"nom": "guerrier", "pv": 30, "atk": 17},
    {"nom": "archer", "pv": 20, "atk": 9},
    {"nom": "mage", "pv": 5, "atk": 12},
    {"nom": "assassin", "pv": 18, "atk": 14},
    {"nom": "alchimiste", "pv": 23, "atk": 6},
    {"nom": "chaman", "pv": 22, "atk": 7}
]
#ajouter les joueurs dans la db

# table des joueurs
# nb_joueurs
# point

#menu
    # tant que infini
        # montrer les différent choix
        # demander le choix au joueur et retourner le choix
        


# choix menu            
    #nom du joueur
    #tant que infini
        # metre le choix de menu dans une variable choix
        # si le choix est un nombre et compris entre 1 et 3
            # transformer choix en chaine de caractère
            # si c'est 1 print le choix choisi et lancer choix joueur
                #demander le nom du joueur qui joue
                #écrire lancement du jeu
                #lancer la fonction choix_joueur
            # sinon si c'est 2 lancer leaderboard 
                #écrire entrer dans le leaderbord
                #lancer la fonction leaderboard
            # sinon ecrire quitter
                #break
        #sinon
            # print que le choix n'est pas bon

# leaderbord()
    #récuperer les nom des joueurs et les scores dans une liste et les mettre dans l'ordre coissant en fonctioin des points
    #faire une boucle pour afficher chaque joueur et ses points


#choix_joueur(joueurs_dans_jeu)
    # tant que infini
        # si le nombre de joueur est égal à trois
            # print les joueurs choisis
            # ajouter dans la db les trois joueurs choisi
            #lancer la fonction vague
            #break
        # sinon
            # pour les element de ma liste joueur
                #montrer les elements
            # demander le choix au joueur entre 1 et 6
            # verifier que ce soit un chiffre et que se soit compris entre 1 et 6
                # Convertit la saisie en nombre entier
                # Créer une copie 
                # Supprime l'_id pour pas que ca duplique
                #ajouter le perso dans la liste des perso_choisi
                # afficher le joueur choisi
                # augmenter le nb_joueurs de 1 
            #sinon
                # écrire message d'erreur

# vague 
    #vague en cours
    # personne_restant = 3
    #importer depuis la bd la première personne avec le nom, pv et atk dans personne_combat
    # choisir aléatoirement un monstre dans la db et importer le nom, pv et atk dans monstre_combat
    #print la vague actuelle
    #print le nouveau joueur
    # tant que infini
        #temps de pose
        # monstre_combat(pv) -= personne_combat(atk)
        # print les dégats infligé
        # si monstre_combat(pv) <= 0
            # ajouter 10 point
            # print monstre batue
            #ajout à vagues 1
            #print la vague actuelle
            # choisir aléatoirement un monstre dans la db et importer le nom, pv et atk dans monstre_combat
        #sinon
            #temps de pose
            # personne_combat(pv) -= monstre_combat(atk)
            # print les dégats infligé
            # si personne_combat(pv) <= 0
                #print que le joueur est mort
                # supprimer le personnage de la db
                # retirer à personne_restant 1
                # si personne_restant == 0 
                    # print fin de partie avec les points gagné
                    #envoyer dans la db le nom du joueur avec ses points
                    #return
                #sinon
                    #importer depuis la bd la première personne avec le nom, pv et atk dans personne_combat
                    #print le nouveau joueur



# def main                
    # choix_menu


# main()
