taches = []


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append(titre)
    print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
        return
    for i in range(len(taches)):
        print(f"{i + 1}. {taches[i]}")


def rechercher_tache():
    mot = input("Mot-clé à rechercher : ").strip().lower()
    trouve = False
    for i in range(len(taches)):
        if mot in taches[i].lower():
            print(f"{i + 1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tâche ne correspond à ce mot-clé.")


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


choix = ""
while choix != "0":
    afficher_menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Option invalide, veuillez choisir 0, 1, 2 ou 3.")