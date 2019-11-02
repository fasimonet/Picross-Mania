#Créé par Fabien, le 21/03/2016 en Python 3.2
#Constantes du programme "grille"

import pygame
from pygame.locals import *

#===============================================================================
#                            LISTE DES VARIABLES
#===============================================================================

#-------------------------------------------------------------------------------
#                       CARACTERISTIQUES DE LA FENETRE
#-------------------------------------------------------------------------------

    #(I) Dimensions de la fenêtre
    #===========================================================================

        #(1) Longueur de la fenêtre
        #---------------------------

LONGUEUR_FENETRE = 800

        #(2) Hauteur de la fenêtre
        #--------------------------

HAUTEUR_FENETRE = 650

    #(II) Titre de la fenêtre
    #===========================================================================

TITRE_FENETRE = "Picross Mania"

#-------------------------------------------------------------------------------
#                        CARACTERISTIQUES DES IMAGES
#-------------------------------------------------------------------------------

    #(I) Chargement des images
    #===========================================================================

        #(A) Boutons
        #============

            #(1) Boutons globaux
            #--------------------

                #(a) Bouton du tutoriel
                #~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_TUTORIEL = pygame.image.load("tutoriel.PNG")

                #(b) Bouton retour
                #~~~~~~~~~~~~~~~~~~

BOUTON_RETOUR = pygame.image.load("retour.PNG")

                #(c) Bouton Son_on
                #~~~~~~~~~~~~~~~~~~

BOUTON_SON_ON = pygame.image.load("son_on2.PNG")

                #(c) Bouton Son_off
                #~~~~~~~~~~~~~~~~~~~

BOUTON_SON_OFF = pygame.image.load("son_off2.PNG")

            #(2) Boutons parties du menu principal
            #--------------------------------------

                #(a) Bouton "Picross à résoudre"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    #- bouton de la partie "picross à résoudre"
BOUTON_PICROSS_A_RESOUDRE = pygame.image.load("picross_resoudre_petit.PNG")
                    #- bouton qui correspond au grossissement du bouton "picross à résoudre"
                    # et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_PICROSS_A_RESOUDRE_INTER = pygame.image.load("picross_resoudre.PNG")

                #(b) Bouton "Résolution de picross"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    #- bouton de la partie "résolution de picross"
BOUTON_RESOLUTION_DE_PICROSS = pygame.image.load("picross_resolution_petit.PNG")
                    #- bouton qui correspond au grossissement du bouton "résolution de picross"
                    # et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_RESOLUTION_DE_PICROSS_INTER = pygame.image.load("picross_resolution.PNG")

                #(c) Bouton "Création de picross"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    #- bouton de la partie "création de picross"
BOUTON_CREATION_DE_PICROSS = pygame.image.load("picross_creation_petit.PNG")
                    #- bouton qui correspond au grossissement du bouton "création de picross"
                    # et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_CREATION_DE_PICROSS_INTER = pygame.image.load("picross_creation.PNG")

            #(3) Boutons des niveaux du menu "Picross à résoudre"
            #-----------------------------------------------------

                # Bouton du niveau 1
                #~~~~~~~~~~~~~~~~~~~~

                    #- bouton du Niveau 1
BOUTON_NIVEAU1 = pygame.image.load("niveau1_intermediaire.PNG")
                    #- bouton qui s'affiche lorsque la souris survole le bouton "Niveau 1"
BOUTON_NIVEAU1_INTER = pygame.image.load("niveau1_moyen.PNG")

                # Bouton du niveau 2
                #~~~~~~~~~~~~~~~~~~~~

                    #- bouton du Niveau 2
BOUTON_NIVEAU2 = pygame.image.load("niveau2_intermediaire.PNG")
                    #- bouton qui s'affiche lorsque la souris survole le bouton "Niveau 2"
BOUTON_NIVEAU2_INTER = pygame.image.load("niveau2_moyen.PNG")

                # Bouton du niveau 3
                #~~~~~~~~~~~~~~~~~~~~

                    #- bouton du Niveau 3
BOUTON_NIVEAU3 = pygame.image.load("niveau3_intermediaire.PNG")
                    #- bouton qui s'affiche lorsque la souris survole le bouton "Niveau 3"
BOUTON_NIVEAU3_INTER = pygame.image.load("niveau3_moyen.PNG")

                # Bouton du niveau 4
                #~~~~~~~~~~~~~~~~~~~~

                    #- bouton du Niveau 4
BOUTON_NIVEAU4 = pygame.image.load("niveau4_intermediaire.PNG")
                    #- bouton qui s'affiche lorsque la souris survole le bouton "Niveau 4"
BOUTON_NIVEAU4_INTER = pygame.image.load("niveau4_moyen.PNG")

                # Bouton du niveau personnalisé
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    #- bouton du niveau personnalisé
BOUTON_MON_NIVEAU = pygame.image.load("mon_niveau_intermediaire.PNG")
                    #- bouton qui s'affiche lorsque la souris survole le bouton "Mon Niveau"
MON_NIVEAU_INTER = pygame.image.load("mon_niveau_moyen.PNG")

        #(B) Entêtes des différentes parties du jeu
        #===========================================

            #(1) Logo du jeu
            #----------------

LOGO = pygame.image.load("entete_menu6.PNG")

            #(2) Icone des différents niveaux de jeu
            #----------------------------------------

                #(a) Icone du niveau 1
                #~~~~~~~~~~~~~~~~~~~~~~

                    #- entête de la page "Niveau 1"
ICONE_NIVEAU1 = pygame.image.load("niveau1_petit.PNG")

                #(b) Icone du niveau 2
                #~~~~~~~~~~~~~~~~~~~~~~

                    #- entête de la page "Niveau 2"
ICONE_NIVEAU2 = pygame.image.load("niveau2_petit.PNG")

                #(c) Icone du niveau 3
                #~~~~~~~~~~~~~~~~~~~~~~

                    #- entête de la page "Niveau 3"
ICONE_NIVEAU3 = pygame.image.load("niveau3_petit.PNG")

                #(d) Icone du niveau 4
                #~~~~~~~~~~~~~~~~~~~~~~

                    #- entête de la page "Niveau 4"
ICONE_NIVEAU4 = pygame.image.load("niveau4_petit.PNG")

                #(e) Icone du niveau personnalisé
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    #- entête de la page "Mon Niveau"
ICONE_MON_NIVEAU = pygame.image.load("mon_niveau_petit.PNG")

    #(C) Titre des parties du jeu
    #=============================

        #(1) Titre de la partie "Picross à résoudre"
        #--------------------------------------------

TITRE_PICROSS_A_RESOUDRE = pygame.image.load("picross_resoudre_titre.PNG")

    #(D) Boutons d'accès aux grilles des différents niveaux
    #=======================================================

        #(1) Numéro des grilles
        #-----------------------

            #(a) Grille numéro 1
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1 = pygame.image.load("bouton_grille1.PNG")

            #(b) Grille numéro 2
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE2 = pygame.image.load("bouton_grille2.PNG")

            #(c) Grille numéro 3
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE3 = pygame.image.load("bouton_grille3.PNG")

            #(d) Grille numéro 4
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE4 = pygame.image.load("bouton_grille4.PNG")

            #(e) Grille numéro 5
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE5 = pygame.image.load("bouton_grille5.PNG")

            #(f) Grille numéro 6
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE6 = pygame.image.load("bouton_grille6.PNG")

            #(g) Grille numéro 7
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE7 = pygame.image.load("bouton_grille7.PNG")

            #(h) Grille numéro 8
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE8 = pygame.image.load("bouton_grille8.PNG")

            #(i) Grille numéro 9
            #~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE9 = pygame.image.load("bouton_grille9.PNG")

        #(2) Icone qui s'affiche lorsque l'on survole un numéro de grille
        #-----------------------------------------------------------------

            #(a) Grille vide
            #~~~~~~~~~~~~~~~~

BOUTON_GRILLE_VIDE = pygame.image.load("bouton_menu_grille_moyen.PNG")

            #(b] Picross non créé
            #~~~~~~~~~~~~~~~~~~~~~

ICONE_PICROSS_NON_CREE = pygame.image.load("bouton_cadenas.PNG")

    #(II) Dimension des images
    #===========================================================================

        #(1) Boutons parties du menu principal
        #--------------------------------------

            #- longueur des boutons : "picross à résoudre", "résolution de picross", "création de picross"
LONGUEUR_BOUTONS_PARTIES = 190
            #- hauteur des boutons : "picross à résoudre", "résolution de picross", "création de picross"
HAUTEUR_BOUTONS_PARTIES = 213

        #(2) Bouton du tutoriel
        #-----------------------

            #- longueur du bouton : "tutoriel"
LONGUEUR_BOUTON_TUTORIEL = 100
            #- hauteur du bouton : "tutoriel"
HAUTEUR_BOUTON_TUTORIEL = 25

        #(3) Bouton retour
        #------------------

            #- longueur du bouton : "retour"
LONGUEUR_BOUTON_RETOUR = 100
            #- hauteur du bouton : "retour"
HAUTEUR_BOUTON_RETOUR = 25

        #(4) Bouton des niveaux de la partie "Picross à résoudre"
        #---------------------------------------------------------

            #- taille coté boutons Niveaux
DIMENSION_COTE_BOUTONS_NIVEAUX = 150

#-------------------------------------------------------------------------------
#                                  TEXTES
#-------------------------------------------------------------------------------

    #(I) Titres de niveaux
    #===========================================================================

        #(1) Titre du niveau 1
        #----------------------

TITRE_NIVEAU1 = "NIVEAU FACILE"

        #(2) Titre du niveau 2
        #----------------------

TITRE_NIVEAU2 = "NIVEAU MOYEN"

        #(3) Titre du niveau 3
        #----------------------

TITRE_NIVEAU3 = "NIVEAU DIFFICILE"

        #(4) Titre du niveau 4
        #----------------------

TITRE_NIVEAU4 = "NIVEAU EXTRÊME"

        #(5) Titre du niveau personnalisé
        #---------------------------------

TITRE_NIVEAU_PERSONNALISE = "NIVEAU PERSONNALISE"

#-------------------------------------------------------------------------------
#                              NOM DES COULEURS
#-------------------------------------------------------------------------------

    #(I) Couleurs globales
    #===========================================================================

        #(1) Noir
        #---------

NOIR = (0,0,0)

        #(2) Bleu clair (=vert pin)
        #---------------------------

VERT_PIN = (1, 121,111)

        #(3) Bleu foncé (=canard)
        #-------------------------

CANARD = (4,139,154)

        #(4) Beige (=blanc crème)
        #-------------------------

BLANC_CREME = (253, 241, 184)

    #(II) Couleurs spécifiques aux niveaux
    #===========================================================================

        #(1) Bleu : associé au niveau "Mon niveau"
        #------------------------------------------

BLEU_MON_NIVEAU = (11, 140, 210)

        #(2) Vert : associé au niveau "Niveau 1"
        #----------------------------------------

VERT_NIVEAU1 = (34 , 177, 76)

        #(3) Jaune : associé au niveau "Niveau 2"
        #-----------------------------------------

JAUNE_NIVEAU2 = (255, 201,14)

        #(4) Orange : associé au niveau "Niveau 3"
        #------------------------------------------

ORANGE_NIVEAU3 = (255, 127, 39)

        #(4) Rouge : associé au niveau "Niveau 4"
        #-----------------------------------------

ROUGE_NIVEAU4 = (237, 28, 36)

#-------------------------------------------------------------------------------
#                               ZONES CLIQUABLES
#-------------------------------------------------------------------------------

    #(I) Accès aux grilles des niveaux de la partie "Picross à résoudre"
    #===========================================================================

        #(1) Zone de l'interface correspondant à la grille 1
        #----------------------------------------------------

Rectgrille1 = pygame.Rect(200, 130, 150, 150)

        #(2) Zone de l'interface correspondant à la grille 2
        #----------------------------------------------------

Rectgrille2 = pygame.Rect(405, 130, 150, 150)

        #(3) Zone de l'interface correspondant à la grille 3
        #----------------------------------------------------

Rectgrille3 = pygame.Rect(610, 130, 150, 150)

        #(4) Zone de l'interface correspondant à la grille 4
        #----------------------------------------------------

Rectgrille4 = pygame.Rect(200, 305, 150, 150)

        #(5) Zone de l'interface correspondant à la grille 5
        #----------------------------------------------------

Rectgrille5 = pygame.Rect(405, 305, 150, 150)

        #(6) Zone de l'interface correspondant à la grille 6
        #----------------------------------------------------

Rectgrille6 = pygame.Rect(610, 305, 150, 150)

        #(7) Zone de l'interface correspondant à la grille 7
        #----------------------------------------------------

Rectgrille7 = pygame.Rect(200, 480, 150, 150)

        #(8) Zone de l'interface correspondant à la grille 8
        #----------------------------------------------------

Rectgrille8 = pygame.Rect(405, 480, 150, 150)

        #(9) Zone de l'interface correspondant à la grille 9
        #----------------------------------------------------

Rectgrille9 = pygame.Rect(610, 480, 150, 150)

    #(II) Accès aux niveaux de la partie "Picross à résoudre"
    #===========================================================================

        #(1) Zone de l'interface correspondant au niveau 1
        #--------------------------------------------------

Rect_bouton_Niveau1 = pygame.Rect(262, 112, 125, 125)

        #(2) Zone de l'interface correspondant au niveau 2
        #--------------------------------------------------

Rect_bouton_Niveau2 = pygame.Rect(542, 112, 125, 125)

        #(3) Zone de l'interface correspondant au niveau 3
        #--------------------------------------------------

Rect_bouton_Niveau3 = pygame.Rect(262, 422, 125, 125)

        #(4) Zone de l'interface correspondant au niveau 4
        #--------------------------------------------------

Rect_bouton_Niveau4 = pygame.Rect(542, 422, 125, 125)

        #(5) Zone de l'interface correspondant au niveau personnalisé
        #-------------------------------------------------------------

Rect_bouton_MonNiveau = pygame.Rect(402, 267, 125, 125)

    #(III) Accès aux parties du jeu
    #===========================================================================

        #(1) Zone de l'interface correspondant à la partie "Picross à résoudre"
        #-----------------------------------------------------------------------

Rect_picross_a_resoudre = pygame.Rect(54, 300, 190, 213)

        #(2) Zone de l'interface correspondant à la partie "Résolution de Picross"
        #-----------------------------------------------------------------------

Rect_resolution_de_picross = pygame.Rect(285, 300, 190, 213)

        #(3) Zone de l'interface correspondant à la partie "Création Picross"
        #-----------------------------------------------------------------------

Rect_creation_picross = pygame.Rect(535, 300, 190, 213)