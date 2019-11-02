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

def Affichage_Grille_Milieu(X_START,Y_START, NBR_LIGNES, NBR_CARRE):
    Affichage_Grille_Milieu_Horizontal(X_START,Y_START, NBR_LIGNES, NBR_CARRE)
    Affichage_Grille_Milieu_Vertical(X_START,Y_START, NBR_LIGNES, NBR_CARRE)

def Affichage_Grille_Milieu_Horizontal(X_START,Y_START, NBR_LIGNES, NBR_CARRE):
    for x in range(NBR_LIGNES):
        Y_END = Y_START
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        Y_START += TAILLE_CARRE

def Affichage_Grille_Milieu_Vertical(X_START,Y_START, NBR_LIGNES, NBR_CARRE):
    for x in range(NBR_LIGNES):
        X_END = X_START
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        X_START += TAILLE_CARRE
################################################################################

def Affichage_Grille_Haut_Horizontal(X_START,Y_START, NBR_LIGNES, NBR_CARRE_LONGUEUR):
    for x in range(NBR_LIGNES):
        Y_END = Y_START
        X_END = X_START + TAILLE_CARRE * (NBR_CARRE_LONGUEUR)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        Y_START -= TAILLE_CARRE

def Affichage_Grille_Haut_Vertical(X_START,Y_START, NBR_LIGNES, NBR_CARRE_HAUTEUR):
    for x in range(NBR_LIGNES):
        X_END = X_START
        Y_END = Y_START - TAILLE_CARRE * (NBR_CARRE_HAUTEUR)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        X_START += TAILLE_CARRE

################################################################################

def Affichage_Grille_Gauche_Vertical(X_START,Y_START, NBR_LIGNES, NBR_CARRE):
    for x in range(NBR_LIGNES):
        X_END = X_START
        Y_END = Y_START + TAILLE_CARRE * (NBR_CARRE)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        X_START -= TAILLE_CARRE

def Affichage_Grille_Gauche_Horizontal(X_START,Y_START, NBR_LIGNES, NBR_CARRE):
    for x in range(NBR_LIGNES):
        Y_END = Y_START
        X_END = X_START - TAILLE_CARRE * (NBR_CARRE)
        pygame.draw.line(FENETRE, NOIR, (X_START, Y_START),(X_END,Y_END))
        Y_START += TAILLE_CARRE

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

#===============================================================================
#                            CORPS DU PROGRAMME
#===============================================================================

#BOUCLE D'EXECUTION - Qui s'exécute tant que la variable "continuer" vaut 1
while continuer == 1:

# Affichage d'une couleur de fond
    FENETRE.fill(BLANC_CREME)

    Affichage_Grille_Milieu(300, 250, 6, 5)
    Affichage_Grille_Haut_Horizontal(300, 250, 4, 5)
    Affichage_Grille_Gauche_Vertical(300, 250, 4, 5)
    Affichage_Grille_Haut_Vertical(300, 250, 6, 3)
    Affichage_Grille_Gauche_Horizontal(300, 250, 6, 3)

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

