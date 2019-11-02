# Cree par Fabien et Sinan le 21/03/2016 en Python 3.2

#===============================================================================
#                            PRINCIPE DU PROGRAMME
#===============================================================================

# Ce programme est la clef de notre projet,
# il se sert d'autres programmes et bibliothèques sous-jacent(e)s afin d'oeuvrer
# à la création d'une grille de jeu picross de dimension 5x5.

#===============================================================================
#                  Import des Bibliothèques et des Annexes
#===============================================================================

# On importe le module pygame qui nous permet de créer l'interface graphique.
import pygame
from pygame.locals import *
from numpy import *

# On initialise l'interface graphique.
pygame.init()

# On rattache le corps du programme aux annexes pour plus de clarté:
# Les fonctions et les constantes du programme
from fonctions5x5_3 import *
from constantes5x5_3 import *

#===============================================================================
#                              Initialisation
#===============================================================================

# Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1
CASE_X = 0
CASE_Y= 0
NBR_CARRE_CENTRAL = 5
POLICE = None
TAILLE_POLICE = 50
COULEUR = (0, 0, 0)
ANTICRENELAGE = True

# Création de la matrice représentant la grille de dimension 5x5 remplie de 0
MATRICE_GRILLE = zeros((LIGNES, COLONNES))


# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 1
#---------------------------------------------
Matrice_grille_gauche1_niveau1 = array([(0, 1, 1),
                                        (0, 0, 5),
                                        (0, 1, 1),
                                        (0, 0, 5),
                                        (0, 1, 1)])
print(Matrice_grille_gauche1_niveau1[1,2])

""" RENDU DE LA GRILLE DE GAUCHE :

    0 1 1
    0 0 5
    0 1 1
    0 0 5
    0 1 1

"""
# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

"""Matrice_grille_centrale1_niveau1 = array([(0, 1, 0, 1, 0), (1, 1, 1, 1, 1), (0, 1, 0, 1, 0), (1, 1, 1, 1, 1), (0, 1, 0, 1, 0)])

RENDU DE LA GRILLE CENTRALE :

    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x

"""

Matrice_grille_haut1_niveau1 = array([(0, 0, 0, 0, 0),
                                        (1, 0, 1, 0, 1),
                                        (1, 5, 1, 5, 1)])

""" RENDU DE LA GRILLE DU HAUT :

    0 0 0 0 0
    1 0 1 0 1
    1 5 1 5 1

"""
def Afficher_Indic_Gauche(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, NBR_CARRE_PETIT, NBR_CARRE_GRAND, MATRICE_GAUCHE):
    font = pygame.font.Font(None, 45)
    for X in range(NBR_CARRE_PETIT):
        for Y in range(NBR_CARRE_GRAND):
            X_START = ((X_ORIGINE - 3 * TAILLE_CARRE + 3) + X * TAILLE_CARRE + 3 + TAILLE_CARRE//4)
            Y_START = (Y_ORIGINE + Y * TAILLE_CARRE + 3) + TAILLE_CARRE//4
            texte = font.render(str(MATRICE_GAUCHE[Y,X]), True, COULEUR)
            SUPPORT.blit(texte, (X_START,Y_START))


def Afficher_Indic_Haut(SUPPORT, COULEUR, X_ORIGINE, Y_ORIGINE, NBR_CARRE_PETIT, NBR_CARRE_GRAND, MATRICE_HAUT):
    font = pygame.font.Font(None, 45)
    for X in range(NBR_CARRE_GRAND):
        for Y in range(NBR_CARRE_PETIT):
            X_START = (X_ORIGINE + X * TAILLE_CARRE + 3) + TAILLE_CARRE//4 + 3
            Y_START = (Y_ORIGINE - 3 * TAILLE_CARRE + 3) + Y * TAILLE_CARRE + 3 + TAILLE_CARRE//4
            texte = font.render(str(MATRICE_HAUT[Y,X]), True, COULEUR)
            SUPPORT.blit(texte, (X_START,Y_START))

#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================
"""

while 1 == 1:
    if allclose(Matrice_grille_centrale1_niveau1, MATRICE_GRILLE):
        continuer = 0
        animation = 1
    else :
        continuer = 1
"""
#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:

#-------------------------------------------------------------------------------
#                              AFFICHAGE DU FOND
#-------------------------------------------------------------------------------

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)

# Affichage des différentes grilles
    Affichage_Grille(FENETRE, X_ORIGINE, Y_ORIGINE, 5, 5, 3)

    Afficher_Indic_Gauche(FENETRE, NOIR, X_ORIGINE, Y_ORIGINE, 3, 5, Matrice_grille_gauche1_niveau1)

    Afficher_Indic_Haut(FENETRE, NOIR, X_ORIGINE,Y_ORIGINE, 3, 5, Matrice_grille_haut1_niveau1)




    """font = pygame.font.Font(POLICE, TAILLE_POLICE)
#On parcourt la coordonnée en X de la matrice de gauche : allant de 0 à 2
    for X in range (2):
#On parcourt la coordonnée en Y de la matrice de gauche : allant de 0 à 4
        for Y in range (4):
#On définit la position du rect de texte en x en fonction de la coordonnée en x de l'origine de la grille centrale
            pos_x = X_ORIGINE - (X+1) * TAILLE_CARRE //2
#On définit la position du rect de texte en y en fonction de la coordonnée en y de l'origine de la grille centrale
            pos_y = Y_ORIGINE + (X+1) * TAILLE_CARRE //2
#Texte à afficher : le chiffre dans la matrice aux coordonnées [X,Y], l'anticrenelage et la couleur
            texte = font.render(str(Matrice_grille_gauche1_niveau1[X,Y]), ANTICRENELAGE, COULEUR)
#Affichage du texte
            FENETRE.blit(texte, (pos_x,pos_y))"""

#-------------------------------------------------------------------------------
#      AFFICHAGE DES FORMES DANS LES CASES DE LA GRILLE : CARRES ET CROIX
#-------------------------------------------------------------------------------

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en largeur puis en longueur.
#BOUCLE AFFICHAGE_FORMES - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la grille centrale en longueur.
    for x in range(L):

#BOUCLE AFFICHAGE_FORMES.1 - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES
# Cette boucle parcourt la grille centrale en hauteur.
        for y in range(H):

#BOUCLE AFFICHAGE_FORMES.VIDE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de la couleur de fond lorsque la matrice aux coordonnées [x,y] est égale à 0 càd dans le cas d'une case vide.
            if MATRICE_GRILLE[x,y]== 0:
                Afficher_Carre(FENETRE, BLANC_CREME, X_ORIGINE, Y_ORIGINE, x, y)

#BOUCLE AFFICHAGE_FORMES.CARRE - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche un carré de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 1 càd dans le cas d'une case noircie.
            elif MATRICE_GRILLE[x,y]== 1:
                Afficher_Carre(FENETRE, NOIR, X_ORIGINE, Y_ORIGINE, x, y)

#BOUCLE AFFICHAGE_FORMES.CROIX - Qui s'exécute dans la BOUCLE AFFICHAGE_FORMES.1
# Cette boucle affiche une croix de couleur prédéfinie lorsque la matrice aux coordonnées [x,y] est égale à 2 càd dans le cas d'une case cochée.
            elif MATRICE_GRILLE[x,y]== 2:
                Afficher_Croix(FENETRE, VERT_PIN, X_ORIGINE, Y_ORIGINE, x, y)

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
    for event in pygame.event.get():

#-------------------------------------------------------------------------------
#                   EVENEMENT DE FERMETURE DE LA FENETRE
#-------------------------------------------------------------------------------

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
        if event.type == QUIT:
            continuer = 0

#-------------------------------------------------------------------------------
#           CALCUL DES COORDONNEES DES CASES DE LA GRILLE CENTRALE
#-------------------------------------------------------------------------------

#BOUCLE D'EVENEMENT DE TYPE "CLIC" - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type MOUSEBUTTONDOWN, càd un clic quel qu'il soit alors :
        if event.type == MOUSEBUTTONDOWN:

            if event.pos[0] >= X_ORIGINE and event.pos[0] <= X_ORIGINE + NBR_CARRE_CENTRAL * TAILLE_CARRE and event.pos[1] >= Y_ORIGINE and event.pos[1] <= Y_ORIGINE + TAILLE_CARRE * NBR_CARRE_CENTRAL:
                # Coordonnées des cases de la grille centrale
                CASE_Y = (event.pos[0] - MARGE_X1)//TAILLE_CARRE
                CASE_X = (event.pos[1] - MARGE_Y1)//TAILLE_CARRE
                print((CASE_X,CASE_Y))

#-------------------------------------------------------------------------------
#                              CLIC GAUCHE
#-------------------------------------------------------------------------------

#BOUCLE EVENT.1 - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICGAUCHE - Qui s'exécute dans la BOUCLE EVENT.1
# Cette boucle s'effectue si on est dans le cas d'un clic gauche (1)
                if event.button == 1: # dans le cas d'un clic gauche

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICGAUCHE.1 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE
# Cette boucle parcourt la grille centrale en longueur.
                    for Y in range (L):   #Pour Y allant de 0 au nombre de ligne de la matrice
#BOUCLE EVENT.CLICGAUCHE.2 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE et dans la BOUCLE EVENT.CLICGAUCHE.1
# Cette boucle parcourt la grille centrale en hauteur.
                        for X in range (H):       #Pour X allant de 0 à la longueur d’une ligne de la matrice - 1 (= nombre de colonnes -1) = 4
#BOUCLE EVENT.CLICGAUCHE.3 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1 et BOUCLE EVENT.CLICGAUCHE.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                            if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICGAUCHE.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee [CASE_X;CASE_Y] pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1

#BOUCLE EVENT.CLICGAUCHE.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noire (1)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 1:
                                    # Assignation de la valeur 0 (Case_Vide) dans la matrice pour la coordonnée [CASE_X;CASE_Y] ayant pour conséquence d'effacer le CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0

#BOUCLE EVENT.CLICGAUCHE.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 2:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1
                                print(MATRICE_GRILLE)

#-------------------------------------------------------------------------------
#                              CLIC DROIT
#-------------------------------------------------------------------------------

#BOUCLE EVENT.2 - Qui s'éxécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :

#BOUCLE EVENT.CLICDROIT - Qui s'exécute dans la BOUCLE EVENT.2
# Cette boucle s'effectue si on est dans le cas d'un clic droit (3)
                elif event.button == 3: #Dans le cas d'un clic droit

#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en longueur puis en hauteur.
#BOUCLE EVENT.CLICDROIT.1 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT
# Cette boucle parcourt la grille centrale en longueur.
                    for Y in range (L): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)
#BOUCLE EVENT.CLICDROIT.2 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT et dans la BOUCLE EVENT.CLICDROIT.1
# Cette boucle parcourt la grille centrale en hauteur.
                        for X in range (H): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 
#BOUCLE EVENT.CLICDROIT.3 - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1 et BOUCLE EVENT.CLICDROIT.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                            if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICDROIT.VIDE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] est vide (0)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0: # comporte un 1 dans la matrice , c'est a dire si la case est vide
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CARRE - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee [CASE_X;CASE_Y] comporte un CARRE noir (1)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 1: # comporte un 1 dans la matrice , c'est a dire si la case est noire
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée [CASE_X;CASE_Y]

#BOUCLE EVENT.CLICDROIT.CROIX - Qui s'exécute dans la BOUCLE EVENT.CLICDROIT, BOUCLE EVENT.CLICDROIT.1, BOUCLE EVENT.CLICDROIT.2, BOUCLE EVENT.CLICDROIT.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                elif MATRICE_GRILLE[CASE_X, CASE_Y] == 2: #comporte un 2 dans la matrice c'est a dire si la case est cochée
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée [CASE_X;CASE_Y]
                                print(MATRICE_GRILLE)


#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()

"""
# Affichage d'un texte
    font = pygame.font.Font(None, 50)
    text = font.render(str(1), 1, (10, 10, 10))
#    textpos = text.get_rect()
    textpos = (X_ORIGINE -4 - TAILLE_CARRE//2, Y_ORIGINE +2 + TAILLE_CARRE//3)
#    textpos.centerx = FENETRE.get_rect().centerx
#    textpos.centery = FENETRE.get_rect().centery
    FENETRE.blit(text, textpos)

"""