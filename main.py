from pymongo import MongoClient
import random
import time
client = MongoClient("mongodb://localhost:27017")
db = client["joueur"]
mechant = db["mechant"]
joueur = db["joueur"]
joueur_jouer = db["joueur_jouer"]

# supprimer toute les données de la db
supp = mechant.delete_many({})
supp = joueur.delete_many({})
supp = joueur_jouer.delete_many({})



#ajouter les mechants dans la db




#ajouter les joueurs dans la db

# table des joueurs
# nb_joueurs



#menu
    # tant que infini
        # montrer les différent choix
        # demander le choix au joueur et retourner le choix
        


# choix menu     
    #tant que infini       
        # metre le choix de menu dans une variable choix
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
        # si le nombre de joueur est égal à trois
            # print les joueurs choisis
            # ajouter dans la db les trois joueurs choisi
            #lancer la fonction vague
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
                    # print fin de partie 
                    #appeler main
                #sinon
                    #importer depuis la bd la première personne avec le nom, pv et atk dans personne_combat
                    #print le nouveau joueur



# def main                
    # choix_menu


# main()
