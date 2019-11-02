#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *
from numpy import *
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

# I- NIVEAU 1
#-------------

    #- Taille d'un carré
TAILLE_CARRE_5x5 = 50

# I- NIVEAU 2
#-------------

TAILLE_CARRE_10x10 = 35

#-------------------------------------------------------------------------------
#                              NOM DES COULEURS
#-------------------------------------------------------------------------------

NOIR = (0,0,0)
VERT_PIN = (1,121,111)
CANARD = (4,139,154)
BLANC_CREME = (253, 241, 184)
BLUE_PEGASUS = (49, 111 ,213)

#-------------------------------------------------------------------------------
#                  COORDONNEES DU POINT D'ORIGINE CORRESPONDANT
#                AU POINT EN HAUT A GAUCHE DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

# I- NIVEAU 1
#-------------

X_ORIGINE_5x5 = 350
Y_ORIGINE_5x5 = 350

# I- NIVEAU 2
#-------------

X_ORIGINE_10x10 = 300
Y_ORIGINE_10x10 = 275

#-------------------------------------------------------------------------------
#                                  MARGES
#-------------------------------------------------------------------------------

# I- NIVEAU 1
#-------------

    #- Marge de gauche
MARGE_X1_5x5 = X_ORIGINE_5x5
    #- Marge de droite
MARGE_X2_5x5 = LONGUEUR_FENETRE - X_ORIGINE_5x5
    #- Marge du haut
MARGE_Y1_5x5 = Y_ORIGINE_5x5
    #- Marge du bas
MARGE_Y2_5x5 = HAUTEUR_FENETRE - Y_ORIGINE_5x5

NBR_CARRE_CENTRAL_5x5 = 5

# II- NIVEAU 2
#--------------

    #- Marge de gauche
MARGE_X1_10x10 = X_ORIGINE_10x10
    #- Marge de droite
MARGE_X2_10x10 = LONGUEUR_FENETRE - X_ORIGINE_10x10
    #- Marge du haut
MARGE_Y1_10x10 = Y_ORIGINE_10x10
    #- Marge du bas
MARGE_Y2_10x10 = HAUTEUR_FENETRE - Y_ORIGINE_10x10

NBR_CARRE_CENTRAL_10x10 = 10


#-------------------------------------------------------------------------------
#                       CARACTERISTIQUES DE LA MATRICE
#-------------------------------------------------------------------------------

# I- NIVEAU 1
#-------------

    #- Nombre de lignes dans la matrice
LIGNES_5x5 = 5
    #- Nombre de colonnes dans la matrice
COLONNES_5x5 = 5

    #- Hauteur de la matrice representant la grille de jeu
H_5x5 = COLONNES_5x5
    #- Largeur de la matrice representant la grille de jeu
L_5x5 = LIGNES_5x5

MATRICE_GRILLE_5x5 = zeros((LIGNES_5x5, COLONNES_5x5))

# I- NIVEAU 2
#-------------

    #- Nombre de lignes dans la matrice
LIGNES_10x10 = 10
    #- Nombre de colonnes dans la matrice
COLONNES_10x10 = 10

    #- Hauteur de la matrice representant la grille de jeu
H_10x10 = COLONNES_10x10
    #- Largeur de la matrice representant la grille de jeu
L_10x10 = LIGNES_10x10

MATRICE_GRILLE_10x10 = zeros((LIGNES_10x10, COLONNES_10x10))

#-------------------------------------------------------------------------------
#     CENTRAGE DES INDICATIONS AU-DESSUS ET A GAUCHE DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

# Les indications sont centrées grace aux variables ci dessous dans les fonctions
# "Afficher_Indic_Haut" et "Afficher_Indic_Gauche"

DIVISEUR_5x5 = 4
DIVISEUR_10x10 = 10
