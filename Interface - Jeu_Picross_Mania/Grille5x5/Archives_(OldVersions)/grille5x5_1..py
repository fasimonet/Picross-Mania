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
"""
        elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
            if event.key == K_ESCAPE:
                continuer_jeu = 0
            if event.type == MOUSEBUTTONDOWN:
"""
#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()


















