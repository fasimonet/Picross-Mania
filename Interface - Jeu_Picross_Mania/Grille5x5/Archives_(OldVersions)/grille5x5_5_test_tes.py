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
# Création de la matrice représentant la grille de dimension 5x5 remplie de 0
MATRICE_GRILLE = zeros((LIGNES, COLONNES))

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

Matrice_grille_centrale1_niveau1 = array([(0, 1, 0, 1, 0), (1, 1, 1, 1, 1), (0, 1, 0, 1, 0), (1, 1, 1, 1, 1), (0, 1, 0, 1, 0)])

""" RENDU DE LA GRILLE CENTRALE :

    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x

"""


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

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)

    # Affichage des différentes grilles
    Affichage_Grille(FENETRE, X_ORIGINE, Y_ORIGINE, 5, 5, 3)

    Afficher_Carre(FENETRE, NOIR, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y)

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

            if event.pos[0] >= X_ORIGINE and event.pos[0] <= X_ORIGINE + NBR_CARRE_CENTRAL * TAILLE_CARRE and event.pos[1] >= Y_ORIGINE and event.pos[1] <= Y_ORIGINE + TAILLE_CARRE * NBR_CARRE_CENTRAL:
                    # Coordonnées des cases de la grille centrale
               CASE_Y = (event.pos[0] - MARGE_X1)//TAILLE_CARRE
               CASE_X = (event.pos[1] - MARGE_Y1)//TAILLE_CARRE
               print((CASE_X,CASE_Y))

pygame.display.flip()

#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()

