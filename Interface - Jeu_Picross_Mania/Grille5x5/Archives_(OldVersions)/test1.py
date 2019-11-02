# Créé par Sinan Daroukh, le 30/04/2016 en Python 3.2
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
def Afficher_carre_noir1(SUPPORT, X_ORIGINE, Y_ORIGINE, CASE_X, CASE_Y):
    X_START = X_ORIGINE + CASE_X * TAILLE_CARRE + 3
    Y_START = Y_ORIGINE + CASE_Y * TAILLE_CARRE + 3
    X_END = TAILLE_CARRE - 4
    Y_END = TAILLE_CARRE - 4
    pygame.draw.rect(SUPPORT, NOIR, (X_START, Y_START, X_END, Y_END ))

#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================

#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)
    Affichage_Grille(FENETRE,300, 250, 5, 5, 3)


    Afficher_Croix_Noire(FENETRE, 300, 250, 0, 4)
    Afficher_Case_Vide(FENETRE, 300, 250, 0, 4)

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

#Permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
#lors de la fermeture de la fenetre)
pygame.quit()

