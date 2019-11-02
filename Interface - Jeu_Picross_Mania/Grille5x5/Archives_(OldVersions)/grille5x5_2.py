# Cree par Fabien, Quentin et Sinan le 21/03/2016 en Python 3.2
"""
________________________________________________________________________________

                            PRINCIPE DU PROGRAMME
________________________________________________________________________________

"""
# Ce programme est la clef de notre projet,
# il se sert d'autres programmes et bibliothèques sous-jacent(e)s afin d'oeuvrer
# à la création d'une grille de jeu picross de dimension 5x5.

################################################################################
#                  Import des Bibliothèques et des Annexes
################################################################################
# On importe le module pygame qui nous permet de créer l'interface graphique.
import pygame
from pygame.locals import *
from numpy import *

# On initialise l'interface graphique.
pygame.init()

# On rattache le corps du programme aux annexes pour plus de clarté:
# Les fonctions et les constantes du programme
from fonctions5x5_2 import *
from constantes5x5_2 import *

################################################################################
#                              Initialisation
################################################################################
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

#ligne 1
noir_zero_zero = False
noir_zero_un = False
noir_zero_deux = False
noir_zero_trois = False
noir_zero_quatre = False
#ligne 2
noir_un_zero = False
noir_un_un = False
noir_un_deux = False
noir_un_trois = False
noir_un_quatre = False
#ligne 3
noir_deux_zero = False
noir_deux_un = False
noir_deux_deux = False
noir_deux_trois = False
noir_deux_quatre = False
#ligne 4
noir_trois_zero = False
noir_trois_un = False
noir_trois_deux = False
noir_trois_trois = False
noir_trois_quatre = False
#ligne 5
noir_quatre_zero = False
noir_quatre_un = False
noir_quatre_deux = False
noir_quatre_trois = False
noir_quatre_quatre = False

#ligne 1
vide_zero_zero = True
vide_zero_un = True
vide_zero_deux = True
vide_zero_trois = True
vide_zero_quatre = True
#ligne 2
vide_un_zero = True
vide_un_un = True
vide_un_deux = True
vide_un_trois = True
vide_un_quatre = True
#ligne 3
vide_deux_zero = True
vide_deux_un = True
vide_deux_deux = True
vide_deux_trois = True
vide_deux_quatre = True
#ligne 4
vide_trois_zero = True
vide_trois_un = True
vide_trois_deux = True
vide_trois_trois = True
vide_trois_quatre = True
#ligne 5
vide_quatre_zero = True
vide_quatre_un = True
vide_quatre_deux = True
vide_quatre_trois = True
vide_quatre_quatre = True

#ligne 1
croix_zero_zero = True
croix_zero_un = True
croix_zero_deux = True
croix_zero_trois = True
croix_zero_quatre = True
#ligne 2
croix_un_zero = True
croix_un_un = True
croix_un_deux = True
croix_un_trois = True
croix_un_quatre = True
#ligne 3
croix_deux_zero = True
croix_deux_un = True
croix_deux_deux = True
croix_deux_trois = True
croix_deux_quatre = True
#ligne 4
croix_trois_zero = True
croix_trois_un = True
croix_trois_deux = True
croix_trois_trois = True
croix_trois_quatre = True
#ligne 5
croix_quatre_zero = True
croix_quatre_un = True
croix_quatre_deux = True
croix_quatre_trois = True
croix_quatre_quatre = True
"""
________________________________________________________________________________

                            CORPS DU PROGRAMME
________________________________________________________________________________

"""
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

    #CASES NOIRES
    #ligne 1
    if noir_zero_zero == True:
        pygame.draw.rect(FENETRE, NOIR, (350, 300, 50, 50))
    if noir_zero_un == True:
        pygame.draw.rect(FENETRE, NOIR, (400, 300, 50, 50))
    if noir_zero_deux == True:
        pygame.draw.rect(FENETRE, NOIR, (450, 300, 50, 50))
    if noir_zero_trois == True:
        pygame.draw.rect(FENETRE, NOIR, (500, 300, 50, 50))
    if noir_zero_quatre == True:
        pygame.draw.rect(FENETRE, NOIR, (550, 300, 50, 50))
    #ligne 2
    if noir_un_zero == True:
        pygame.draw.rect(FENETRE, NOIR, (350, 350, 50, 50))
    if noir_un_un == True:
        pygame.draw.rect(FENETRE, NOIR, (400, 350, 50, 50))
    if noir_un_deux == True:
        pygame.draw.rect(FENETRE, NOIR, (450, 350, 50, 50))
    if noir_un_trois == True:
        pygame.draw.rect(FENETRE, NOIR, (500, 350, 50, 50))
    if noir_un_quatre == True:
        pygame.draw.rect(FENETRE, NOIR, (550, 350, 50, 50))
    #ligne 3
    if noir_deux_zero == True:
        pygame.draw.rect(FENETRE, NOIR, (350, 400, 50, 50))
    if noir_deux_un == True:
        pygame.draw.rect(FENETRE, NOIR, (400, 400, 50, 50))
    if noir_deux_deux == True:
        pygame.draw.rect(FENETRE, NOIR, (450, 400, 50, 50))
    if noir_deux_trois == True:
        pygame.draw.rect(FENETRE, NOIR, (500, 400, 50, 50))
    if noir_deux_quatre == True:
        pygame.draw.rect(FENETRE, NOIR, (550, 400, 50, 50))
    #ligne 4
    if noir_trois_zero == True:
        pygame.draw.rect(FENETRE, NOIR, (350, 450, 50, 50))
    if noir_trois_un == True:
        pygame.draw.rect(FENETRE, NOIR, (400, 450, 50, 50))
    if noir_trois_deux == True:
        pygame.draw.rect(FENETRE, NOIR, (450, 450, 50, 50))
    if noir_trois_trois == True:
        pygame.draw.rect(FENETRE, NOIR, (500, 450, 50, 50))
    if noir_trois_quatre == True:
        pygame.draw.rect(FENETRE, NOIR, (550, 450, 50, 50))
    #ligne 5
    if noir_quatre_zero == True:
        pygame.draw.rect(FENETRE, NOIR, (350, 500, 50, 50))
    if noir_quatre_un == True:
        pygame.draw.rect(FENETRE, NOIR, (400, 500, 50, 50))
    if noir_quatre_deux == True:
        pygame.draw.rect(FENETRE, NOIR, (450, 500, 50, 50))
    if noir_quatre_trois == True:
        pygame.draw.rect(FENETRE, NOIR, (500, 500, 50, 50))
    if noir_quatre_quatre == True:
        pygame.draw.rect(FENETRE, NOIR, (550, 500, 50, 50))


    #CASES VIDES
    if vide_zero_zero == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (350, 300, 50, 50))
    if vide_zero_un == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (400, 300, 50, 50))
    if vide_zero_deux == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (450, 300, 50, 50))
    if vide_zero_trois == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (500, 300, 50, 50))
    if vide_zero_quatre == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (550, 300, 50, 50))
    #ligne 2
    if vide_un_zero == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (350, 350, 50, 50))
    if noir_un_un == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (400, 350, 50, 50))
    if vide_un_deux == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (450, 350, 50, 50))
    if vide_un_trois == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (500, 350, 50, 50))
    if vide_un_quatre == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (550, 350, 50, 50))
    #ligne 3
    if vide_deux_zero == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (350, 400, 50, 50))
    if vide_deux_un == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (400, 400, 50, 50))
    if vide_deux_deux == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (450, 400, 50, 50))
    if vide_deux_trois == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (500, 400, 50, 50))
    if vide_deux_quatre == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (550, 400, 50, 50))
    #ligne 4
    if vide_trois_zero == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (350, 450, 50, 50))
    if vide_trois_un == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (400, 450, 50, 50))
    if vide_trois_deux == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (450, 450, 50, 50))
    if vide_trois_trois == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (500, 450, 50, 50))
    if vide_trois_quatre == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (550, 450, 50, 50))
    #ligne 5
    if vide_quatre_zero == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (350, 500, 50, 50))
    if vide_quatre_un == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (400, 500, 50, 50))
    if vide_quatre_deux == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (450, 500, 50, 50))
    if vide_quatre_trois == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (500, 500, 50, 50))
    if vide_quatre_quatre == True:
        pygame.draw.rect(FENETRE, BLANC_CREME, (550, 500, 50, 50))

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


################################################################################
#                              CLIC GAUCHE
################################################################################

#BOUCLE EVENT.CLICGAUCHE - Qui s'exécute dans la BOUCLE EVENT.1
# Cette boucle s'effectue si on est dans le cas d'un clic gauche (1)
            if event.button == 1: # dans le cas d'un clic gauche
                #ligne 1
                if event.pos[0] <= 400 and event.pos[0] >= 350 and event.pos[1] <= 350 and event.pos[1] >= 300:
                    if croix_zero_zero == True or vide_zero_zero == True:
                        croix_zero_zero = False
                        vide_zero_zero = False
                        noir_zero_zero = True
                    if noir_zero_zero == True :
                        noir_zero_zero = False
                        vide_zero_zero = True
                if event.pos[0] <= 450 and event.pos[0] >= 400 and event.pos[1] <= 350 and event.pos[1] >= 300:
                    if croix_zero_un == True or vide_zero_un == True:
                        croix_zero_un = False
                        vide_zero_un = False
                        noir_zero_un = True
                    if noir_zero_un == True :
                        noir_zero_un = False
                        vide_zero_un = True
                if event.pos[0] <= 500 and event.pos[0] >= 450 and event.pos[1] <= 350 and event.pos[1] >= 300:
                    if croix_zero_deux == True or vide_zero_deux == True:
                        croix_zero_deux = False
                        vide_zero_deux = False
                        noir_zero_deux = True
                    if noir_zero_deux == True :
                        noir_zero_deux = False
                        vide_zero_deux = True
                if event.pos[0] <= 550 and event.pos[0] >= 500 and event.pos[1] <= 350 and event.pos[1] >= 300:
                    if croix_zero_trois == True or vide_zero_trois == True:
                        croix_zero_trois = False
                        vide_zero_trois = False
                        noir_zero_trois = True
                    if noir_zero_trois == True :
                        noir_zero_trois = False
                        vide_zero_trois = True
                if event.pos[0] <= 600 and event.pos[0] >= 550 and event.pos[1] <= 350 and event.pos[1] >= 300:
                    if croix_zero_quatre == True or vide_zero_quatre == True:
                        croix_zero_quatre = False
                        vide_zero_quatre = False
                        noir_zero_quatre = True
                    if noir_zero_quatre == True :
                        noir_zero_quatre = False
                        vide_zero_quatre = True
                #ligne 2
                if event.pos[0] <= 400 and event.pos[0] >= 350 and event.pos[1] <= 400 and event.pos[1] >= 350:
                    if croix_un_zero == True or vide_un_zero == True:
                        croix_un_zero = False
                        vide_un_zero = False
                        noir_un_zero = True
                    if noir_un_zero == True :
                        noir_un_zero = False
                        vide_un_zero = True
                if event.pos[0] <= 450 and event.pos[0] >= 400 and event.pos[1] <= 400 and event.pos[1] >= 350:
                    if croix_un_un == True or vide_un_un == True:
                        croix_un_un = False
                        vide_un_un = False
                        noir_un_un = True
                    if noir_un_un == True :
                        noir_un_un = False
                        vide_un_un = True
                if event.pos[0] <= 500 and event.pos[0] >= 450 and event.pos[1] <= 400 and event.pos[1] >= 350:
                    if croix_un_deux == True or vide_un_deux == True:
                        croix_un_deux = False
                        vide_un_deux = False
                        noir_un_deux = True
                    if noir_un_deux == True :
                        noir_un_deux = False
                        vide_un_deux = True
                if event.pos[0] <= 550 and event.pos[0] >= 500 and event.pos[1] <= 400 and event.pos[1] >= 350:
                    if croix_un_trois == True or vide_un_trois == True:
                        croix_un_trois = False
                        vide_un_trois = False
                        noir_un_trois = True
                    if noir_un_trois == True :
                        noir_un_trois = False
                        vide_un_trois = True
                if event.pos[0] <= 600 and event.pos[0] >= 550 and event.pos[1] <= 400 and event.pos[1] >= 350:
                    if croix_un_quatre == True or vide_un_quatre == True:
                        croix_un_quatre = False
                        vide_un_quatre = False
                        noir_un_quatre = True
                    if noir_un_quatre == True :
                        noir_un_quatre = False
                        vide_un_quatre = True
                #ligne 3
                if event.pos[0] <= 400 and event.pos[0] >= 350 and event.pos[1] <= 450 and event.pos[1] >= 400:
                    if croix_deux_zero == True or vide_deux_zero == True:
                        croix_deux_zero = False
                        vide_deux_zero = False
                        noir_deux_zero = True
                    if noir_deux_zero == True :
                        noir_deux_zero = False
                        vide_deux_zero = True
                if event.pos[0] <= 450 and event.pos[0] >= 400 and event.pos[1] <= 450 and event.pos[1] >= 400:
                    if croix_deux_un == True or vide_deux_un == True:
                        croix_deux_un = False
                        vide_deux_un = False
                        noir_deux_un = True
                        noir_deux_un = True
                    if noir_deux_un == True :
                        noir_deux_un = False
                        vide_deux_un = True
                if event.pos[0] <= 500 and event.pos[0] >= 450 and event.pos[1] <= 450 and event.pos[1] >= 400:
                    if croix_deux_deux == True or vide_deux_deux == True:
                        croix_deux_deux = False
                        vide_deux_deux = False
                        noir_deux_deux = True
                        noir_deux_deux = True
                    if noir_deux_deux == True :
                        noir_deux_deux = False
                        vide_deux_deux = True
                if event.pos[0] <= 550 and event.pos[0] >= 500 and event.pos[1] <= 450 and event.pos[1] >= 400:
                    if croix_deux_trois == True or vide_deux_trois == True:
                        croix_deux_trois = False
                        vide_deux_trois = False
                        noir_deux_trois = True
                    if noir_deux_trois == True :
                        noir_deux_trois = False
                        vide_deux_trois = True
                if event.pos[0] <= 600 and event.pos[0] >= 550 and event.pos[1] <= 450 and event.pos[1] >= 400:
                    if croix_deux_quatre == True or vide_deux_quatre == True:
                        croix_deux_quatre = False
                        vide_deux_quatre = False
                        noir_deux_quatre = True
                    if noir_deux_quatre == True :
                        noir_deux_quatre = False
                        vide_deux_quatre = True
                #ligne 4
                if event.pos[0] <= 400 and event.pos[0] >= 350 and event.pos[1] <= 500 and event.pos[1] >= 450:
                    if croix_trois_zero == True or vide_trois_zero == True:
                        croix_trois_zero = False
                        vide_trois_zero = False
                        noir_trois_zero = True
                    if noir_trois_zero == True :
                        noir_trois_zero = False
                        vide_trois_zero = True
                if event.pos[0] <= 450 and event.pos[0] >= 400 and event.pos[1] <= 500 and event.pos[1] >= 450:
                    if croix_trois_un == True or vide_trois_un == True:
                        croix_trois_un = False
                        vide_trois_un = False
                        noir_trois_un = True
                    if noir_trois_un == True :
                        noir_trois_un = False
                        vide_trois_un = True
                if event.pos[0] <= 500 and event.pos[0] >= 450 and event.pos[1] <= 500 and event.pos[1] >= 450:
                    if croix_trois_deux == True or vide_trois_deux == True:
                        croix_trois_deux = False
                        vide_trois_deux = False
                        noir_trois_deux = True
                    if noir_trois_deux == True :
                        noir_trois_deux = False
                        vide_trois_deux = True
                if event.pos[0] <= 550 and event.pos[0] >= 500 and event.pos[1] <= 500 and event.pos[1] >= 450:
                    if croix_trois_trois == True or vide_trois_trois == True:
                        croix_trois_trois = False
                        vide_trois_trois = False
                        noir_trois_trois = True
                    if noir_trois_trois == True :
                        noir_trois_trois = False
                        vide_trois_trois = True
                if event.pos[0] <= 600 and event.pos[0] >= 550 and event.pos[1] <= 500 and event.pos[1] >= 450:
                    if croix_trois_quatre == True or vide_trois_quatre == True:
                        croix_trois_quatre = False
                        vide_trois_quatre = False
                        noir_trois_quatre = True
                    if noir_trois_quatre == True :
                        noir_trois_quatre = False
                        vide_trois_quatre = True
                #ligne 5
                if event.pos[0] <= 400 and event.pos[0] >= 350 and event.pos[1] <= 550 and event.pos[1] >= 500:
                    if croix_quatre_zero == True or vide_quatre_zero == True:
                        croix_quatre_zero = False
                        vide_quatre_zero = False
                        noir_quatre_zero = True
                    if noir_quatre_zero == True :
                        noir_quatre_zero = False
                        vide_quatre_zero = True
                if event.pos[0] <= 450 and event.pos[0] >= 400 and event.pos[1] <= 550 and event.pos[1] >= 500:
                    if croix_quatre_un == True or vide_quatre_un == True:
                        croix_quatre_un = False
                        vide_quatre_un = False
                        noir_quatre_un = True
                    if noir_quatre_deux == True :
                        noir_quatre_deux = False
                        vide_quatre_deux = True
                if event.pos[0] <= 500 and event.pos[0] >= 450 and event.pos[1] <= 550 and event.pos[1] >= 500:
                    if croix_quatre_deux == True or vide_quatre_deux == True:
                        croix_quatre_deux = False
                        vide_quatre_deux = False
                        noir_quatre_deux = True
                    if noir_quatre_deux == True :
                        noir_quatre_deux = False
                        vide_quatre_deux = True
                if event.pos[0] <= 550 and event.pos[0] >= 500 and event.pos[1] <= 550 and event.pos[1] >= 500:
                    if croix_quatre_trois == True or vide_quatre_trois == True:
                        croix_quatre_trois = False
                        vide_quatre_trois = False
                        noir_quatre_trois = True
                    if noir_quatre_trois == True :
                        noir_quatre_trois = False
                        vide_quatre_trois = True
                if event.pos[0] <= 600 and event.pos[0] >= 550 and event.pos[1] <= 550 and event.pos[1] >= 500:
                    if croix_quatre_quatre == True or vide_quatre_quatre == True:
                        croix_quatre_quatre = False
                        vide_quatre_quatre = False
                        noir_quatre_quatre = True
                    if noir_quatre_quatre == True :
                        noir_quatre_quatre = False
                        vide_quatre_quatre = True



"""
                if event.button == 3: #Dans le cas d'un clic droit
                    for X in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                        for Y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                            if X == CASE_X and Y == CASE_Y:
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 1: #comporte un 1 dans la matrice? c'est a dire si la case est cochée
                                    #effacer la croix noir
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonnée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 2: # comporte un 2 dans la matrice , c'est a dire si la cas est noire
                                    #effacer le carré noir
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonnée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 0:
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonnée (case_x;case_y)
"""


#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()
