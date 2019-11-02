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

    #(I) Dimensions de la fenêtre
    #=============================

        #- Longueur de la fenetre
LONGUEUR_FENETRE = 800
    #- Hauteur de la fenetre
HAUTEUR_FENETRE = 650
    #- Titre de la fenetre
TITRE_FENETRE = "Picross Mania"

#-------------------------------------------------------------------------------
#                  DIMENSION DES CONSTITUANTS DE LA GRILLE
#-------------------------------------------------------------------------------

    #- Taille d'un carré
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

X_ORIGINE = 300
Y_ORIGINE = 200

#-------------------------------------------------------------------------------
#                                  MARGES
#-------------------------------------------------------------------------------

    #- Marge de gauche
MARGE_X1 = X_ORIGINE
    #- Marge de droite
MARGE_X2 = LONGUEUR_FENETRE - X_ORIGINE
    #- Marge du haut
MARGE_Y1 = Y_ORIGINE
    #- Marge du bas
MARGE_Y2 = HAUTEUR_FENETRE - Y_ORIGINE

#-------------------------------------------------------------------------------
#                       CARACTERISTIQUES DE LA MATRICE
#-------------------------------------------------------------------------------

    #- Nombre de lignes dans la matrice
LIGNES = 5
    #- Nombre de colonnes dans la matrice
COLONNES = 5

    #- Hauteur de la matrice representant la grille de jeu
H = COLONNES
    #- Largeur de la matrice representant la grille de jeu
L = LIGNES
