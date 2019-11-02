#Cree par Fabien et Quentin le 21/03/2016 en Python 3.2
#Création d'une grille de jeu picross de dimension 5x5
#Corps du programme

#On importe le module pygame qui nous permet de créer l'interface graphique et l'initialise
import pygame
from pygame.locals import *
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
#Les fonctions et les constantes du programme
from fonctions5x5 import *
from constantes5x5 import *

#Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))
#Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

#Variable qui continue la boucle si = 1, stoppe si = 0
#Cela permet de garder la fenetre ouverte
continuer = 1

"""CASE_X : abscisse de la case de la grille
CASE_Y : ordonnée de la case de la grille"""

#BOUCLE PRINCIPAL
#Fermeture de la fenetre
while continuer:
    #Met une couleur de fond
    FENETRE.fill(BLANC_CREME)

    #Affichage des grilles laterales et de la grille centrale
    Grille_haut(FENETRE, VERT_PIN, CANARD)
    Grille_laterale(FENETRE, VERT_PIN, CANARD)
    Grille_centrale(FENETRE, VERT_PIN, NOIR)

    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

    for event in pygame.event.get():   #On parcourt la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle ce qui ferme la fenetre

        if event.type == MOUSEBUTTONDOWN:
            #Lorsque la souris est sur la grille centrale
            if SOURIS_X >= (LONGUEUR_FENETRE - MARGE_X1) and SOURIS_X <= (LONGUEUR_FENETRE - MARGE_X2) and SOURIS_Y >= (HAUTEUR_FENETRE - MARGE_Y1) and SOURIS_X <= (HAUTEUR_FENETRE - MARGE_Y2):
                #Coordonnées des cases de la grille centrale
                CASE_X = (SOURIS_X - MARGE_X1)//TAILLE_CARRE
                CASE_Y = (SOURIS_Y - MARGE_Y1)//TAILLE_CARRE

                if event.button == 2: # dans le cas d'un clic gauche
                    for X in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                        for Y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                            if X == CASE_X and Y == CASE_Y: # définir ce qu'est case_x et case_y
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 1: #Si la matrice pour la coordonnee (CASE_X;CASE_Y) comporte un 2 c'est a dire si croix noire
                                    #Effacer la croix noire
                                    #Effacer le carré
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 0 #Assignation de la valeur 0 dans la matrice pour la coordonnée (CASE_X;CASE_Y)

                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 2: #Si la matrice pour la coordonnee (CASE_X;CASE_Y) comporte un 2 c'est a dire si croix noire
                                    #Effacer la croix noire
                                    pygame.draw.rect(FENETRE, NOIR, (300 + (CASE_X+1) * TAILLE_CARRE, 300 + (CASE_Y+1) * TAILLE_CARRE, TAILLE_CARRE-2, TAILLE_CARRE-2))  #Dessiner un carré noir
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 1 #Assignation d'un 1 dans la matrice pour la coordonnee (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 0:
                                    pygame.draw.rect(FENETRE, NOIR, (300 + (CASE_X+1) * TAILLE_CARRE, 300 + (CASE_Y+1) * TAILLE_CARRE, TAILLE_CARRE-2, TAILLE_CARRE-2))  #Dessiner un carré noir
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 1

                if event.button == 1: #Dans le cas d'un clic droit
                    SOURIS_X = 0
                    SOURIS_Y = 0
                    #On attribue a SOURIS_X l'abscisse de la position de la souris
                    SOURIS_X = event.pos[0]
                    #On attribue a SOURIS_Y l'ordonnée de la position de la souris
                    SOURIS_Y = event.pos[1]

                    for X in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                        for Y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                            if X == CASE_X and Y == CASE_Y:
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 1: #comporte un 1 dans la matrice? c'est a dire si la case est cochée
                                    #effacer la croix noir
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 0 # on assigne 0 dans la matrice pour la coordonée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 2: # comporte un 2 dans la matrice , c'est a dire si la cas est noire
                                    #effacer le carré noir
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 2 # on assigne 2 dans la matrice pour la coordonée (case_x;case_y)
                                if MATRICE_GRILLE[CASE_X][CASE_Y] == 0:
                                    #dessiner une croix noire
                                    MATRICE_GRILLE[CASE_X][CASE_Y] = 2 #on assigne 2 dans la matrice pour la coordonée (case_x;case_y)




#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()
