import random
import time

class Environment:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur

    def afficher_grille(self):
        grille = [[random.randint(0,2) for i in range(self.longueur)] for j in range(self.largeur)]
        new_grille = [[0 for i in range(self.longueur)] for j in range(self.largeur)]
        for ligne in grille:        #affichage des élements de la grille
            print(ligne)
        print(self.longueur*3*'_')
        for ligne in new_grille:
            print(ligne)       
        print(self.longueur*3*'_')
        time.sleep(0.25)