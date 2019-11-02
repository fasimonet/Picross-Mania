#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *
pygame.init()

#===============================================================================
#                            LISTE DES VARIABLES
#===============================================================================

#-------------------------------------------------------------------------------
#                       CARACTERISTIQUES DE LA FENETRE
#-------------------------------------------------------------------------------

    #- longueur de la fenetre
LONGUEUR_FENETRE = 800
    #- largeur de la fenetre
HAUTEUR_FENETRE = 650
    #- titre de la fenetre
TITRE_FENETRE = "Picross Mania"

#Taille d'un carré
TAILLE_CARRE = 50

#-------------------------------------------------------------------------------
#                              NOM DES COULEURS
#-------------------------------------------------------------------------------

NOIR = (0,0,0)
VERT_PIN = (1,121,111)
CANARD = (4,139,154)
BLANC_CREME = (253, 241, 184)

#-------------------------------------------------------------------------------
#                  COORDONNEES DU POINT D'ORIGINE CORRESPONDANT
#                AU POINT EN HAUT A GAUCHE DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

ABSCISSE_ORIGINE = 350
ORDONNEE_ORIGINE = 300

#-------------------------------------------------------------------------------
#                                  MARGES
#-------------------------------------------------------------------------------

MARGE_X2 = 200
MARGE_X1 = 350
MARGE_Y2 = 100
MARGE_Y1 = 250 #300

"""#On attribue a SOURIS_X l'abscisse de la position de la souris
SOURIS_X = event.pos[0]
#On attribue a SOURIS_Y l'ordonnée de la position de la souris
SOURIS_Y = event.pos[1]"""

"""#Boucle de récupération des coordonnées
if SOURIS_X >= (LONGUEUR_FENETRE - MARGE_X1) and SOURIS_X <= (LONGUEUR_FENETRE - MARGE_X2) and SOURIS_Y >= (HAUTEUR_FENETRE - MARGE_Y1) and SOURIS_X <= (HAUTEUR_FENETRE - MARGE_Y2):

    #Coordonnées des cases de la grille centrale
    CASE_X = (SOURIS_X - MARGE_X1)//TAILLE_CARRE
    CASE_Y = (SOURIS_Y - MARGE_Y1)//TAILLE_CARRE"""

#MATRICE
#Nombre de lignes dans la matrice
LIGNES = 5
#Nombre de colonnes dans la matrice
COLONNES = 5

#Hauteur de la matrice representant la grille de jeu
H = COLONNES
#Largeur de la matrice representant la grille de jeu
L = LIGNES
"""
#Cases ligne 1
Rect_case_zero_zero = pygame.Rect(350, 350, 50, 50)
Rect_case_zero_un = pygame.Rect(400, 350, 50, 50)
Rect_case_zero_deux = pygame.Rect(450, 350, 50, 50)
Rect_case_zero_trois = pygame.Rect(500, 350, 50, 50)
Rect_case_zero_quatre = pygame.Rect(550, 350, 50, 50)

#case ligne 2
Rect_case_un_zero = pygame.Rect(350, 400, 50, 50)
Rect_case_un_un = pygame.Rect(400, 400, 50, 50)
Rect_case_un_deux = pygame.Rect(450, 400, 50, 50)
Rect_case_un_trois = pygame.Rect(500, 400, 50, 50)
Rect_case_un_quatre = pygame.Rect(550, 400, 50, 50)

#case ligne 3
Rect_case_deux_zero = pygame.Rect(350, 450, 50, 50)
Rect_case_deux_un = pygame.Rect(400, 450, 50, 50)
Rect_case_deux_deux = pygame.Rect(450, 450, 50, 50)
Rect_case_deux_trois = pygame.Rect(500, 450, 50, 50)
Rect_case_deux_quatre = pygame.Rect(550, 450, 50, 50)

#case ligne 4
Rect_case_trois_zero = pygame.Rect(350, 500, 50, 50)
Rect_case_trois_un = pygame.Rect(400, 500, 50, 50)
Rect_case_trois_deux = pygame.Rect(450, 500, 50, 50)
Rect_case_trois_trois = pygame.Rect(500, 500, 50, 50)
Rect_case_trois_quatre = pygame.Rect(550, 500, 50, 50)

#case ligne 5
Rect_case_quatre_zero = pygame.Rect(350, 550, 50, 50)
Rect_case_quatre_un = pygame.Rect(400, 550, 50, 50)
Rect_case_quatre_deux = pygame.Rect(450, 550, 50, 50)
Rect_case_quatre_trois = pygame.Rect(500, 550, 50, 50)
Rect_case_quatre_quatre = pygame.Rect(550, 550, 50, 50)"""