#Cree par Fabien et Quentin le 21/03/2016 en Python 3.2
#Création du menu principal du jeu
#Corps du programme

#On importe le module pygame qui nous permet de créer l'interface graphique et l'initialise
import pygame
from pygame.locals import *
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
    #- les fonctions
    #- les constantes
from fonctions_menu import *
from constantes_menu import *

#Creation d'une variable fenetre qui affiche la fenetre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))
#Titre de la fenetre
pygame.display.set_caption(TITRE_FENETRE)

#Variable qui continue la boucle si = 1, stoppe si = 0
#cela permet de garder la fenetre du menu ouverte
continuer_menu = 1

#BOUCLE PRINCIPAL
#Fermeture de la fenetre
while continuer_menu:
    #Met une couleur de fond
    FENETRE.fill(BLANC_CREME)

    #Collage des différents boutons sur la fenêtre :
        #- le bouton "picross à résoudre"
        #- le bouton "résolution de picross"
        #- le bouton "création de picross"
        #- le bouton "tutoriel"
        #- le logo du jeu "Picross Mania"
    FENETRE.blit(BOUTON_PICROSS_A_RESOUDRE, (35,300))
    FENETRE.blit(BOUTON_RESOLUTION_DE_PICROSS, (285,300))
    FENETRE.blit(BOUTON_CREATION_DE_PICROSS, (535,300))
    FENETRE.blit(BOUTON_TUTORIEL, (660,588))
    FENETRE.blit(LOGO, (130,120))

    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

    #On parcourt la liste de tous les événements reçus
    for event in pygame.event.get():
        #Si un de ces événements est de type QUIT
        if event.type == QUIT:
            #On arrête la boucle ce qui ferme la fenetre
            continuer_menu = 0
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


















