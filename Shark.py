import random
class Shark:
    def __init__(self, energy, position, die ) -> None:
        self.position = position
        self.energy = 10
        # self.die = die



    
    def check(self):
        east_position = (self.position[0]+1, self.position[1])
        west_position = (self.position[0]-1, self.position[1])
        north_position = (self.position[0], self.position[1]+1)
        south_position = (self.position[0], self.position[1]-1)

        position_voisine = [east_position, west_position, north_position, south_position]

    
        for i in position_voisine :
             
             controle_case = grid[i[0]][i[1]] 

             if controle_case == "0" :
                  self.energy -= 1
                #   if self.energy <= 0 :
                    #   self.die()
                      
                  self.position = i
                  break

             elif controle_case == "1":
                  self.energy += 1
                  self.position = i
                  break
             else : 
                  pass
             
        
                  

     #def grille():
        # for i in range(0,5):
        #     for j in range(0,5):
        #         a = random.randint(0,1)
        #         print(f"{a}", end = "")
        #     print()
    
    # def energy(self):
    #     if self.energy == 1 :
    #         print("the shark is hungry, one life left !")
    #     elif self.energy <= 1 :
    #         print("shark is dead, end of game")
        




        #for i in position_voisine :
            #  if i == "0" :
            #       case vide donc mouvement aléatoire et -1 NRJ
            #  elif i == "1":
            #       case thon donc mange et +1 NRJ (-1 pour mouvement +2 pour manger)
            #  else : 
            #       case requin donc pas de mouvement
             



    
    # def move (self):

    #     east_position = (self.position[0]+1, self.position[1])
    #     west_position = (self.position[0]-1, self.position[1])
    #     north_position = (self.position[0], self.position[1]+1)
    #     south_position = (self.position[0], self.position[1]-1)

    #     if east_position or west_position or north_position or south_position is 



'''

check de la position

si 1 des 4 positions vide = deplacement
'''

# initial_position = (self.position[0], self.position[1])







# def reproduce ():
#         pass





'''

class Fish:
    def __init__(self, position: tuple):
        self.position = position

     je commence pour scanner les positions adjacentes
    # je code le mouvement ici : pas de problème d'import
    # je crée un dictionnaire un sous de cases adjacentes

    def check_adjacent_places(self):
        # Positions adjacentes
        return adjacent_positions

    # je crée le mouvement perpétuel
    def move(self, ecosystem: dict):
        # faire bouger le poisson vers une case vide

        # quelles sont les emplacements vides dans les positions adjacentes fournies par le scan
        # element = (position_1, ecosystem[position_1])
        
       # un des éléments prend la valeur Thon ou Requin et la position initiale à une valeur qui passe à None
        if len(elements) != 0:
            # déplacer le poisson à la nouvelle position
            # mettre un None à l'ancienne position

'''


# class Ocean :
#     def __init__(self, grille : list) -> None:
#          self.grille = list(grille)

#     def mouvement(self):
#         for i in range(0,5)


# for i in range (0,5):
#     for j in range (0,5):
#         print(([i][j]), end = " ")
#     print()