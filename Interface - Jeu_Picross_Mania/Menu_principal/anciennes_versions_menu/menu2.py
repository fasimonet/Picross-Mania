#Cree par Fabien et Quentin le 21/03/2016 en Python 3.2
#Création du menu principal du jeu
#Corps du programme

#On importe le module pygame qui nous permet de créer l'interface graphique et l'initialise
import pygame
from pygame.locals import *
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
    #- les fonctions du menu
    #- les constantes du menu
from fonctions_menu import *
from constantes_menu import *
    #- le corps du tutoriel
    #- les fonctions du tutoriel
    #- les constantes du tutoriel
"""from tuto import *
from fonctions_tuto import *
from constantes_tuto import *"""

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

    #On récupère les dimensions du bouton "picross à résoudre"

    #Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

    #On parcourt la liste de tous les événements reçus
    for event in pygame.event.get():
        #Si un de ces événements est de type QUIT
        if event.type == QUIT:
            #On arrête la boucle ce qui ferme la fenetre
            continuer_menu = 0
        #Si l'utilisateur fait un clic gauche
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #Si l'utilisateur clique sur la zone correspondant au bouton "picross à résoudre"
            if event.pos[0] >= 35 and event.pos[0] <= 35+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                #Fermeture du menu principal
                continuer_menu = 0
                #Ouverture de la fenêtre "picross à résoudre"
                """continuer_picross_a_resoudre = 1"""
            #Si l'utilisateur clique sur la zone correspondant au bouton "résolution de picross"
            if event.pos[0] >= 285 and event.pos[0] <= 285+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                #Fermeture du menu principal
                continuer_menu = 0
                #Ouverture de la fenêtre "résolution de picross"
                """continuer_resolution_de_picross = 1"""
            #Si l'utilisateur clique sur la zone correspondant au bouton "création de picross"
            if event.pos[0] >= 535 and event.pos[0] <= 535+LONGUEUR_BOUTONS_PARTIES and event.pos[1] >= 300 and event.pos[1] <= 300+HAUTEUR_BOUTONS_PARTIES:
                #Fermeture du menu principal
                continuer_menu = 0
                #Ouverture de la fenêtre "création de picross"
                """continuer_creation_de_picross = 1"""
            #Si l'utilisateur clique sur la zone correspondant au bouton "tutoriel"
            if event.pos[0] >= 660 and event.pos[0] <= 660+LONGUEUR_BOUTON_TUTORIEL and event.pos[1] >= 588 and event.pos[1] <= 588+HAUTEUR_BOUTON_TUTORIEL:
                #Fermeture du menu principal
                continuer_menu = 0
                #Ouverture de la fenêtre "création de picross"
                continuer_tutoriel = 1



#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()


















