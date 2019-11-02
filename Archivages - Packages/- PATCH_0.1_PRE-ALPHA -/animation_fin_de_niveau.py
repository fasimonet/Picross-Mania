# Cree par Fabien et Sinan le 21/03/2016 en Python 3.2

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
animation = 1

#BOUCLE MUSICALE - Qui s'éxécute tant que la fenêtre spécifique est ouverte.
# NB : Toujours privilégier le fichier.ogg plus fluide et plus léger !
if animation == 1:
    pygame.mixer.music.load("FF4VictoryFanfare.ogg")
    pygame.mixer.music.set_volume(0.175)
    pygame.mixer.music.play(-1, 0)

#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================

#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while animation == 1:

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)
    pygame.draw.line(FENETRE, NOIR, (154, 400), (650, 400), 4)
    pygame.draw.line(FENETRE, NOIR, (650, 204), (650, 402), 4)

    FENETRE.blit(pygame.image.load("animation.PNG"), (150, 200))
    """FENETRE.blit(pygame.image.load("Luigi3.gif"), (0, 400))
    FENETRE.blit(pygame.image.load("Luigi2.gif"), (600, 250))"""



# Rafraichissement de la fenetre (nécessaire pour afficher ce qui précède)
    pygame.display.flip()

#BOUCLE PRINCIPALE - Qui s'exécute dans la BOUCLE D'EXECUTION soit tant que la variable "continuer" vaut 1
# Cette boucle parcourt la liste de tous les événements reçus
    for event in pygame.event.get():

#BOUCLE DE FERMETURE - Qui s'éxécute dans la BOUCLE PRINCIPALE
# Si un de ces événements est de type QUIT, alors on affecte à "continuer" la valeur 0
# Ceci ayant pour conséquence d'arrêter la BOUCLE D'EXECUTION donc l'exécution du programme
        if event.type == QUIT:
            animation = 0

#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()
