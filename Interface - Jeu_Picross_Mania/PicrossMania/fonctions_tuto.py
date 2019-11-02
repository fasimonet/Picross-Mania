# Créé par Fabien et Quentin, le 21/03/2016 en Python 3.2
# Classes du programme "grille"
import pygame
from pygame.locals import *
pygame.init()

#Fonction qui permet d'afficher un texte en choisissant :
    #- la surface sur laquelle on blitte l'image (on la colle)
    #- le texte à afficher
    #- l'abscisse du point supérieur gauche du rectangle de texte
    #- l'ordonnée du point supérieur gauche du rectangle de texte
    #- la couleur du texte
    #- la police du texte
    #- la taille du texte

def Texte(screen, texte,x,y,color, police, taille):


    pygame.font.init()
    font = pygame.font.Font(police, taille)
    text = font.render(texte, 1, color)

    screen.blit(text, (x, y))
