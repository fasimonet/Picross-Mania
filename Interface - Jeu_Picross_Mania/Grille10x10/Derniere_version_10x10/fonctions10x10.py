# Créé par Fabien et Quentin, le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *

def Grille_haut(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE DU HAUT OU SONT NOTEES DES INDICATIONS
       POUR REMPLIR LA GRILLE CENTRALE VERTICALEMENT"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,175), (350,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (375,175), (375,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (400,175), (400,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (425,175), (425,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (450,175), (450,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (475,175), (475,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (500,175), (500,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (525,175), (525,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (550,175), (550,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (575,175), (575,300), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (600,175), (600,300), 3)

    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,175), (600,175), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,200), (600,200), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,225), (600,225), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,250), (600,250), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,275), (600,275), 2)

def Grille_laterale(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE LATERALE : grille sur le cote gauche ou sont notées des
       indications pour remplir la grille centrale horizontalement"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (225,300), (225,550), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (250,300), (250,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (275,300), (275,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (300,300), (300,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (325,300), (325,550), 2)


    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (225,300), (350,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,325), (350,325), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,350), (350,350), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,375), (350,375), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,400), (350,400), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,425), (350,425), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,450), (350,450), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,475), (350,475), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,500), (350,500), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (225,525), (350,525), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (225,550), (350,550), 3)

def Grille_centrale(SUPPORT, COULEUR_BORDURE, COULEUR_INTERIEURE):
    """GRILLE DE PICROSS"""
    ##(SUPPORT, COULEUR DU TRAIT, COORDONNEES DU PREMIER POINT, COORDONNEES DU
    ##DEUXIEME POINT, EPAISSEUR DU TRAIT)"""
    """SUPPORT : ce sur quoi on va dessiner les lignes
       COULEUR_BORDURE : couleur des lignes formant le contour de la grille
       COULEUR_INTERIEURE : couleur des lignes formant l'intérieur de la grille"""

    #Dessine les lignes verticales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE,(350,300),(350,550),3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (375,300), (375,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (400,300), (400,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (425,300), (425,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (450,300), (450,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (475,300), (475,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (500,300), (500,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (525,300), (525,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE,(550,300),(550,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (575,300), (575,550), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (600,300), (600,550), 3)

    #Dessine les lignes horizontales de la grille
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,300), (600,300), 3)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,325), (600,325), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,350), (600,350), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,375), (600,375), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,400), (600,400), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,425), (600,425), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,450), (600,450), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,475), (600,475), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,500), (600,500), 2)
    pygame.draw.line(SUPPORT, COULEUR_INTERIEURE, (350,525), (600,525), 2)
    pygame.draw.line(SUPPORT, COULEUR_BORDURE, (350,550), (600,550), 3)






