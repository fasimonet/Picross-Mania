# Créé par Sinan et un peu Fabien (:joke:) le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *
pygame.init()

from constantes5x5_3 import *

#===============================================================================
#                       AFFICHAGE DES GRILLES DE JEU
#===============================================================================

def Affichage_Grille(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, NBR_CARRE_GRAND, NBR_CARRE_PETIT):
    Affichage_Grille_Haut_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND)
    Affichage_Grille_Haut_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT)
    Affichage_Grille_Gauche_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT)
    Affichage_Grille_Gauche_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND)
    Affichage_Grille_Milieu_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL)
    Affichage_Grille_Milieu_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL)

#-------------------------------------------------------------------------------
#           AFFICHAGE DE LA GRILLE DU HAUT CONTENANT LES INDICATIONS
#           NECESSAIRES POUR REMPLIR LA GRILLE CENTRALE VERTICALEMENT
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Haut_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT):
    for x in range(NBR_CARRE_GRAND + 1):
        X_END = X_START
        Y_END = Y_START - TAILLE_CARRE * (NBR_CARRE_PETIT)
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
        X_START += TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Haut_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND):
    for x in range(NBR_CARRE_PETIT + 1):
        Y_END = Y_START
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE_GRAND)
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
        Y_START -= TAILLE_CARRE

#-------------------------------------------------------------------------------
#          AFFICHAGE DE LA GRILLE DE GAUCHE CONTENANT LES INDICATIONS
#          NECESSAIRES POUR REMPLIR LA GRILLE CENTRALE HORIZONTALEMENT
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Gauche_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND):
    for x in range(NBR_CARRE_PETIT + 1):
        X_END = X_START
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE_GRAND)
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
        X_START -= TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Gauche_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT):
    for x in range(NBR_CARRE_GRAND + 1):
        Y_END = Y_START
        X_END = X_START - TAILLE_CARRE * (NBR_CARRE_PETIT)
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
        Y_START += TAILLE_CARRE


#-------------------------------------------------------------------------------
#           AFFICHAGE DE LA GRILLE CENTRALE A COMPLETER PAR LE JOUEUR
#              EN FONCTION DES INDICATIONS DES DEUX AUTRES GRILLES
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Milieu_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL):
    for x in range(NBR_CARRE_CENTRAL + 1):
        X_END = X_START
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE_CENTRAL) + 1
        pygame.draw.line(SUPPORT, VERT_PIN, (X_START, Y_START),(X_END,Y_END), 4)
        X_START += TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Milieu_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL):
    for x in range(NBR_CARRE_CENTRAL + 1):
        Y_END = Y_START
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE_CENTRAL) + 1
        pygame.draw.line(SUPPORT, VERT_PIN, (X_START, Y_START),(X_END,Y_END), 4)
        Y_START += TAILLE_CARRE

#===============================================================================
#                 AFFICHAGE DES FIGURES DE LA GRILLE CENTRALE
#===============================================================================

#-------------------------------------------------------------------------------
#                NOIRCISSEMENT DE LA CASE / EFFACEMENT DE LA CASE
#-------------------------------------------------------------------------------

def Afficher_Carre(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y):
    X_START = X_ORIGINE + CASE_Y * TAILLE_CARRE + 3
    Y_START = Y_ORIGINE + CASE_X * TAILLE_CARRE + 3
    X_END = TAILLE_CARRE - 4
    Y_END = TAILLE_CARRE - 4
    pygame.draw.rect(SUPPORT, COULEUR, (X_START, Y_START, X_END, Y_END ))


#-------------------------------------------------------------------------------
#                             COCHAGE DE LA CASE
#-------------------------------------------------------------------------------

def Afficher_Croix(SUPPORT,COULEUR, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y):
    X_START_1 = X_ORIGINE + CASE_Y * TAILLE_CARRE + 3
    Y_START_1 = Y_ORIGINE + CASE_X * TAILLE_CARRE + 3
    X_END_1 = X_START_1 + TAILLE_CARRE - 4
    Y_END_1 = Y_START_1 + TAILLE_CARRE - 4
    X_START_2 = X_START_1 + TAILLE_CARRE - 5
    Y_START_2 = Y_START_1 - 1
    X_END_2 = X_START_1
    Y_END_2 = Y_START_2  + TAILLE_CARRE - 4
    pygame.draw.line(SUPPORT, COULEUR,(X_START_1, Y_START_1),(X_END_1, Y_END_1), 4)
    pygame.draw.line(SUPPORT, COULEUR,(X_START_2, Y_START_2),(X_END_2, Y_END_2), 4)

