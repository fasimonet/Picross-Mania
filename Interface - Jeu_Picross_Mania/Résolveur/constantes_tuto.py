#Créé par Sinan et Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *

#===============================================================================
#                            LISTE DES VARIABLES
#===============================================================================

#-------------------------------------------------------------------------------
#                        CARACTERISTIQUES DE LA FENETRE
#-------------------------------------------------------------------------------

    #- Longueur de la fenetre
LONGUEUR_FENETRE = 800
    #- Largeur de la fenetre
HAUTEUR_FENETRE = 650
    #- Titre de la fenetre
TITRE_FENETRE = "Picross Mania"

#-------------------------------------------------------------------------------
#                              NOM DES COULEURS
#-------------------------------------------------------------------------------

    #- noir
NOIR = (0,0,0)
    #- bleu clair
VERT_PIN = (1,121,111)
    #- bleu foncé
CANARD = (4,139,154)
    #- beige
BLANC_CREME = (253, 241, 184)

#-------------------------------------------------------------------------------
#                         CARACTERISTIQUES DES IMAGES
#-------------------------------------------------------------------------------

    #(1) CHARGEMENT DES IMAGES
        #(a) BOUTONS
        #- bouton "retour"
BOUTON_RETOUR = pygame.image.load("retour.PNG")
        #- bouton "Comment résoudre un picross ?"
BOUTON_RESOLVEUR_1 = pygame.image.load("bouton1.PNG")
        #- bouton "Comment créer son picross ?"
BOUTON_RESOLVEUR_1_INTER = pygame.image.load("bouton1inter.PNG")
        #- bouton "Comment utiliser le résolveur automatique ?"
BOUTON_RESOLVEUR_2 = pygame.image.load("bouton2.PNG")
        #- bouton_inter "Comment résoudre un picross ?"
BOUTON_RESOLVEUR_2_INTER = pygame.image.load("bouton2inter.PNG")
BOUTON_GRILLE5x5 = pygame.image.load("grille5x5.PNG")
BOUTON_GRILLE5x5_INTER = pygame.image.load("grille5x5inter.PNG")
PICROSS_TRISTE = pygame.image.load("picrosstriste.PNG")

        #(b) TITRES
ENTETE = pygame.image.load("entete_menu6.PNG")

    #(2) DIMENSION DES IMAGES
        #- longueur du bouton : "retour"
LONGUEUR_BOUTON_RETOUR = 100
        #- hauteur du bouton : "retour"
HAUTEUR_BOUTON_RETOUR = 25
        #- longueur des boutons "tuto"
LONGUEUR_BOUTON = 500
        #- hauteur des boutons "tuto"
HAUTEUR_BOUTON = 100
        #- longueur des boutons "tuto_inter"
LONGUEUR_BOUTON_INTER = 550
        #- hauteur des boutons "tuto_inter"
HAUTEUR_BOUTON_INTER = 110
DIMENSIONS_BOUTON_GRILLE = 125

#ZONES CLIQUABLES - ACCES AUX TUTORIELS
Rect_bouton_1 = pygame.Rect((150, 270),(500, 100))
Rect_bouton_2 = pygame.Rect((150, 430),(500, 100))
Rect_bouton_3 = pygame.Rect((338,283),(125, 125))

#TEXTES
TEXTE_RESOLVEUR = "Veuillez sélectionner l'un des résolveurs disponibles."
TEXTE_GRILLE = "Pour le moment, seule la grille 5x5 est disponible !"
TEXTE_CONTENU_INDISPONIBLE = "Ce contenu est, pour le moment, indisponible..."

