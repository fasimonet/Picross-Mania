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
BOUTON_TUTO_1 = pygame.image.load("bouton_tutoriel_1.PNG")
        #- bouton "Comment créer son picross ?"
BOUTON_TUTO_1_INTER = pygame.image.load("bouton_tutoriel_1_inter.PNG")
        #- bouton "Comment utiliser le résolveur automatique ?"
BOUTON_TUTO_2 = pygame.image.load("bouton_tutoriel_2.PNG")
        #- bouton_inter "Comment résoudre un picross ?"
BOUTON_TUTO_2_INTER = pygame.image.load("bouton_tutoriel_2_inter.PNG")
        #- bouton_inter "Comment créer son picross ?"
BOUTON_TUTO_3 = pygame.image.load("bouton_tutoriel_3.PNG")
        #- bouton_inter "Comment utiliser le résolveur automatique ?"
BOUTON_TUTO_3_INTER = pygame.image.load("bouton_tutoriel_3_inter.PNG")
        #- bouton "précedent"
BOUTON_AVANT = pygame.image.load("precedent2.PNG")
        #- bouton "suivant"
BOUTON_APRES = pygame.image.load("suivant2.PNG")
        #- bouton_inter "précedent"
BOUTON_AVANT_INTER = pygame.image.load("precedent_inter3.PNG")
        #- bouton_inter "suivant"
BOUTON_APRES_INTER = pygame.image.load("suivant_inter3.PNG")


        #(b) TITRES
TITRE_TUTORIEL = pygame.image.load("tutoriel_titre2.PNG")

    #(2) DIMENSION DES IMAGES
        #- longueur du bouton : "retour"
LONGUEUR_BOUTON_RETOUR = 100
        #- hauteur du bouton : "retour"
HAUTEUR_BOUTON_RETOUR = 25
        #- longueur des boutons "tuto"
LONGUEUR_BOUTON_TUTO = 500
        #- hauteur des boutons "tuto"
HAUTEUR_BOUTON_TUTO = 100
        #- longueur des boutons "tuto_inter"
LONGUEUR_BOUTON_TUTO_INTER = 550
        #- hauteur des boutons "tuto_inter"
HAUTEUR_BOUTON_TUTO_INTER = 110
        #- Dimensions des flèches
DIMENSIONS_FLECHES = 50

#ZONES CLIQUABLES - ACCES AUX TUTORIELS
Rect_bouton_tuto_1 = pygame.Rect((150, 190),(500, 100))
Rect_bouton_tuto_2 = pygame.Rect((150, 310),(500, 100))
Rect_bouton_tuto_3 = pygame.Rect((150, 430),(500, 100))

#ZONES CLIQUABLES - ACCES AUX PAGES SUIVANTES
Rect_bouton_avant = pygame.Rect((675, 580),(35, 35))
Rect_bouton_apres = pygame.Rect((725, 580),(35, 35))


#TEXTES
TEXTE_TUTORIEL = "Veuillez sélectionner l'un des boutons ci-dessous."

