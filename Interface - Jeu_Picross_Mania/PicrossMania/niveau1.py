﻿#Cree par Fabien et Sinan le 01/05/2016 en Python 3.2

#===============================================================================
#                        IMPORTATION DES BIBLIOTHEQUES
#===============================================================================

from numpy import *

#===============================================================================
#                             VARIABLES UTILISEES
#===============================================================================

#-------------------------------------------------------------------------------
#                               GRILLE CENTRALE
#-------------------------------------------------------------------------------

# 0 --> case vide
# 1 --> case noircie
# 2 --> case cochée

#-------------------------------------------------------------------------------
#                     GRILLE DE GAUCHE ET GRILLE DU HAUT
#-------------------------------------------------------------------------------

# 0 --> la case contient un "0" ou elle est vide
# 1 --> la case contient un "1"
# 2 --> la case contient un "2"
# 3 --> la case contient un "3"
# 4 --> la case contient un "4"
# 5 --> la case contient un "5"

#===============================================================================
#                            PRINCIPE DU PROGRAMME
#===============================================================================

# Répertoire des matrices des picross du niveau 1

#===============================================================================
#          MATRICES CORRESPONDANT AUX PICROSS A RESOUDRE DU NIVEAU 1
#===============================================================================

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 1
#------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 1
#-------------------------------------------

MAT_HAUT_NIV1_PIC1 = array([(0, 0, 0, 0, 0),
                            (1, 0, 1, 0, 1),
                            (1, 5, 1, 5, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 1
#---------------------------------------------

MAT_GAUC_NIV1_PIC1 = array([(0, 1, 1),
                            (0, 0, 5),
                            (0, 1, 1),
                            (0, 0, 5),
                            (0, 1, 1)])


# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

MAT_CENT_NIV1_PIC1 = array([(2, 1, 2, 1, 2),
                            (1, 1, 1, 1, 1),
                            (2, 1, 2, 1, 2),
                            (1, 1, 1, 1, 1),
                            (2, 1, 2, 1, 2)])

""" RENDU DE LA GRILLE CENTRALE :

    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x
    ■ ■ ■ ■ ■
    x ■ x ■ x

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 2
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 2
#-------------------------------------------

MAT_HAUT_NIV1_PIC2 = array([(0, 1, 0, 1, 0),
                            (1, 1, 1, 1, 1),
                            (1, 1, 1, 1, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 2
#---------------------------------------------

MAT_GAUC_NIV1_PIC2 = array([(0, 1, 1),
                            (1, 1 ,1),
                            (0, 1, 1),
                            (1, 1, 1),
                            (0, 1, 1)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 2
#--------------------------------------------

MAT_CENT_NIV1_PIC2 = array([(2, 1, 2, 1, 2),
                            (1, 2, 1, 2, 1),
                            (2, 1, 2, 1, 2),
                            (1, 2, 1, 2, 1),
                            (2, 1, 2, 1, 2)])

""" RENDU DE LA GRILLE CENTRALE :

    x ■ x ■ x
    ■ x ■ x ■
    x ■ x ■ x
    ■ x ■ x ■
    x ■ x ■ x

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 3
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 3
#-------------------------------------------

MAT_HAUT_NIV1_PIC3 = array([(0, 0, 0, 0, 0),
                            (0, 2, 1, 2, 0),
                            (3, 2, 1, 2, 3)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 3
#---------------------------------------------

MAT_GAUC_NIV1_PIC3 = array([(0, 0, 3),
                            (0, 2, 2),
                            (0, 1, 1),
                            (0, 2, 2),
                            (0, 0, 3)])


# MATRICE DE LA GRILLE CENTRALE DU PICROSS 3
#--------------------------------------------

MAT_CENT_NIV1_PIC3 = array([(2, 1, 1, 1, 2),
                            (1, 1, 2, 1, 1),
                            (1, 2, 2, 2, 1),
                            (1, 1, 2, 1, 1),
                            (2, 1, 1, 1, 2)])

""" RENDU DE LA GRILLE CENTRALE :

    x ■ ■ ■ x
    ■ ■ x ■ ■
    ■ x x x ■
    ■ ■ x ■ ■
    x ■ ■ ■ x

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 4
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 4
#-------------------------------------------

MAT_HAUT_NIV1_PIC4 = array([(0, 0, 1, 0, 0),
                            (1, 2, 1, 2, 1),
                            (1, 2, 1, 2, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 4
#---------------------------------------------

MAT_GAUC_NIV1_PIC4 = array([(0, 0, 5),
                            (0, 1, 1),
                            (0, 0, 1),
                            (0, 1, 1),
                            (0, 0, 5)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 4
#--------------------------------------------

MAT_CENT_NIV1_PIC4 = array([(1, 1, 1, 1, 1),
                            (2, 1, 2, 1, 2),
                            (2, 2, 1, 2, 2),
                            (2, 1, 2, 1, 2),
                            (1, 1, 1, 1, 1)])

""" RENDU DE LA GRILLE CENTRALE :

    ■ ■ ■ ■ ■
    x ■ x ■ x
    x x ■ x x
    x ■ x ■ x
    ■ ■ ■ ■ ■

"""
#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 5
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 5
#-------------------------------------------

MAT_HAUT_NIV1_PIC5 = array([(1, 0, 0, 0, 1),
                            (1, 0, 0, 0, 1),
                            (1, 1, 5, 1, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 5
#---------------------------------------------

MAT_GAUC_NIV1_PIC5 = array([(1, 1, 1),
                            (0, 0, 1),
                            (0, 0, 5),
                            (0, 0, 1),
                            (1, 1, 1)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 5
#--------------------------------------------

MAT_CENT_NIV1_PIC5 = array([(1, 2, 1, 2, 1),
                            (2, 2, 1, 2, 2),
                            (1, 1, 1, 1, 1),
                            (2, 2, 1, 2, 2),
                            (1, 2, 1, 2, 1)])

""" RENDU DE LA GRILLE CENTRALE :

    ■ x ■ x ■
    x x ■ x x
    ■ ■ ■ ■ ■
    x x ■ x x
    ■ x ■ x ■

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 6
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 6
#-------------------------------------------

MAT_HAUT_NIV1_PIC6 = array([(0, 0, 1, 0, 0),
                            (0, 1, 1, 1, 0),
                            (5, 1, 1, 1, 5)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 6
#---------------------------------------------

MAT_GAUC_NIV1_PIC6 = array([(0, 0, 5),
                            (0, 1, 1),
                            (1, 1, 1),
                            (0, 1, 1),
                            (0, 0, 5)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 6
#--------------------------------------------

MAT_CENT_NIV1_PIC6 = array([(1, 1, 1, 1, 1),
                            (1, 2, 2, 2, 1),
                            (1, 2, 1, 2, 1),
                            (1, 2, 2, 2, 1),
                            (1, 1, 1, 1, 1)])

""" RENDU DE LA GRILLE CENTRALE :

    ■ ■ ■ ■ ■
    ■ x x x ■
    ■ x ■ x ■
    ■ x x x ■
    ■ ■ ■ ■ ■

"""
#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 7
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 7
#-------------------------------------------

MAT_HAUT_NIV1_PIC7 = array([(0, 0, 0, 0, 0),
                            (2, 2, 0, 2, 2),
                            (1, 2, 2, 2, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 7
#---------------------------------------------

MAT_GAUC_NIV1_PIC7 = array([(0, 2, 2),
                            (0, 2, 2),
                            (0, 0, 0),
                            (0, 0, 5),
                            (0, 0, 3)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 7
#--------------------------------------------

MAT_CENT_NIV1_PIC7 = array([(1, 1, 2, 1, 1),
                            (1, 1, 2, 1, 1),
                            (2, 2, 2, 2, 2),
                            (1, 1, 1, 1, 1),
                            (2, 1, 1, 1, 2)])

""" RENDU DE LA GRILLE CENTRALE :

    ■ ■ x ■ ■
    ■ ■ x ■ ■
    x x x x x
    ■ ■ ■ ■ ■
    x ■ ■ ■ x

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 8
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 8
#-------------------------------------------

MAT_HAUT_NIV1_PIC8 = array([(0, 0, 0, 0, 0),
                            (2, 0, 0, 0, 2),
                            (2, 3, 1, 3, 2)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 8
#---------------------------------------------

MAT_GAUC_NIV1_PIC8 = array([(0, 1, 1),
                            (0, 2, 2),
                            (0, 0, 3),
                            (0, 2, 2),
                            (0, 1, 1)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 8
#--------------------------------------------

MAT_CENT_NIV1_PIC8 = array([(1, 2, 2, 2, 1),
                            (1, 1, 2, 1, 1),
                            (2, 1, 1, 1, 2),
                            (1, 1, 2, 1, 1),
                            (1, 2, 2, 2, 1)])

""" RENDU DE LA GRILLE CENTRALE :

    ■ x x x ■
    ■ ■ x ■ ■
    x ■ ■ ■ x
    ■ ■ x ■ ■
    ■ x x x ■

"""
#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 9
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 9
#-------------------------------------------

MAT_HAUT_NIV1_PIC9 = array([(0, 0, 1, 0, 0),
                            (0, 1, 1, 1, 0),
                            (1, 1, 1, 1, 1)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 9
#---------------------------------------------

MAT_GAUC_NIV1_PIC9 = array([(0, 0, 1),
                            (0, 1, 1),
                            (1, 1, 1),
                            (0, 1, 1),
                            (0, 0, 1)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 9
#--------------------------------------------

MAT_CENT_NIV1_PIC9 = array([(2, 2, 1, 2, 2),
                            (2, 1, 2, 1, 2),
                            (1, 2, 1, 2, 1),
                            (2, 1, 2, 1, 2),
                            (2, 2, 1, 2, 2)])

""" RENDU DE LA GRILLE CENTRALE :

    x x ■ x x
    x ■ x ■ x
    ■ x ■ x ■
    x ■ x ■ x
    x x ■ x x

"""
