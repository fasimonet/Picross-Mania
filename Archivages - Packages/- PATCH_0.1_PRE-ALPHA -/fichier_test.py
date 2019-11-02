#Cree par Fabien et Sinan le 11/04/2016 en Python 3.2
"""
________________________________________________________________________________

                            PRINCIPE DU PROGRAMME
________________________________________________________________________________


INTERFACE GRAPHIQUE DU JEU PICROSS MANIA

Elle est composée de plusieurs parties :
    - le menu principal
    - la page "picross à résoudre"
        - le niveau 1
        - le niveau 2
        - le niveau 3
        - le niveau 4
    - la page "création de picross"
    - la page "résolution de picross"
    - le tutoriel """


################################################################################
#                  Import des Bibliothèques et des Annexes
################################################################################
#On importe le module pygame qui nous permet de créer l'interface graphique

import pygame
from pygame.locals import *

# On initialise l'interface graphique.
pygame.init()

#On rattache le corps du programme aux annexes pour plus de clarté:
    #- les fonctions du menu
    #- les constantes du menu
    #- le corps du tutoriel
    #- les fonctions du tutoriel
    #- les constantes du tutoriel

from fonctions_menu import *
from constantes_menu import *
"""from tuto import *"""
from fonctions_tuto import *
from constantes_tuto import *

################################################################################
#                              Initialisation
################################################################################

# Création d'une variable "FENETRE" qui affiche la fenêtre du jeu
FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

# Titre de la fenêtre
pygame.display.set_caption(TITRE_FENETRE)

# Variable "continuer" à laquelle on affecte la valeur 1
# Cela va nous permettre de garder la fenêtre ouverte
continuer = 1

#BOUCLE DU BOUTON "RETOUR" - Qui s'exécute dans la BOUCLE D'EVENEMENT DE TYPE "MOUVEMENT DE LA SOURIS"
#Si l'utilisateur met sa souris sur le bouton "grille 1"
if event.pos[0] >= 200 and event.pos[0] <= 200+150 and event.pos[1] >= 130 and event.pos[1] <= 130+150:
    # Fermeture de la fenêtre "Niveau 2"
    FENETRE.blit(pygame.image.load("bouton_grille1.PNG"), (200,130))
    """CA BUGGE LORSQUE ON PASSE LA SOURIS EN DEHORS DE LA FENETRE CAR EVENT.POS N'EST PLUS DEFINI"""

