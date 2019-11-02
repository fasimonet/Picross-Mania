# Créé par Sinan Daroukh, le 14/05/2016 en Python 3.2
# - Résolveur -
# Corps du programme

import pygame
from pygame.locals import *
from constantes_tuto import *
from fonctions_tuto import *
from constantes5x5_3 import *
from fonctions5x5_4 import *
pygame.init()

FENETRE = pygame.display.set_mode((LONGUEUR_FENETRE, HAUTEUR_FENETRE))

pygame.display.set_caption(TITRE_FENETRE)

resolveur = 1
contenu_indisp = 0
selection_grille = 0
grille5x5_resolv = 0

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 1
#-------------------------------------------

MAT_HAUT = array([(0, 0, 0, 0, 0),
                            (1, 0, 1, 0, 1),
                            (1, 5, 1, 5, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 1
#---------------------------------------------

MAT_GAUC = array([(0, 1, 1),
                            (0, 0, 5),
                            (0, 1, 1),
                            (0, 0, 5),
                            (0, 1, 1)])


# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

MAT_CENT = array([(2, 1, 2, 1, 2),
                            (1, 1, 1, 1, 1),
                            (2, 1, 2, 1, 2),
                            (1, 1, 1, 1, 1),
                            (2, 1, 2, 1, 2)])

################################################################################
#                       Page d'affichage des Résolveurs
################################################################################
while resolveur == 1:
    FENETRE.fill(BLANC_CREME)
    FENETRE.blit(BOUTON_RETOUR, (30,40))
    FENETRE.blit(ENTETE, (120, 80))
    FENETRE.blit(BOUTON_RESOLVEUR_1, (150, 270))
    FENETRE.blit(BOUTON_RESOLVEUR_2,(150, 430))

    if pygame.mouse.get_focused():
        if Rect_bouton_1.collidepoint(event.pos):
            FENETRE.blit(BOUTON_RESOLVEUR_1_INTER, (125, 265))
        if Rect_bouton_2.collidepoint(event.pos):
            FENETRE.blit(BOUTON_RESOLVEUR_2_INTER, (125, 425))

    Texte(FENETRE, TEXTE_RESOLVEUR, 120, 190, NOIR, None, 30)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == QUIT:
            resolveur = 0
            continuer = 0

        if event.type == MOUSEBUTTONDOWN and event.button == 1:

            if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                resolveur = 0
                """continuer_menu = 1"""

            if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON and event.pos[1] >= 270 and event.pos[1] <= 270 + HAUTEUR_BOUTON:
                resolveur = 0
                selection_grille = 1

            if event.pos[0] >= 150 and event.pos[0] <= 150 + LONGUEUR_BOUTON and event.pos[1] >= 430 and event.pos[1] <= 430 + HAUTEUR_BOUTON:
                resolveur = 0
                contenu_indisp = 1

################################################################################
#                       Page de séléctions des Grilles
################################################################################
while selection_grille == 1:
    FENETRE.fill(BLANC_CREME)
    FENETRE.blit(BOUTON_RETOUR, (30,40))
    FENETRE.blit(ENTETE, (120, 80))
    FENETRE.blit(BOUTON_GRILLE5x5, (338, 283))

    if pygame.mouse.get_focused():
        if Rect_bouton_3.collidepoint(event.pos):
            FENETRE.blit(BOUTON_GRILLE5x5_INTER, (333, 278))

    Texte(FENETRE, TEXTE_GRILLE, 120, 190, NOIR, None, 30)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == QUIT:
            selection_grille = 0
            resolveur = 1

        if event.type == MOUSEBUTTONDOWN and event.button == 1:

            if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                selection_grille = 0
                """continuer_menu = 1"""

            if event.pos[0] >= 338 and event.pos[0] <= 338 + DIMENSIONS_BOUTON_GRILLE and event.pos[1] >= 283 and event.pos[1] <= 283 + DIMENSIONS_BOUTON_GRILLE:
                selection_grille = 0
                grille5x5_resolv = 1

################################################################################
#                       Page d'affichage Picross Couleur
################################################################################
while contenu_indisp == 1:
    FENETRE.fill(BLANC_CREME)
    FENETRE.blit(BOUTON_RETOUR, (30,40))
    FENETRE.blit(ENTETE, (120, 80))
    FENETRE.blit(PICROSS_TRISTE, (318, 263))

    Texte(FENETRE, TEXTE_CONTENU_INDISPONIBLE, 100, 190, NOIR, None, 40)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == QUIT:
            contenu_indisp = 0
            resolveur = 1

        if event.type == MOUSEBUTTONDOWN and event.button == 1:

            if event.pos[0] >= 30 and event.pos[0] <= 30 + LONGUEUR_BOUTON_RETOUR and event.pos[1] >= 40 and event.pos[1] <= 40 + HAUTEUR_BOUTON_RETOUR:
                contenu_indisp = 0
                """continuer_menu = 1"""

################################################################################
#                       Page d'affichage Resolv 5x5
################################################################################
while grille5x5_resolv ==1:
#-------------------------------------------------------------------------------
#                              AFFICHAGE DU FOND
#-------------------------------------------------------------------------------
# Affichage d'une couleur de fond
        FENETRE.fill(BLANC_CREME)
        #- le logo du jeu "Picross Mania"
        """FENETRE.blit(LOGO, (130,75))"""

# Affichage des différentes grilles
        Affichage_Grille(FENETRE, X_ORIGINE_5x5, Y_ORIGINE_5x5, 5, 5, 3, TAILLE_CARRE_5x5)

        Afficher_Indic_Gauche(FENETRE, BLUE_PEGASUS, X_ORIGINE_5x5, Y_ORIGINE_5x5, 3, 5, 35, TAILLE_CARRE_5x5, MAT_GAUC, DIVISEUR_5x5)

        Afficher_Indic_Haut(FENETRE, BLUE_PEGASUS, X_ORIGINE_5x5,Y_ORIGINE_5x5, 3, 5, 35, TAILLE_CARRE_5x5, MAT_HAUT, DIVISEUR_5x5)

        if allclose(MAT_CENT, MATRICE_GRILLE_5x5):
                continuer_grille5x5 = 0
                animation_son = 1
                animation = 1

#-------------------------------------------------------------------------------
#      AFFICHAGE DES FORMES DANS LES CASES DE LA GRILLE : CARRES ET CROIX
#-------------------------------------------------------------------------------

        for x in range(L_5x5):

            for y in range(H_5x5):

                if MATRICE_GRILLE_5x5[x,y]== 0:
                    Afficher_Carre(FENETRE, BLANC_CREME, BLANC_CREME, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5, 1)

                elif MATRICE_GRILLE_5x5[x,y]== 1:
                    Afficher_Carre(FENETRE, VERT_PIN, BLANC_CREME, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5, 1)

                elif MATRICE_GRILLE_5x5[x,y]== 2:
                    Afficher_Croix(FENETRE, VERT_PIN, BLANC_CREME, X_ORIGINE_5x5, Y_ORIGINE_5x5, x, y, TAILLE_CARRE_5x5, 1)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                grille5x5_resolv = 0

pygame.quit()

