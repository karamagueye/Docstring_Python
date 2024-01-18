import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un element a la liste 
2: Retirer un element de la liste 
3: Afficher la liste 
4: Vider la liste 
5: Quitteer
? Votre choix : 

"""

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print(f"Veillez choisir un option valide ")
        continue

    if user_choice == "1":
        item = input("Entrer le nom d'un element a ajouter a la liste de courses: ")
        LISTE.append(item)
        print(f"L'element {item} a bie été ajoute a la liste.")
    elif user_choice == "2":
        item = input(f"Entrez le nom de l'element a retirer de la liste de course: ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'element {item} a bien été supprimer de la lite.")
        else:
            print(f"L'element {item} n'est pas dans la liste.")
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de votre liste: ")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")

            else:
                print(f"Votre liste ne contient aucun elemenet.")
        elif user_choice == "4":
            LISTE.clear()
            print(f"La liste a été vier.")
        elif user_choice == "5":
            print(f"A bientot !")
            sys.exit()
