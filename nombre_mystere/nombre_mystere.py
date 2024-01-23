from random import randint

nombre_a_choisir = randint(0,100)
nombre_essais = 5

print("** Le jeu du nombre mystere **")

"""
Boucle principale

"""
while nombre_essais > 0:
    print(f"Il te reste {nombre_essais} essai {'s'if nombre_essais > 1 else ''} ")

    """
    saisie de l'utilisateur

    """
    choix_utilisateur = input("Devine le nombre: ")
    if not choix_utilisateur.isdigit():
        print(f"Veuillez entrer un nombre valide.")
        continue

    choix_utilisateur = int(choix_utilisateur)

    if nombre_a_choisir > choix_utilisateur:   
        print(f"Le nombre mystére est plus grannd que {choix_utilisateur}")
    elif nombre_a_choisir < choix_utilisateur:   
        print(f"Le nombre mystere est plus que {choix_utilisateur}")
    else:  

        break

    nombre_essais -= 1

    """
    Gagné ou perdu

    """
    if nombre_essais == 0:
        print(f"Dommage ! le nombre mystere etait {nombre_a_choisir}")
    else:
        print(f"Bravo ! Le nombre mystére etait bien {nombre_a_choisir} ! ")
        print(f"Tu as trouver le nombre en {6 - nombre_essais} essai")

        print("Fin du jeu.")
