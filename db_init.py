from pymongo import MongoClient


def init_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client["joueur"]

    mechant = db["mechant"]
    joueur = db["joueur"]
    joueur_jouer = db["joueur_jouer"]

    # Nettoyage des collections (on garde "scores" intact pour le leaderboard)
    mechant.delete_many({})
    joueur.delete_many({})
    joueur_jouer.delete_many({})

    mechants = [
        {"nom": "squelette", "pv": 12, "atk": 5},
        {"nom": "zombie", "pv": 18, "atk": 4},
        {"nom": "loup-garou", "pv": 25, "atk": 7},
        {"nom": "demon", "pv": 30, "atk": 10},
        {"nom": "araignee_geante", "pv": 20, "atk": 5},
    ]

    joueurs = [
        {"nom": "guerrier", "pv": 30, "atk": 17},
        {"nom": "archer", "pv": 20, "atk": 9},
        {"nom": "mage", "pv": 5, "atk": 12},
        {"nom": "assassin", "pv": 18, "atk": 14},
        {"nom": "alchimiste", "pv": 23, "atk": 6},
        {"nom": "chaman", "pv": 22, "atk": 7},
    ]

    mechant.insert_many(mechants)
    joueur.insert_many(joueurs)

    print("Base de données initialisée avec succès.")
    client.close()


if __name__ == "__main__":
    init_db()