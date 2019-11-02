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
#cela permet de garder la fenetre ouverte
continuer = 1

"""case_x : abscisse de la case de la grille
case_y : ordonnée de la case de la grille"""

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

        if event.type == MOUSEBUTTON:
            if event.buton==1:
                event.button = clic_droit
            if event.button == 2:
                event.button = cli_gauche

        if clic_gauche:
            for x in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                for y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                    if (case_x;case_y) == (X;Y): # définir ce qu'est case_x et case_y
                        if (case_x;case_y)==1: #A CORRIGER "comporte un 1"? c'est a dire si case noir
                            #effacer le carré
                            (case_x;case_y)=0 # assignation de la valeur 0 dans la matrice pour la coordonée (case_x;case_y)

                        if (case_x;case_y)==2 # comporte un 2? c'est a dire si croix noire
                            #effacer la croix noire
                            #dessiner un carré noir
                            (case_x;case_y)=1 #assignation de 1 dans la matrice pour la coordonée (case_x;case_y)
                        if (case_x;case_y)==0
                            #dessiner un carré noir
                            (case_x;case_y)=1

        if clic_droit:
            for x in range (H-1): #Pour X allant de 0 à la longueur d’une ligne de la matrice-1(= nombre de colonnes -1)

                for y in range (L-1): #Pour Y allant de 0 au nombre de ligne de la matrice – 1 

                    if(case_x;case_y) == (X;Y):
                        if (case_x;case_y)==1: #comporte un 1 dans la matrice? c'est a dire si la case est cochée
                        #effacer la croix noir
                        (case_x;case_y)=0 # on assigne 0 dans la matrice pour la coordonée (case_x;case_y)
                    if (case_x;case_y) ==2 # comporte un 2 dans la matrice , c'est a dire si la cas est noire
                        #effacer le carré noir
                        #dessiner une croix noire
                        (case_x;case_y)=2 # on assigne 2 dans la matrice pour la coordonée (case_x;case_y)
                    if (case_x;case_y)==0:
                        #dessiner une croix noire
                        (case_x;case_y)=2 #on assigne 2 dans la matrice pour la coordonée (case_x;case_y)





#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()
