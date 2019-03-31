import pygame
import numpy
from pionnoir import pion_noir
from pionblanc import pion_blanc
from pprint import pprint

#PARAM GRAPHIQUE----
cellsize = 100
abs = 100
ord = 100
width = 100
height = 100
#------------------

#------COLOR
white = (255,255,255)
blue = (0,0,255)
green = (0,125,0)
black = (0,0,0)
brown = (210,105,30)
#----------------

#PYGAME GUI
gamedisplay = pygame.display.set_mode(( cellsize*7, cellsize*7))#creation map en 8x8
gamedisplay.fill(white)#Fond blanc
pygame.display.set_caption("Squadro Board")#non de la fenetre
turn = 0 #tour du joueur
#-----------


#INIT VALEUR BACKEND----
board = numpy.zeros((7,7))#tableau du jeu
list_pionnoir = []#liste des pions noirs
list_pionblanc =[]#liste des pions blanc

#------INIT BACK END-------
def init_pion(board):
    """Initialise le back end"""
    for i in range (1,6):
        new_pion_noir = pion_noir(i) #Affectation nouveau pion
        new_pion_noir.set_pos_case((i, 0))#On initialise ses valeurs de cases
        board[new_pion_noir.get_val(), 0] = new_pion_noir.get_type() #on affiche son type dans le tableau
        list_pionnoir.append(new_pion_noir)#On ajoute le pion dans la liste


        new_pion_blanc = pion_blanc(i)
        new_pion_blanc.set_pos_case((6, i))
        board[6, new_pion_blanc.get_val()] = new_pion_blanc.get_type()
        list_pionblanc.append(new_pion_blanc)

init_pion(board)
print(board)
#-------------------

#---- Atribution de valeur unique
pion_blanc_1,pion_blanc_2,pion_blanc_3,pion_blanc_4,pion_blanc_5 = list_pionblanc
pion_blanc_1,pion_noir_2,pion_noir_3,pion_noir_4,pion_noir_5 = list_pionnoir
list_pions = list_pionnoir + list_pionblanc
print(pion_blanc_1.get_val())
#---------




#---- dessin de la map
def map_init():
    for i in range(0, 7):
        for j in range(0, 7):
            pygame.draw.rect(gamedisplay, brown, (i * abs, j * ord, cellsize, cellsize), 0)  # On fait les cases

            pygame.draw.line(gamedisplay, black, (0, j * ord), (700, j * ord), 3)  # Ligne Horizontale
            pygame.draw.line(gamedisplay, black, (i * abs, 0), (i * abs, 700), 3)  # Ligne Verticale0,
    for i in range(1, 6):
        pygame.draw.circle(gamedisplay, black, (cellsize // 2, i * ord + 50), 20)
        pygame.draw.circle(gamedisplay, white, ((i) * abs + cellsize // 2, 650), 20)
map_init()

def init_rule():
    """ Afficher les regles de déplacement des pions du jeu"""
    max_case = 6
    for i in range(1,7):

        if i == 1 :
            for x in range(0, 3):
                pygame.draw.circle(gamedisplay, blue, (cellsize // 10+ x* cellsize//4,
                                                      i * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, ((i) * abs + cellsize // 10,
                                                       x * cellsize // 4 + 640), 7)
                pygame.draw.circle(gamedisplay, blue, (i +2 * ord + cellsize // 10,
                                                       cellsize // 10 + x * cellsize // 4), 7)
                pygame.draw.circle(gamedisplay, blue, (i + 4 * ord + cellsize // 10,
                                                       cellsize // 10 + x * cellsize // 4), 7)
                pygame.draw.circle(gamedisplay, blue, (cellsize * (i+5)+ x* cellsize//4 + cellsize//8,
                                                       (i + 3) * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, (cellsize * (i + 5) + x * cellsize // 4 + cellsize // 8,
                                                       (i + 1) * ord + cellsize // 5), 7)

        elif i == 2 :
            for x in range(0, 1):
                pygame.draw.circle(gamedisplay, blue, (cellsize // 10+ x* cellsize//4,
                                                       i * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, ((i) * abs + cellsize // 10,
                                                       x * cellsize // 4 + 640), 7)
                pygame.draw.circle(gamedisplay, blue, ((i -1) * ord + cellsize // 10,
                                                       cellsize // 10 + x * cellsize // 4), 7)
                pygame.draw.circle(gamedisplay, blue, (cellsize * (i+4) + x * cellsize // 4 + cellsize // 8,
                                                       (i +3 ) * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, (cellsize * (i + 4) + x * cellsize // 4 + cellsize // 8,
                                                       ord + cellsize // 5), 7)

        elif i == 3 :
            for x in range(0, 2):
                pygame.draw.circle(gamedisplay, blue, (cellsize // 10+ x* cellsize//4,
                                                    i * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, ((i) * abs + cellsize // 10,
                                                    x * cellsize // 4 + 640), 7)
                pygame.draw.circle(gamedisplay, blue, (i + 3 * ord + cellsize // 10,
                                                       cellsize // 10 + x * cellsize // 4), 7)

                pygame.draw.circle(gamedisplay, blue, (cellsize * (i+3) + x * cellsize // 4 + cellsize // 8,
                                                       (i ) * ord + cellsize // 5), 7)
        elif i == 4 :
            for x in range(0, 1):
                pygame.draw.circle(gamedisplay, blue, (cellsize // 10+ x* cellsize//4,
                                                       i * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, ((i) * abs + cellsize // 10,
                                                       x * cellsize // 4 + 640), 7)
                pygame.draw.circle(gamedisplay, blue, (cellsize // 9 * (i + 6) + x * cellsize // 4 + cellsize * 4,
                                                        cellsize //9), 7)


        elif i == 5 :
            for x in range(0, 3):
                pygame.draw.circle(gamedisplay, blue, (cellsize // 10+ x* cellsize//4,
                                                       i * ord + cellsize // 5), 7)
                pygame.draw.circle(gamedisplay, blue, ((i) * abs + cellsize // 10,
                                                       x * cellsize // 4 + 640), 7)
init_rule()

#-------------
def drawPionnoir(pos) :
    """Permet de dessiner un cercle NOIR sur l'ecran """
    return pygame.draw.circle(gamedisplay,black,pos,20)

def drawPionBlanc(pos):
    """Permet de dessiner un cercle Blanc sur l'ecran """
    return pygame.draw.circle(gamedisplay,white,pos,20)

def removecircle(pos):
    """
    :param pos:
    :return: Pion supprimer FRONT END
    """
    return pygame.draw.circle(gamedisplay,brown,pos,20)

def getPosCase():
    pos = pygame.mouse.get_pos()
    x, y = pos
    case_x = x // width
    case_y = y // height
    return case_x,case_y


def replacepion(pion,case_x,case_y):
    for pionsuppr in list_pions:  # On parcours à nouveeau la liste pour
        # obtenir une correspodance entre le pion jouer et les pions restant
        case_a, case_b = pionsuppr.get_pos_case()
        type = pionsuppr.get_type()
        if (case_x, case_y) == (case_a, case_b) and type != pion.get_type():
            # SI on obtient une correspondant et que les pions ne sont pas du même type
            pionsuppr.goBack()  # On remet à 0 la position du pion
            case_back_x, case_back_y = pionsuppr.get_pos_case()  # affectation de ses valeurs
            board[case_back_y, case_back_x] = type  # On reaffecte sa position en back end

            if type == 1:  # On affiche la position du nouveau pion à l'arrière
                drawPionnoir((case_back_x * cellsize + 50, case_back_y * cellsize + 50))
            else:
                drawPionBlanc((case_back_x * cellsize + 50, case_back_y * cellsize + 50))
            print("ok")

def get_pion():
    """
    Permet de récupérer un pion et de le déplaceer
    :return:
    """
    case_x,case_y = getPosCase()#Case selectionné sur clique
    print("tu as cliqué la ({},{})".format(case_x,case_y))
    for pion in list_pions: #Pour chaque pion dans la liste
    #on parcour la liste de pion pour déterminer une oorrespondance par case

        case_a,case_b  = pion.get_pos_case() #On récupère la position du pion par itération

        if (case_x,case_y) == (case_a,case_b): # correspondance case cliqué et case pion dans liste
            print(pion.get_pos_case())
            type = pion.get_type()
            #if turn % 2 == False and type == 1 : #Joue en premier, impair que sur les pions Noir

            #----DELETE OLD POS-------
            old_case_x, old_case_y = pion.get_pos_case() #Save old pos
            board[old_case_y,old_case_x] = 0 #Delete old Pos BACK END
            #------------------------

            #----MOVE IN NEW POS----
            pion.move() #Move pion
            case_x,case_y = pion.get_pos_case() #Get new pos pion X, Y
            #-----------------------

            #MAKE PION GO BACK--------------------
            replacepion(pion,case_x,case_y)
            #------------------------------------

            board[case_y,case_x] = pion.get_type()#Affect new POS in BACK END
            #-----------------------

            #---FRONT
            if pion.get_type() == 1 : #¨Pion noir
                drawPionnoir((case_x*cellsize+50,case_y*cellsize+50)) #Draw
            else :# -> Pion Blanc
                drawPionBlanc((case_x*cellsize+50,case_y*cellsize+50))#Draw
            removecircle((old_case_x*cellsize+50,old_case_y*cellsize+50))#Delete old Circle
            #------------------

            print(pion.get_pos_case())
            print(board)



def main_fonction():
    """Fonction principal du jeu,
    c'est une boucle infiniue rafraichissant la page à chaque action"""
    quitGame = False
    global  turn
    while not  quitGame : #boucle infinie pour le jeu

            for event in pygame.event.get(): #on recupere tous les event
                if event.type == pygame.QUIT:#si un event correspond à quitter
                    quitGame = True #on arrete la boucle infinie
                    pygame.quit() #on quitte le jeu
                if event.type == pygame.MOUSEBUTTONUP:  # dès qu'on relache la souris
                    get_pion()
                    turn = turn + 1
            pygame.display.update() #udapte

if __name__ == '__main__':
    """MAIN"""
    main_fonction()



