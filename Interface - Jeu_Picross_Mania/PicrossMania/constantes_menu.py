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

#Longueur de la fenêtre
LONGUEUR_FENETRE = 800
#Hauteur de la fenêtre
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

#Bouton du tutoriel
BOUTON_TUTORIEL = pygame.image.load("tutoriel.PNG")
#Bouton retour
BOUTON_RETOUR = pygame.image.load("retour.PNG")
BOUTON_VALIDER = pygame.image.load("valider.PNG")
#Bouton Son_on
BOUTON_SON_ON = pygame.image.load("son_on2.PNG")
#Bouton Son_off
BOUTON_SON_OFF = pygame.image.load("son_off2.PNG")

            #(2) Boutons parties du menu principal
            #--------------------------------------

                #(a) Bouton "Picross à résoudre"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bouton de la partie "picross à résoudre"
BOUTON_PICROSS_A_RESOUDRE = pygame.image.load("picross_resoudre_petit.PNG")
#Bouton qui correspond au grossissement du bouton "picross à résoudre"
#et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_PICROSS_A_RESOUDRE_INTER = pygame.image.load("picross_resoudre.PNG")

                #(b) Bouton "Résolution de picross"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bouton de la partie "résolution de picross"
BOUTON_RESOLUTION_DE_PICROSS = pygame.image.load("picross_resolution_petit.PNG")
#Bouton qui correspond au grossissement du bouton "résolution de picross"
#et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_RESOLUTION_DE_PICROSS_INTER = pygame.image.load("picross_resolution.PNG")

                #(c) Bouton "Création de picross"
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bouton de la partie "création de picross"
BOUTON_CREATION_DE_PICROSS = pygame.image.load("picross_creation_petit.PNG")
#Bouton qui correspond au grossissement du bouton "création de picross"
#et qui s'effectue lorsque la souris est placée sur ce bouton
BOUTON_CREATION_DE_PICROSS_INTER = pygame.image.load("picross_creation.PNG")

            #(3) Boutons des niveaux du menu "Picross à résoudre"
            #-----------------------------------------------------

                # Bouton du niveau 1
                #~~~~~~~~~~~~~~~~~~~~

#Bouton du Niveau 1
BOUTON_NIVEAU1 = pygame.image.load("niveau1_intermediaire.PNG")
#Bouton qui s'affiche lorsque la souris survole le bouton "Niveau 1"
BOUTON_NIVEAU1_INTER = pygame.image.load("niveau1_moyen.PNG")

                # Bouton du niveau 2
                #~~~~~~~~~~~~~~~~~~~~

#Bouton du Niveau 2
BOUTON_NIVEAU2 = pygame.image.load("niveau2_intermediaire.PNG")
#Bouton qui s'affiche lorsque la souris survole le bouton "Niveau 2"
BOUTON_NIVEAU2_INTER = pygame.image.load("niveau2_moyen.PNG")

                # Bouton du niveau 3
                #~~~~~~~~~~~~~~~~~~~~

#Bouton du Niveau 3
BOUTON_NIVEAU3 = pygame.image.load("niveau3_intermediaire.PNG")
#Bouton qui s'affiche lorsque la souris survole le bouton "Niveau 3"
BOUTON_NIVEAU3_INTER = pygame.image.load("niveau3_moyen.PNG")

                # Bouton du niveau 4
                #~~~~~~~~~~~~~~~~~~~~

#Bouton du Niveau 4
BOUTON_NIVEAU4 = pygame.image.load("niveau4_intermediaire.PNG")
#Bouton qui s'affiche lorsque la souris survole le bouton "Niveau 4"
BOUTON_NIVEAU4_INTER = pygame.image.load("niveau4_moyen.PNG")

                # Bouton du niveau personnalisé
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bouton du niveau personnalisé
BOUTON_MON_NIVEAU = pygame.image.load("mon_niveau_intermediaire.PNG")
#Bouton qui s'affiche lorsque la souris survole le bouton "Mon Niveau"
MON_NIVEAU_INTER = pygame.image.load("mon_niveau_moyen.PNG")

        #(B) Entêtes des différentes parties du jeu
        #===========================================

            #(1) Logo du jeu
            #----------------

LOGO = pygame.image.load("entete_menu6.PNG")

            #(2) Icone des différents niveaux de jeu
            #----------------------------------------

#Entête de la page "Niveau 1"
ICONE_NIVEAU1 = pygame.image.load("niveau1_petit.PNG")
#Entête de la page "Niveau 2"
ICONE_NIVEAU2 = pygame.image.load("niveau2_petit.PNG")
#Entête de la page "Niveau 3"
ICONE_NIVEAU3 = pygame.image.load("niveau3_petit.PNG")
#Entête de la page "Niveau 4"
ICONE_NIVEAU4 = pygame.image.load("niveau4_petit.PNG")
#Entête de la page "Mon Niveau"
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

BOUTON_GRILLE1 = pygame.image.load("bouton_grille1.PNG")
BOUTON_GRILLE2 = pygame.image.load("bouton_grille2.PNG")
BOUTON_GRILLE3 = pygame.image.load("bouton_grille3.PNG")
BOUTON_GRILLE4 = pygame.image.load("bouton_grille4.PNG")
BOUTON_GRILLE5 = pygame.image.load("bouton_grille5.PNG")
BOUTON_GRILLE6 = pygame.image.load("bouton_grille6.PNG")
BOUTON_GRILLE7 = pygame.image.load("bouton_grille7.PNG")
BOUTON_GRILLE8 = pygame.image.load("bouton_grille8.PNG")
BOUTON_GRILLE9 = pygame.image.load("bouton_grille9.PNG")

        #(2) Icone qui s'affiche lorsque l'on survole un numéro de grille
        #-----------------------------------------------------------------

            #(a) Boutons grilles niveau 1 vides
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU1 = pygame.image.load("bouton_menu_grille1_niveau1.PNG")
BOUTON_GRILLE2_NIVEAU1 = pygame.image.load("bouton_menu_grille2_niveau1.PNG")
BOUTON_GRILLE3_NIVEAU1 = pygame.image.load("bouton_menu_grille3_niveau1_2.PNG")
BOUTON_GRILLE4_NIVEAU1 = pygame.image.load("bouton_menu_grille4_niveau1.PNG")
BOUTON_GRILLE5_NIVEAU1 = pygame.image.load("bouton_menu_grille5_niveau1.PNG")
BOUTON_GRILLE6_NIVEAU1 = pygame.image.load("bouton_menu_grille6_niveau1.PNG")
BOUTON_GRILLE7_NIVEAU1 = pygame.image.load("bouton_menu_grille7_niveau1.PNG")
BOUTON_GRILLE8_NIVEAU1 = pygame.image.load("bouton_menu_grille8_niveau1.PNG")
BOUTON_GRILLE9_NIVEAU1 = pygame.image.load("bouton_menu_grille9_niveau1.PNG")

            #(b) Boutons grilles niveau 1 résolues
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille1_niveau1_resolu2.PNG")
BOUTON_GRILLE2_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille2_niveau1_resolu.PNG")
BOUTON_GRILLE3_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille3_niveau1_resolu2.PNG")
BOUTON_GRILLE4_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille4_niveau1_resolu.PNG")
BOUTON_GRILLE5_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille5_niveau1_resolu.PNG")
BOUTON_GRILLE6_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille6_niveau1_resolu.PNG")
BOUTON_GRILLE7_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille7_niveau1_resolu.PNG")
BOUTON_GRILLE8_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille8_niveau1_resolu.PNG")
BOUTON_GRILLE9_NIVEAU1_RESOLUE = pygame.image.load("bouton_menu_grille9_niveau1_resolu.PNG")

            #(c) Boutons grilles niveau 2 vides
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU2 = pygame.image.load("bouton_menu_grille1_niveau2.PNG")
BOUTON_GRILLE2_NIVEAU2 = pygame.image.load("bouton_menu_grille2_niveau2.PNG")
BOUTON_GRILLE3_NIVEAU2 = pygame.image.load("bouton_menu_grille3_niveau2.PNG")
BOUTON_GRILLE4_NIVEAU2 = pygame.image.load("bouton_menu_grille4_niveau2.PNG")
BOUTON_GRILLE5_NIVEAU2 = pygame.image.load("bouton_menu_grille5_niveau2.PNG")
BOUTON_GRILLE6_NIVEAU2 = pygame.image.load("bouton_menu_grille6_niveau2.PNG")
BOUTON_GRILLE7_NIVEAU2 = pygame.image.load("bouton_menu_grille7_niveau2.PNG")
BOUTON_GRILLE8_NIVEAU2 = pygame.image.load("bouton_menu_grille8_niveau2.PNG")
BOUTON_GRILLE9_NIVEAU2 = pygame.image.load("bouton_menu_grille9_niveau2.PNG")

            #(d) Boutons grilles niveau 2 résolues
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille1_niveau2_resolu.PNG")
BOUTON_GRILLE2_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille2_niveau2_resolu.PNG")
BOUTON_GRILLE3_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille3_niveau2_resolu.PNG")
BOUTON_GRILLE4_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille4_niveau2_resolu.PNG")
BOUTON_GRILLE5_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille5_niveau2_resolu.PNG")
BOUTON_GRILLE6_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille6_niveau2_resolu.PNG")
BOUTON_GRILLE7_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille7_niveau2_resolu.PNG")
BOUTON_GRILLE8_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille8_niveau2_resolu.PNG")
BOUTON_GRILLE9_NIVEAU2_RESOLUE = pygame.image.load("bouton_menu_grille9_niveau2_resolu.PNG")

            #(e) Boutons grilles niveau 3 vide
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU3 = pygame.image.load("bouton_menu_grille1_niveau3.PNG")
BOUTON_GRILLE2_NIVEAU3 = pygame.image.load("bouton_menu_grille2_niveau3.PNG")
BOUTON_GRILLE3_NIVEAU3 = pygame.image.load("bouton_menu_grille3_niveau3.PNG")
BOUTON_GRILLE4_NIVEAU3 = pygame.image.load("bouton_menu_grille4_niveau3.PNG")
BOUTON_GRILLE5_NIVEAU3 = pygame.image.load("bouton_menu_grille5_niveau3.PNG")
BOUTON_GRILLE6_NIVEAU3 = pygame.image.load("bouton_menu_grille6_niveau3.PNG")
BOUTON_GRILLE7_NIVEAU3 = pygame.image.load("bouton_menu_grille7_niveau3.PNG")
BOUTON_GRILLE8_NIVEAU3 = pygame.image.load("bouton_menu_grille8_niveau3.PNG")
BOUTON_GRILLE9_NIVEAU3 = pygame.image.load("bouton_menu_grille9_niveau3.PNG")

            #(f) Boutons grilles niveau 3 résolues
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille1_niveau3_resolu.PNG")
BOUTON_GRILLE2_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille2_niveau3_resolu.PNG")
BOUTON_GRILLE3_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille3_niveau3_resolu.PNG")
BOUTON_GRILLE4_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille4_niveau3_resolu.PNG")
BOUTON_GRILLE5_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille5_niveau3_resolu.PNG")
BOUTON_GRILLE6_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille6_niveau3_resolu.PNG")
BOUTON_GRILLE7_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille7_niveau3_resolu.PNG")
BOUTON_GRILLE8_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille8_niveau3_resolu.PNG")
BOUTON_GRILLE9_NIVEAU3_RESOLUE = pygame.image.load("bouton_menu_grille9_niveau3_resolu.PNG")

            #(e) Boutons grilles niveau 4 vide
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE2_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE3_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE4_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE5_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE6_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE7_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE8_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")
BOUTON_GRILLE9_NIVEAU4 = pygame.image.load("bouton_menu_grille_vide_niveau4.PNG")

            #(f) Boutons grilles niveau 4 résolus
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOUTON_GRILLE1_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille1_niveau4_resolu.PNG")
BOUTON_GRILLE2_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille2_niveau4_resolu.PNG")
BOUTON_GRILLE3_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille3_niveau4_resolu.PNG")
BOUTON_GRILLE4_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille4_niveau4_resolu.PNG")
BOUTON_GRILLE5_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille5_niveau4_resolu.PNG")
BOUTON_GRILLE6_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille6_niveau4_resolu.PNG")
BOUTON_GRILLE7_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille7_niveau4_resolu.PNG")
BOUTON_GRILLE8_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille8_niveau4_resolu.PNG")
BOUTON_GRILLE9_NIVEAU4_RESOLUE = pygame.image.load("bouton_menu_grille9_niveau4_resolu.PNG")

            #(e) Autres
            #~~~~~~~~~~~

#Bouton d'une grille vide
BOUTON_GRILLE_VIDE = pygame.image.load("bouton_menu_grille_moyen.PNG")
#Icone d'un cadenas
ICONE_PICROSS_NON_CREE = pygame.image.load("bouton_cadenas.PNG")

        #(3) Barre de progression
        #-------------------------

#Progression : 0 sur 9
BARRE_PROGRESSION0 = pygame.image.load("barre_progression_0sur9.PNG")
#Progression : 1 sur 9
BARRE_PROGRESSION1 = pygame.image.load("barre_progression_1sur9.PNG")
#Progression : 2 sur 9
BARRE_PROGRESSION2 = pygame.image.load("barre_progression_2sur9.PNG")
#Progression : 3 sur 9
BARRE_PROGRESSION3 = pygame.image.load("barre_progression_3sur9.PNG")
#Progression : 4 sur 9
BARRE_PROGRESSION4 = pygame.image.load("barre_progression_4sur9.PNG")
#Progression : 5 sur 9
BARRE_PROGRESSION5 = pygame.image.load("barre_progression_5sur9.PNG")
#Progression : 6 sur 9
BARRE_PROGRESSION6 = pygame.image.load("barre_progression_6sur9.PNG")
#Progression : 7 sur 9
BARRE_PROGRESSION7 = pygame.image.load("barre_progression_7sur9.PNG")
#Progression : 8 sur 9
BARRE_PROGRESSION8 = pygame.image.load("barre_progression_8sur9.PNG")
#Progression : 9 sur 9
BARRE_PROGRESSION9 = pygame.image.load("barre_progression_9sur9.PNG")

    #(II) Dimension des images
    #===========================================================================

        #(1) Boutons parties du menu principal
        #--------------------------------------

#Longueur des boutons : "picross à résoudre", "résolution de picross", "création de picross"
LONGUEUR_BOUTONS_PARTIES = 190
#Hauteur des boutons : "picross à résoudre", "résolution de picross", "création de picross"
HAUTEUR_BOUTONS_PARTIES = 213

        #(2) Bouton du tutoriel
        #-----------------------

#Longueur du bouton : "tutoriel"
LONGUEUR_BOUTON_TUTORIEL = 100
#Hauteur du bouton : "tutoriel"
HAUTEUR_BOUTON_TUTORIEL = 25

        #(3) Bouton retour
        #------------------

#Longueur du bouton : "retour"
LONGUEUR_BOUTON_RETOUR = 100
#Hauteur du bouton : "retour"
HAUTEUR_BOUTON_RETOUR = 25

        #(4) Bouton des niveaux de la partie "Picross à résoudre"
        #---------------------------------------------------------

#Taille coté boutons Niveaux
DIMENSION_COTE_BOUTONS_NIVEAUX = 150

#-------------------------------------------------------------------------------
#                                  TEXTES
#-------------------------------------------------------------------------------

    #(I) Titres de niveaux
    #===========================================================================

TITRE_NIVEAU1 = "NIVEAU FACILE"
TITRE_NIVEAU2 = "NIVEAU MOYEN"
TITRE_NIVEAU3 = "NIVEAU DIFFICILE"
TITRE_NIVEAU4 = "NIVEAU EXTRÊME"
TITRE_NIVEAU_PERSONNALISE = "NIVEAU PERSONNALISE"

#-------------------------------------------------------------------------------
#                              NOM DES COULEURS
#-------------------------------------------------------------------------------

    #(I) Couleurs globales
    #===========================================================================

#Noir
NOIR = (0,0,0)
#Bleu clair (=vert pin)
VERT_PIN = (1, 121,111)
#Bleu foncé (=canard)
CANARD = (4,139,154)
#Beige (=blanc crème)
BLANC_CREME = (253, 241, 184)

    #(II) Couleurs spécifiques aux niveaux
    #===========================================================================

#Bleu : associé au niveau "Mon niveau"
BLEU_MON_NIVEAU = (11, 140, 210)
#Vert : associé au niveau "Niveau 1"
VERT_NIVEAU1 = (34 , 177, 76)
#Jaune : associé au niveau "Niveau 2"
JAUNE_NIVEAU2 = (255, 201,14)
#Orange : associé au niveau "Niveau 3"
ORANGE_NIVEAU3 = (255, 127, 39)
#Rouge : associé au niveau "Niveau 4"
ROUGE_NIVEAU4 = (237, 28, 36)

#-------------------------------------------------------------------------------
#                               ZONES CLIQUABLES
#-------------------------------------------------------------------------------

    #(I) Accès aux grilles des niveaux de la partie "Picross à résoudre"
    #===========================================================================

#Zone de l'interface correspondant à la grille 1
Rectgrille1 = pygame.Rect(200, 130, 150, 150)
#Zone de l'interface correspondant à la grille 2
Rectgrille2 = pygame.Rect(405, 130, 150, 150)
#Zone de l'interface correspondant à la grille 3
Rectgrille3 = pygame.Rect(610, 130, 150, 150)
#Zone de l'interface correspondant à la grille 4
Rectgrille4 = pygame.Rect(200, 305, 150, 150)
#Zone de l'interface correspondant à la grille 5
Rectgrille5 = pygame.Rect(405, 305, 150, 150)
#Zone de l'interface correspondant à la grille 6
Rectgrille6 = pygame.Rect(610, 305, 150, 150)
#Zone de l'interface correspondant à la grille 7
Rectgrille7 = pygame.Rect(200, 480, 150, 150)
#Zone de l'interface correspondant à la grille 8
Rectgrille8 = pygame.Rect(405, 480, 150, 150)
#Zone de l'interface correspondant à la grille 9
Rectgrille9 = pygame.Rect(610, 480, 150, 150)

    #(II) Accès aux niveaux de la partie "Picross à résoudre"
    #===========================================================================

#Zone de l'interface correspondant au niveau 1
Rect_bouton_Niveau1 = pygame.Rect(262, 112, 125, 125)
#Zone de l'interface correspondant au niveau 2
Rect_bouton_Niveau2 = pygame.Rect(542, 112, 125, 125)
#Zone de l'interface correspondant au niveau 3
Rect_bouton_Niveau3 = pygame.Rect(262, 422, 125, 125)
#Zone de l'interface correspondant au niveau 4
Rect_bouton_Niveau4 = pygame.Rect(542, 422, 125, 125)
#Zone de l'interface correspondant au niveau personnalisé
Rect_bouton_MonNiveau = pygame.Rect(402, 267, 125, 125)

    #(III) Accès aux parties du jeu
    #===========================================================================

#Zone de l'interface correspondant à la partie "Picross à résoudre"
Rect_picross_a_resoudre = pygame.Rect(57, 300, 190, 213)
#Zone de l'interface correspondant à la partie "Résolution de Picross"
Rect_resolution_de_picross = pygame.Rect(304, 300, 190, 213)
#Zone de l'interface correspondant à la partie "Création Picross"
Rect_creation_picross = pygame.Rect(551, 300, 190, 213)