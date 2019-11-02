#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *
pygame.init()

#LISTE DES VARIABLES

#Longueur de la fenetre
LONGUEUR_FENETRE = 800

#Largeur de la fenetre
HAUTEUR_FENETRE = 650
#Titre de la fenetre
TITRE_FENETRE = "Picross Mania"

#Taille d'un carré
TAILLE_CARRE = 50

#Nom des couleurs
NOIR = (0,0,0)
VERT_PIN = (1,121,111)
CANARD = (4,139,154)
BLANC_CREME = (253, 241, 184)

#Marges (ou bordures)
MARGE_X2 = 197
MARGE_X1 = 350
MARGE_Y2 = 87
MARGE_Y1 = 350

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

