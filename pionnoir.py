import pygame

height, width = 100, 100

class pion_noir:

    def  __init__(self,val):

        self.type = 1
        self.case_x = 0
        self.case_y = 0
        self.val = val
        self.Max = False
        self.max_case = 6
        self.min_case = 0
    def get_pos_pion(self):
        """ Retourne la position du pion e
        :return :la position du pion en x,y
        """
        # recuperer la position quand on click
        pos = pygame.mouse.get_pos()
        return pos

    def set_pos_case(self,pos):
        x, y = pos
        self.case_x = x
        self.case_y = y
    def set_max(self,bool):
        self.Max = bool

    def set_val(self,case_y):
        """
        Permet d'optenir la valeur du range d'un pion noir
        :param case_y:
        :return: le rang du pion noir
        """
        self.val = case_y
    def premove(self):
        pass

    def goBack(self):
        self.case_y = 0
    def move(self):
        if self.case_y == self.max_case:
            self.set_max(True)
        if self.case_y == self.min_case:
            self.set_max(False)
        if self.Max == True :
            if self.val == 1 or self.val == 5:
                self.case_y = self.case_y - 1
            elif self.val == 2 or self.val == 4:
                self.case_y = self.case_y - 3
            if self.val == 3:
                self.case_y = self.case_y - 2

        else :
            if self.val == 1 or self.val == 5:
                self.case_y = self.case_y + 3
            elif self.val == 2 or self.val == 4:
                self.case_y = self.case_y + 1
            if self.val == 3:
                self.case_y = self.case_y + 2
    def get_pos_case(self):
        """
        Retourne les coordonnées x et y du pion dans le tableau
        :return: la position du pion
        """
        return self.case_y, self.case_x

    def get_type(self):
        """

        :return: Le type du pion, blanc ou noir
        """
        return self.type
    def get_val(self):
        return self.val

    def get_max(self):
        return self.Max

