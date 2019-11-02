# Créé par Sinan et un peu Fabien (:joke:) le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *
pygame.init()

from constantes5x5_3 import *

#===============================================================================
#                       AFFICHAGE DES GRILLES DE JEU
#===============================================================================

# Cette fonction est la fusion de toutes les fonctions ci-dessous, et permet ainsi d'afficher la grille totale
# Notons qu'il faut d'abord afficher les grilles tierces puis la grille principale pour avoir les épaisseurs correctes

def Affichage_Grille(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, NBR_CARRE_GRAND, NBR_CARRE_PETIT, TAILLE_CARRE):
    Affichage_Grille_Haut_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_CARRE)
    Affichage_Grille_Haut_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT, TAILLE_CARRE)
    Affichage_Grille_Gauche_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT, TAILLE_CARRE)
    Affichage_Grille_Gauche_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_CARRE)
    Affichage_Grille_Milieu_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, TAILLE_CARRE)
    Affichage_Grille_Milieu_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, TAILLE_CARRE)

#-------------------------------------------------------------------------------
#           AFFICHAGE DE LA GRILLE DU HAUT CONTENANT LES INDICATIONS
#           NECESSAIRES POUR REMPLIR LA GRILLE CENTRALE VERTICALEMENT
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Haut_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT, TAILLE_CARRE):
# BOUCLE CARRE GRAND VERTICAL - Qui parcourt la grille dans la longueur (= à son plus grand nombre de carré + 1) pour obtenir l'origine des traits verticaux
    for x in range(NBR_CARRE_GRAND + 1):
    # On affecte la variable X_START à la variable X_END, car on trace des traits verticaux et que l'abscisse des points d'origines et finaux sera tjrs la même
        X_END = X_START
    # On affecte la variable Y_END à la variable Y_START à laquelle on soustrait la hauteur de la grille, pour obtenir l'ordonnée du point final
        Y_END = Y_START - TAILLE_CARRE * (NBR_CARRE_PETIT)
    # On trace la ligne vertical d'épaisseur 2
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
    # On augmente la variable X_START d'une TAILLE_CARRE pour obtenir l'origine du prochain point
        X_START += TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Haut_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_CARRE ):
# BOUCLE CARRE PETIT HORIZONTAL- Qui parcourt la grille dans la hauteur (= à son plus petit nombre de carré + 1) pour obtenir l'origine des traits horizontaux
    for x in range(NBR_CARRE_PETIT + 1):
    # On affecte la variable Y_START à la variable Y_END, car on trace des traits horizontaux et que l'ordonée des points d'origines et finaux sera tjrs la même
        Y_END = Y_START
    # On affecte à la variable X_END, la variable X_START à laquelle on ajoute la longueur de la grille, pour obtenir l'abscisse du point final
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE_GRAND)
    # On trace la ligne vertical d'épaisseur 2
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
    # On diminue la variable Y_START d'une TAILLE_CARRE pour obtenir l'ordonnée du prochain point
        Y_START -= TAILLE_CARRE

#-------------------------------------------------------------------------------
#          AFFICHAGE DE LA GRILLE DE GAUCHE CONTENANT LES INDICATIONS
#          NECESSAIRES POUR REMPLIR LA GRILLE CENTRALE HORIZONTALEMENT
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Gauche_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_CARRE):
# BOUCLE CARRE PETIT VERTICAL - Qui parcourt la grille dans la longueur (= à son plus petit nombre de carré + 1) pour obtenir l'origine des traits verticaux
    for x in range(NBR_CARRE_PETIT + 1):
    # On affecte la variable X_START à la variable X_END, car on trace des traits verticaux et que l'abscisse des points d'origines et finaux sera tjrs la même
        X_END = X_START
    # On affecte la variable Y_END à la variable Y_START à laquelle on soustrait la hauteur de la grille, pour obtenir l'ordonnée du point final
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE_GRAND)
    # On trace la ligne vertical d'épaisseur 2
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
    # On diminue la variable X_START d'une TAILLE_CARRE pour obtenir l'origine du prochain point
        X_START -= TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Gauche_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_GRAND, NBR_CARRE_PETIT, TAILLE_CARRE):
# BOUCLE CARRE PETIT HORIZONTAL- Qui parcourt la grille dans la hauteur (= à son plus grand nombre de carré + 1) pour obtenir l'origine des traits horizontaux
    for x in range(NBR_CARRE_GRAND + 1):
    # On affecte la variable Y_START à la variable Y_END, car on trace des traits horizontaux et que l'ordonnée des points d'origines et finaux sera tjrs la même
        Y_END = Y_START
    # On affecte à la variable X_END, la variable X_START à laquelle on soustrait la longueur de la grille, pour obtenir l'abscisse du point final
        X_END = X_START - TAILLE_CARRE * (NBR_CARRE_PETIT)
    # On trace la ligne vertical d'épaisseur 2
        pygame.draw.line(SUPPORT, NOIR, (X_START, Y_START),(X_END,Y_END), 2)
    # On augmente la variable Y_START d'une TAILLE_CARRE pour obtenir l'ordonnée du prochain point
        Y_START += TAILLE_CARRE


#-------------------------------------------------------------------------------
#           AFFICHAGE DE LA GRILLE CENTRALE A COMPLETER PAR LE JOUEUR
#              EN FONCTION DES INDICATIONS DES DEUX AUTRES GRILLES
#-------------------------------------------------------------------------------

    #(I) Affichage des lignes verticales de la grille
    #=================================================

def Affichage_Grille_Milieu_Vertical(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, TAILLE_CARRE):
# BOUCLE CARRE CENTRAL GRILLE PRINCIPAL - Qui parcourt la grille dans la longueur (= à son plus grand nombre de carré + 1) pour obtenir l'origine des traits verticaux
    for x in range(NBR_CARRE_CENTRAL + 1):
    # On affecte la variable X_START à la variable X_END, car on trace des traits verticaux et que l'abscisse des points d'origines et finaux sera tjrs la même
        X_END = X_START
    # On affecte la variable Y_END à la variable Y_START à laquelle on ajoute la hauteur de la grille, pour obtenir l'ordonnée du point final
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE_CENTRAL) + 1
    # On trace la ligne vertical d'épaisseur 4
        pygame.draw.line(SUPPORT, VERT_PIN, (X_START, Y_START),(X_END,Y_END), 4)
    # On augmente la variable X_START d'une TAILLE_CARRE pour obtenir l'abscisse du prochain point
        X_START += TAILLE_CARRE

    #(II) Affichage des lignes horizontales de la grille
    #====================================================

def Affichage_Grille_Milieu_Horizontal(SUPPORT,X_START,Y_START, NBR_CARRE_CENTRAL, TAILLE_CARRE):
# BOUCLE CARRE CENTRAL GRILLE PRINCIPAL - Qui parcourt la grille dans la longueur (= à son plus grand nombre de carré + 1) pour obtenir l'origine des traits verticaux
    for x in range(NBR_CARRE_CENTRAL + 1):
    # On affecte la variable Y_START à la variable Y_END, car on trace des traits horizontaux et que l'ordonée des points d'origines et finaux sera tjrs la même
        Y_END = Y_START
    # On affecte à la variable X_END, la variable X_START à laquelle on ajoute la longueur de la grille, pour obtenir l'abscisse du point final
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE_CENTRAL) + 1
    # On trace la ligne vertical d'épaisseur 4
        pygame.draw.line(SUPPORT, VERT_PIN, (X_START, Y_START),(X_END,Y_END), 4)
    # On augmente la variable Y_START d'une TAILLE_CARRE pour obtenir l'ordonnée du prochain point
        Y_START += TAILLE_CARRE

#===============================================================================
#                 AFFICHAGE DES FIGURES DE LA GRILLE CENTRALE
#===============================================================================

#-------------------------------------------------------------------------------
#                NOIRCISSEMENT DE LA CASE / EFFACEMENT DE LA CASE
#-------------------------------------------------------------------------------

def Afficher_Carre(SUPPORT, COULEUR1, COULEUR2, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y, TAILLE_CARRE, EPAISSEUR_CONTOUR):
    # On affecte à l'abscisse X_START, l'abscisse du point d'origine à laquelle on ajoute la case où se trouve la souris multiplié par la taille d'un carré
    X_START = X_ORIGINE + CASE_Y * TAILLE_CARRE + 3
    # On affecte à l'ordonnée Y_START, l'ordonné du point d'origine à laquelle on ajoute la case où se trouve la souris multiplié par la taille d'un carré
    Y_START = Y_ORIGINE + CASE_X * TAILLE_CARRE + 3
    # On affecte à la variable X_END, la taille carré (=longueur)
    X_END = TAILLE_CARRE - 4
    # On affecte à la variable Y_END, la taille carré (= hauteur)
    Y_END = TAILLE_CARRE - 4
    # On trace le rectangle
    pygame.draw.rect(SUPPORT, COULEUR1, (X_START, Y_START, X_END, Y_END ))
    pygame.draw.rect(SUPPORT, COULEUR2, (X_START, Y_START, X_END, Y_END ), EPAISSEUR_CONTOUR)

#-------------------------------------------------------------------------------
#                             COCHAGE DE LA CASE
#-------------------------------------------------------------------------------

def Afficher_Croix(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y, TAILLE_CARRE):
    # On affecte à l'abscisse X_START_1, l'abscisse du point d'origine à laquelle on ajoute la case où se trouve la souris multiplié par la taille d'un carré
    X_START_1 = X_ORIGINE + CASE_Y * TAILLE_CARRE + 3
    # On affecte à l'ordonnée Y_START_1, l'ordonné du point d'origine à laquelle on ajoute la case où se trouve la souris multiplié par la taille d'un carré
    Y_START_1 = Y_ORIGINE + CASE_X * TAILLE_CARRE + 3
    # On affecte à la variable X_END_1, l'abscisse X_START_1 à laquelle on ajoute la taille carré (=longueur)
    X_END_1 = X_START_1 + TAILLE_CARRE - 4
    # On affecte à la variable Y_END_1, l'abscisse Y_START_1 à laquelle on ajoute la taille carré (= hauteur)
    Y_END_1 = Y_START_1 + TAILLE_CARRE - 4
    # On affecte à l'abscisse X_START_2, l'abscisse X_START_1 + la longueur du carré
    X_START_2 = X_START_1 + TAILLE_CARRE - 5
    # On affecte à l'ordonné Y_START_2, l'ordonnée Y_START_1
    Y_START_2 = Y_START_1 - 1
    # On affecte à l'abscisse X_END_2, la valeur de X_START_1
    X_END_2 = X_START_1
    # On affecte à l'ordonnée Y_END_2, l'ordonnée à l'origine + la hauteur d'un carré
    Y_END_2 = Y_START_2  + TAILLE_CARRE - 4
    # On trace la première diagonale
    pygame.draw.line(SUPPORT, COULEUR,(X_START_1, Y_START_1),(X_END_1, Y_END_1), 4)
    # On trace la seconde diagonale
    pygame.draw.line(SUPPORT, COULEUR,(X_START_2, Y_START_2),(X_END_2, Y_END_2), 4)

#-------------------------------------------------------------------------------
#                        AFFICHAGE DES INDICATIONS
#-------------------------------------------------------------------------------

def Afficher_Indic_Gauche(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_POLICE, TAILLE_CARRE, MATRICE_GAUCHE, DIVISEUR):
    font = pygame.font.Font(None, TAILLE_POLICE)
    for X in range(NBR_CARRE_PETIT):
        for Y in range(NBR_CARRE_GRAND):
            X_START = ((X_ORIGINE - NBR_CARRE_PETIT * TAILLE_CARRE + 3) + X * TAILLE_CARRE + 3 + TAILLE_CARRE//DIVISEUR)
            Y_START = (Y_ORIGINE + Y * TAILLE_CARRE + 3) + TAILLE_CARRE//DIVISEUR
            texte = font.render(str(MATRICE_GAUCHE[Y,X]), True, COULEUR)
            SUPPORT.blit(texte, (X_START,Y_START))


def Afficher_Indic_Haut(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, NBR_CARRE_PETIT, NBR_CARRE_GRAND, TAILLE_POLICE, TAILLE_CARRE, MATRICE_HAUT, DIVISEUR):
    font = pygame.font.Font(None, TAILLE_POLICE)
    for X in range(NBR_CARRE_GRAND):
        for Y in range(NBR_CARRE_PETIT):
            X_START = (X_ORIGINE + X * TAILLE_CARRE + 3) + TAILLE_CARRE//DIVISEUR + 3
            Y_START = (Y_ORIGINE - NBR_CARRE_PETIT * TAILLE_CARRE + 3) + Y * TAILLE_CARRE + 3 + TAILLE_CARRE//DIVISEUR
            texte = font.render(str(MATRICE_HAUT[Y,X]), True, COULEUR)
            SUPPORT.blit(texte, (X_START,Y_START))
