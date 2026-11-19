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
ajouter_joueurs = joueur.insert_many(joueurs)

# table des joueurs
joueur_jouers = []
# nb_joueurs
nb_joueurs = 0
# point
point = 0

#menu
def menu():
    # point
    point = 0
    # nb_joueurs
    nb_joueurs = 0
    # tant que infini
    while True:
        # montrer les différent choix
        print("=====MENU=====")
        print("1 Jouer")
        print("2 Leaderbord")
        print("3 Quitter")
        # demander le choix au joueur et retourner le choix
        return input("Faire un choix entre 1 et 3: ")
        


# choix menu            
def choix_menu():
    #nom du joueur
    nom_du_joueur = ""
    #tant que infini
    while True:
        # metre le choix de menu dans une variable choix
        choix = menu()
        # si le choix est un nombre et compris entre 1 et 3
        if choix.isdigit() and 1<= int(choix) <=3:
            # transformer choix en chaine de caractère
            choix = int(choix)
            # si c'est 1 print le choix choisi et lancer choix joueur
            if choix == 1:
                #demander le nom du joueur qui joue
                nom_du_joueur = input("Entrez votre nom:")
                #écrire lancement du jeu
                print("==========Lancement du jeu=========="),
                #lancer la fonction choix_joueur
                choix_joueur(nb_joueurs,joueur_jouer,nom_du_joueur)
            # sinon si c'est 2 lancer leaderboard 
            elif choix==2:
                #écrire entrer dans le leaderbord
                print("==========leaderbord=========="),
                #lancer la fonction leaderboard
                leaderbord()
            # sinon ecrire quitter
            else :
                print("Quitter")
                #break
                break
        #sinon
        else:
            # print que le choix n'est pas bon
            print("choix invalide")

# leaderbord()
def leaderbord():
    #récuperer les nom des joueurs et les scores dans une liste et les mettre dans l'ordre coissant en fonctioin des points
    classement = list(scores.find().sort("points", -1))
    #faire une boucle pour afficher chaque joueur et ses points
    for i in classement:
        print(i["nom"], ":", i["points"], "points")


#choix_joueur(joueurs_dans_jeu)
def choix_joueur(nb_joueurs,joueur_jouer,nom_du_joueur):
    # tant que infini
    while True:
        # si le nombre de joueur est égal à trois
        if nb_joueurs == 3:
            # print les joueurs choisis
            print("votre équipe final :",joueur_jouers)
            # ajouter dans la db les trois joueurs choisi
            joueur_jouer.insert_many(joueur_jouers)
            #lancer la fonction vague
            vague(point,nom_du_joueur)
            #break
            break
        # sinon
        else:
            # pour les element de ma liste joueur afficher sans l'id
            for element in joueur.find({}, {"_id": 0}):
                #montrer les elements
                print(element)
            # demander le choix au joueur entre 1 et 6
            joueur_final = input("Faire un choix entre 1 et 6 :" )
            # verifier que ce soit un chiffre et que se soit compris entre 1 et 6
            if joueur_final.isdigit() and 1<= int(joueur_final) <=6:
                # Convertit la saisie en nombre entier
                index = int(joueur_final) - 1
                # Créer une copie 
                perso_choisi = joueurs[index].copy()
                # Supprime l'_id pour pas que ca duplique
                perso_choisi.pop("_id", None)  
                #ajouter le perso dans la liste des perso_choisi
                joueur_jouers.append(perso_choisi)
                # afficher le joueur choisi
                print("vous avez choisi: ",perso_choisi["nom"])
                # augmenter le nb_joueurs de 1 
                nb_joueurs = nb_joueurs +1
            #sinon
            else:
                # écrire message d'erreur
                print("choix invalide")

# vague 
def vague(point,nom_du_joueur):
    #vague en cours
    vagues = 1
    # personne_restant = 3
    personne_restant = 3
    #importer depuis la bd la première personne avec le nom, pv et atk dans personne_combat
    personne_combat = joueur_jouer.find_one({}, {"_id": 0, "nom": 1, "pv": 1, "atk": 1})
    # choisir aléatoirement un monstre dans la db et importer le nom, pv et atk dans monstre_combat
    monstre_combat = list(mechant.aggregate([{"$sample": {"size": 1}},{"$project": {"_id": 0, "nom": 1, "pv": 1, "atk": 1}}]))[0]
    #print la vague actuelle
    print("Entrer dans la vague",vagues)
    #print le nouveau joueur
    print(personne_combat["nom"], "entre dans le combat")
    # tant que infini
    while True:
        # si personne_restant == 0 
        if personne_restant == 0:
            # print fin de partie avec les points gagné
            print(nom_du_joueur,"c'est la fin de la partie, vous avez remportez : ",point,"points")
            #envoyer dans la db le nom du joueur avec ses points
            scores.insert_one({"nom": nom_du_joueur,"points": point})
            #vider la liste des joueurs jouer 
            joueur_jouers.clear()  
            # vider les joueurs jouer dans mongodb
            joueur_jouer.delete_many({})
            #return
            return
        #sinon
        else:
            # si personne_combat(pv) <= 0
            if personne_combat["pv"] <= 0:
                #importer depuis la bd la première personne avec le nom, pv et atk dans personne_combat
                personne_combat = joueur_jouer.find_one({}, {"_id": 0, "nom": 1, "pv": 1, "atk": 1})
                #print le nouveau joueur
                print(personne_combat["nom"], "entre dans le combat")
            #lancer le combat et mettre à jours l'état de la partie
            monstre_combat, vagues, point, personne_restant = combat(personne_combat, monstre_combat, vagues, point, personne_restant)

#def combat
def combat(personne_combat,monstre_combat,vagues,point, personne_restant):
    #tant que infini
    while True:
        #temps de pose
        time.sleep(2)
        # monstre_combat(pv) -= personne_combat(atk)
        monstre_combat ["pv"] -= personne_combat["atk"]
        # print les dégats infligé
        print(personne_combat["nom"],"a fait", personne_combat["atk"],"de dégat au ", monstre_combat["nom"],"il lui reste ", monstre_combat["pv"] )
        # si monstre_combat(pv) <= 0
        if monstre_combat["pv"] <= 0:
            # ajouter 10 point
            point = point +10
            # print monstre batue
            print("Monstre batue, vous avez gagnez : 10 points")
            #ajout à vagues 1
            vagues = vagues +1
            #print la vague actuelle
            print("Entrer dans la vague",vagues)
            # choisir aléatoirement un monstre dans la db et importer le nom, pv et atk dans monstre_combat
            monstre_combat = list(mechant.aggregate([{"$sample": {"size": 1}},{"$project": {"_id": 0, "nom": 1, "pv": 1, "atk": 1}}]))[0]
            #return les données monstre_combat, vagues, point, personne_restant
            return monstre_combat, vagues, point, personne_restant
        #sinon
        else:
            #temps de pose
            time.sleep(2)
            # personne_combat(pv) -= monstre_combat(atk)
            personne_combat ["pv"] -= monstre_combat["atk"]
            # print les dégats infligé
            print(monstre_combat["nom"],"a fait", monstre_combat["atk"],"de dégat au ", personne_combat["nom"],"il lui reste ", personne_combat["pv"] )
            # si personne_combat(pv) <= 0
            if personne_combat["pv"] <= 0:
                #print que le joueur est mort
                print(personne_combat["nom"],"est mort")
                # supprimer le personnage de la db
                joueur_jouer.delete_one({"nom": personne_combat["nom"]})
                # retirer à personne_restant 1
                personne_restant = personne_restant - 1
                #return
                return monstre_combat, vagues, point, personne_restant
# def main                
def main():
    # choix_menu
    choix_menu()


# main()
main()
