"""Ce module contient la classe de Pion blanc"""

class pion_blanc:

    def  __init__(self,val):

        self.type = 2#Blanc
        self.case_x = 0#case x
        self.case_y = 0#case y
        self.val = val# valeur correspondante à la case attribuée

        self.Max = False #permet determiner les limites du terrain
        self.max_case = 0#case correspondante aux limites du terrain
        self.min_case = 6#
    def set_pos_case(self,pos):
        """
        Cette fonction permet au pion d'être a attribué
        à une case du tableau jeu
        :param pos: la poisition de la sourie lors du clique
        !!! WARNING !!! les tableaux numpys sont inversés,
        Y correspond à l'abscisse
        X correspond à l'ordonnée
        """
        x, y = pos
        self.case_y = y#Abscisse
        self.case_x = x#Ordonnée

    def set_val(self,case_x):
        """
        Permet d'optenir la valeur du range d'un pion noir
        :param case_y:
        :return: le rang du pion noir
        """
        self.val = case_x
    def set_max(self,bool):
        """Permet de paramétrer la variable max
         en temps que booléen
        :param MAX"""
        self.Max = bool
    def move(self):
        """Cette fonction permet d'établir le mouvement
        du pion dans le tableau en modifiant la valeur de ses cases"""
        if self.case_x == self.max_case:
            self.set_max(True)
        if self.case_x == self.min_case:
            self.set_max(False)
        if self.Max == True :
            if self.val == 1 or self.val == 5:#determine sa colonne
                self.case_x = self.case_x + 1#on y incremente une valeur
            elif self.val == 2 or self.val == 4:
                self.case_x = self.case_x + 3
            if self.val == 3:
                self.case_x = self.case_x + 2
        else :
            if self.val == 1 or self.val == 5:
                self.case_x = self.case_x - 3
            elif self.val == 2 or self.val == 4:
                self.case_x = self.case_x - 1
            if self.val == 3:
                self.case_x = self.case_x - 2
    def goBack(self):
       self.case_x = 6


    def get_pos_case(self):
        """
        Retourne les coordonnées x et y du pion dans le tableau
        :return: la position du pion
        """
        return self.case_y, self.case_x

    def get_type(self):
        """
        Renvoie Le type du pion, ici étant blanc, la valeur
        du pion blanc est deux
        :return: 2
        """
        return self.type
    def get_val(self):
        """
        La valeur de la position du pion
        :return:
        """
        return self.val

    def get_max(self):
        """
        Getter renvoie la valeur du booleen MAX
        Dans le but de determiner si le pion est dans sa phase
        de retour ou non
        :return:
        """
        return self.Max
