#VERSION SCRIPT - à passer en POO
# Definition de la grille  -> future classe Environnement
import random
import time

t= 0  # temps
"""
Paramètres utilisateur :  largeur / longueur de la grille 
Attribution des cases :
        0 = vide
        1 = thon
        2 = requin

On initialise 2 grilles : une première où on initialise l'environnement 0 / 1 / 2
"""

largeur = 5
longueur = 5

# Initialisation de la grille
grille = [[random.randint(0,2) for i in range(longueur)] for j in range(largeur)]

# 0 = vide / 1 = tuna / 2 = shark
new_grille = [[0 for i in range(longueur)] for j in range(largeur)]

while t < 10:   
    for x in range(largeur):
        for y in range(longueur):   
            direction = random.choice(["left", "right", "up", "down"])
            if direction == "up":
                new_grille[x][y] = grille[x-(largeur-1)][y]   #up
            if direction == "down":
                new_grille[x][y] = grille[x-1][y]   #down
            if direction == "left":
                new_grille[x][y] = grille[x][y-(longueur-1)]   #left
            if direction == "right":
                new_grille[x][y] = grille[x][y-1]  #right

    print(f"t = {t}")

    for ligne in grille:        #affichage des élements de la grille
        print(ligne)
    print(longueur*3*'_')
    for ligne in new_grille:
        print(ligne)       
    print(longueur*3*'_')
    time.sleep(0.25)
    t +=1
