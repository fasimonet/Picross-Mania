# Créé par Fabien et Quentin, le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *
pygame.init()

def Grille_haut(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE DU HAUT OU SONT NOTEES DES INDICATIONS
       POUR REMPLIR LA GRILLE CENTRALE VERTICALEMENT"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,150), (350,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (400,150), (400,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (450,150), (450,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (500,150), (500,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (550,150), (550,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (600,150), (600,300), 3)

    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,150), (600,150), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,200), (600,200), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,250), (600,250), 2)

def Grille_laterale(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE LATERALE : grille sur le cote gauche ou sont notées des
       indications pour remplir la grille centrale horizontalement"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (200,300), (200,550), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (250,300), (250,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (300,300), (300,550), 2)

    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (200,300), (350,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (200,350), (350,350), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (200,400), (350,400), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (200,450), (350,450), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (200,500), (350,500), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (200,550), (350,550), 3)

def Grille_centrale(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE DE PICROSS"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE,(350,300),(350,550),3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (400,300), (400,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (450,300), (450,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (500,300), (500,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE,(550,300),(550,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (600,300), (600,550), 3)

    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,300), (598,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (352,350), (598,350), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (352,400), (598,400), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (352,450), (598,450), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (352,500), (598,500), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (352,550), (598,550), 3)






