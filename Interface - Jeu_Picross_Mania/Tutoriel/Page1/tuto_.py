#Cree par Fabien et Quentin le 21/03/2016 en Python 3.2
#Création d'une grille de jeu picross de dimension 5x5
#Corps du programme

#On importe le module pygame qui nous permet de créer l'interface graphique et l'initialise
import pygame
from pygame.locals import *
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
#Les fonctions et les constantes du programme
"""from fonctions_tuto import *"""
from constantes_tuto_ import *
from fonctions_tuto_ import *

#Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))
#Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

#Variable qui continue la boucle si = 1, stoppe si = 0
#cela permet de garder la fenetre du menu ouverte
continuer_tuto = 1

#BOUCLE PRINCIPAL
#Fermeture de la fenetre
while continuer_tuto:
    #Met une couleur de fond
    FENETRE.fill(BLANC_CREME)

    #Affichage du titre
    FENETRE.blit(TITRE_TUTORIEL, (290,25))

    #Affichage du texte
    Texte(FENETRE, TEXTE, 100, 100, NOIR, None, 30)

    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

    #On parcourt la liste de tous les événements reçus
    for event in pygame.event.get():
        #Si un de ces événements est de type QUIT
        if event.type == QUIT:
            #On arrête la boucle ce qui ferme la fenetre
            continuer_tuto = 0

#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus lors de la fermeture de la fenetre)
pygame.quit()


















