# Cree par Fabien, Quentin et Sinan le 21/03/2016 en Python 3.2

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
from constantes5x5 import *

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
# Création de la matrice représentant la grille de dimension 5x5 remplie de 0
MATRICE_GRILLE = zeros((LIGNES, COLONNES))


#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================

#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)

# Affichage des différentes grilles
    #- grille du haut ou il y a les indications pour remplir verticalement
    Grille_haut(FENETRE, VERT_PIN, CANARD)
    #- grille à gauche ou il y a les indications pour remplir horizontalement
    Grille_laterale(FENETRE, VERT_PIN, CANARD)
    #- grille de jeu
    Grille_centrale(FENETRE, VERT_PIN, NOIR)

    # TEST : ligne verticale de 300px (marge y1)
    pygame.draw.line(FENETRE, (250,0,0), (350, 0), (350, 300), 1)
    # TEST : ligne verticale de 100px (marge y2)
    pygame.draw.line(FENETRE, (250,0,0), (350, 550), (350, 650), 1)
    # TEST : ligne horizontale de 350px (marge x1)
    pygame.draw.line(FENETRE, (250,0,0), (0, 250), (350, 250), 1)
    # TEST : ligne horizontale de 200px (marge x2)
    pygame.draw.line(FENETRE, (250,0,0), (600, 250), (800, 250), 1)

    pygame.draw.rect(FENETRE, NOIR, (350, 300, TAILLE_CARRE, TAILLE_CARRE))

# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
    for event in pygame.event.get():

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
        if event.type == QUIT:
            continuer = 0

#BOUCLE D'EVENEMENT DE TYPE "CLIC" - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type MOUSEBUTTONDOWN, càd un clic quel qu'il soit alors :
        if event.type == MOUSEBUTTONDOWN:

#BOUCLE EVENT.1 - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "CLIC"
# S'exécute que SI le clic est effectué SUR la grille centrale :


#-------------------------------------------------------------------------------
#                              CLIC GAUCHE
#-------------------------------------------------------------------------------

#BOUCLE EVENT.CLICGAUCHE - Qui s'exécute dans la BOUCLE EVENT.1
# Cette boucle s'effectue si on est dans le cas d'un clic gauche (1)
                if event.button == 1: # dans le cas d'un clic gauche
                    if event.pos[0] >= 350 and event.pos[0] <= 599 and event.pos[1] >= 300 and event.pos[1] <= 549:
                    #Coordonnées des cases de la grille centrale
                        CASE_X = (event.pos[0] - MARGE_X1)//TAILLE_CARRE
                        CASE_Y = (event.pos[1] - MARGE_Y1)//TAILLE_CARRE + 1 # POURQUOI + 1 ??? SANS CA LES COORD SONT PAS BONNES ?!
                        print((CASE_X,CASE_Y))
#PARCOURS DES CASES DE LA GRILLE
# Dans ce bloc, on parcourt les cases de la grille en largeur puis en longueur.
#BOUCLE EVENT.CLICGAUCHE.1 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE
# Cette boucle parcourt la grille centrale en longueur.
                    for X in range (H - 1):       #Pour X allant de 0 à la longueur d’une ligne de la matrice - 1 (= nombre de colonnes -1) = 4
#BOUCLE EVENT.CLICGAUCHE.2 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE et dans la BOUCLE EVENT.CLICGAUCHE.1
# Cette boucle parcourt la grille centrale en largeur.
                        for Y in range (L - 1):   #Pour Y allant de 0 au nombre de ligne de la matrice – 1 
#BOUCLE EVENT.CLICGAUCHE.3 - Qui s'exécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1 et BOUCLE EVENT.CLICGAUCHE.2.
# Cette boucle s'effectue SI ET SEULEMENT SI les compteurs (X,Y) sont équivalents aux coordonnées des cases (CASE_X,CASE_Y)
                            if X == CASE_X and Y == CASE_Y:

#BOUCLE EVENT.CLICGAUCHE.CARRE - Qui s'éxécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte un CARRE noire (1)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 1:
                                    # Assignation de la valeur 0 (Case_Vide) dans la matrice pour la coordonnée (CASE_X;CASE_Y) ayant pour conséquence d'effacer le CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0

#BOUCLE EVENT.CLICGAUCHE.CROIX - Qui s'éxécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) comporte une CROIX noire (2)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 2:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1

#BOUCLE EVENT.CLICGAUCHE.VIDE - Qui s'éxécute dans la BOUCLE EVENT.CLICGAUCHE, BOUCLE EVENT.CLICGAUCHE.1, BOUCLE EVENT.CLICGAUCHE.2, BOUCLE EVENT.CLICGAUCHE.3.
# Cette boucle s'effectue SI ET SEULEMENT SI la matrice pour la coordonnee (CASE_X;CASE_Y) est vide
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0:
                                    # Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y) pour indiquer que la case contient un CARRE
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 1
                                    print (MATRICE_GRILLE[CASE_X, CASE_Y])


"""
                if event.button == 3: #Dans le cas d'un clic droit
                    for X in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                        for Y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                            if X == CASE_X and Y == CASE_Y:
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 1: #comporte un 1 dans la matrice? c'est a dire si la case est cochée
                                    #effacer la croix noir
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 2: # comporte un 2 dans la matrice , c'est a dire si la cas est noire
                                    #effacer le carré noir
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X, CASE_Y] == 0:
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X, CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée (case_x;case_y)
"""

pygame.display.flip()

#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()
