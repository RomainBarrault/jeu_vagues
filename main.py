from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["joueur"]
mechant = db["mechant"]
joueur = db["joueur"]
joueur_jouer = db["joueur_jouer"]

# supprimer toute les données de la db



#ajouter les mechants dans la db



#ajouter les joueurs dans la db


# table des joueurs
# choix
# nb_joueurs



#menu
    # tant que infini
        # montrer les différent choix (jouer, leaderbord, quitter)
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
        # si le nombre de joueur est égal à trois
            # print les joueurs choisis
            # ajouter dans la db les trois joueurs choisi
            #break
        # sinon
            # pour les element de ma liste joueur
                #montrer les elements
            # demander le choix au joueur entre 1 et 6
            # verifier que ce soit un chiffre et que se soit compris entre 1 et 6
                # Convertit la saisie en nombre entier
                # ajouter dans la liste  joueur_jouers le joueur choisi
                # afficher le joueur choisi
                # augmenter le nb_joueurs de 1 
            #sinon
                # écrire message d'erreur

# def main
    #choix_menu



# main()

