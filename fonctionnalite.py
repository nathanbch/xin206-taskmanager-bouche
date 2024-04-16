def charger_taches():
    with open("tache.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

def sauvegarder_taches(taches):
    with open("tache.txt", "w") as file:
        for tache in taches:
            file.write(tache + "\n")

def ajouter_tache(taches):
    nouvelle_tache = input("Entrez la nouvelle tâche : ")
    taches.append(nouvelle_tache)
    print("Tâche ajoutée avec succès.")

def supprimer_tache(taches):
    afficher_taches(taches)
    index = int(input("Entrez l'index de la tâche à supprimer : ")) - 1
    if 0 <= index < len(taches):
        taches.pop(index)
        print("Tâche supprimée avec succès.")
    else:
        print("Index invalide.")

def afficher_taches(taches):
    if not taches:
        print("\nAucune tâche.")
    else:
        print("\nListe des tâches :")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache}") 

def marquer_comme_terminee(taches):
    afficher_taches(taches)
    index = int(input("Entrez l'index de la tâche terminée : ")) - 1
    if 0 <= index < len(taches):
        taches[index] += " (Terminée)"
        print("Tâche marquée comme terminée avec succès.")
    else:
        print("Index invalide.")

