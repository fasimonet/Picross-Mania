#Cree par Fabien et Quentin le 01/05/2016 en Python 3.2

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

# v --> case vide
# n --> case noircie
# c --> case cochée

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

#Répertoire des matrices des picross du niveau 2

#===============================================================================
#          MATRICES CORRESPONDANT AUX PICROSS A RESOUDRE DU NIVEAU 2
#===============================================================================

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 1
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 1
#-------------------------------------------

MAT_HAUT_NIV2_PIC1 = array([(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                            (0, 0, 2, 2, 0, 0, 0, 0, 0, 0),
                            (0, 0, 2, 2, 2, 0, 5, 5, 0, 0),
                            (2, 4, 1, 2, 7, 10, 2, 1, 4, 2)])


# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 1
#---------------------------------------------

MAT_GAUC_NIV2_PIC1 = array([(0, 0, 0, 0, 2),
                            (0, 0, 0, 0, 4),
                            (0, 0, 0, 2, 3),
                            (0, 0, 0, 2, 5),
                            (0, 0, 0, 2, 7),
                            (0, 0, 0, 0, 10),
                            (0, 0, 2, 2, 2),
                            (0, 0, 0, 0, 2),
                            (0, 0, 0, 0, 4),
                            (0, 0, 0, 0, 6)])


# MATRICE DE LA GRILLE CENTRALE DU PICROSS 1
#--------------------------------------------

MAT_CENT_NIV2_PIC1 = array([(2, 2, 2, 2, 1, 1, 2, 2, 2, 2),
                            (2, 2, 2, 1, 1, 1, 1, 2, 2, 2),
                            (2, 2, 1, 1, 2, 1, 1, 1, 2, 2),
                            (2, 1, 1, 2, 1, 1, 1, 1, 1, 2),
                            (1, 1, 2, 1, 1, 1, 1, 1, 1, 1),
                            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                            (2, 1, 1, 2, 1, 1, 2, 1, 1, 2),
                            (2, 2, 2, 2, 1, 1, 2, 2, 2, 2),
                            (2, 2, 2, 1, 1, 1, 1, 2, 2, 2),
                            (2, 2, 1, 1, 1, 1, 1, 1, 2, 2),])

""" RENDU DE LA GRILLE CENTRALE :

    x x x x ■ ■ x x x x
    x x x ■ ■ ■ ■ x x x
    x x ■ ■ x ■ ■ ■ x x
    x ■ ■ x ■ ■ ■ ■ ■ x
    ■ ■ x ■ ■ ■ ■ ■ ■ ■
    ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
    x ■ ■ x ■ ■ x ■ ■ x
    x x x x ■ ■ x x x x
    x x x ■ ■ ■ ■ x x x
    x x ■ ■ ■ ■ ■ ■ x x

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 2
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 2
#-------------------------------------------

MAT_HAUT_NIV2_PIC2 = array([(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                            (0, 1, 1, 0, 0, 0, 1, 1, 1, 0),
                            (0, 1, 2, 3, 0, 0, 1, 2, 1, 0),
                            (7, 1, 1, 1, 8, 8, 1, 1, 1, 7)])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 2
#---------------------------------------------

MAT_GAUC_NIV2_PIC2 = array([(0, 0, 0, 1, 1),
                            (0, 1, 1, 1, 1),
                            (0, 0, 0, 0, 6),
                            (0, 0, 0, 0, 10),
                            (0, 0, 1, 2, 1),
                            (0, 0, 1, 2, 1),
                            (0, 0, 1, 2, 1),
                            (0, 0, 1, 2, 1),
                            (0, 0, 1, 2, 1),
                            (0, 0, 0, 0, 10)])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 2
#--------------------------------------------

MAT_CENT_NIV2_PIC2 = array([(2, 2, 1, 2, 2, 2, 2, 1, 2, 2),
                            (2, 1, 2, 1, 2, 2, 1, 2, 1, 2),
                            (2, 2, 1, 1, 1, 1, 1, 1, 2, 2),
                            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                            (1, 2, 2, 2, 1, 1, 2, 2, 2, 1),
                            (1, 2, 2, 2, 1, 1, 2, 2, 2, 1),
                            (1, 2, 2, 2, 1, 1, 2, 2, 2, 1),
                            (1, 2, 2, 2, 1, 1, 2, 2, 2, 1),
                            (1, 2, 2, 2, 1, 1, 2, 2, 2, 1),
                            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),])

""" RENDU DE LA GRILLE CENTRALE :

    x x ■ x x x x ■ x x
    x ■ x ■ x x ■ x ■ x
    x x ■ ■ ■ ■ ■ ■ x x
    ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
    ■ x x x ■ ■ x x x ■
    ■ x x x ■ ■ x x x ■
    ■ x x x ■ ■ x x x ■
    ■ x x x ■ ■ x x x ■
    ■ x x x ■ ■ x x x ■
    ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

"""

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 3
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 3
#-------------------------------------------

Matrice_grille_haut3_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 3
#---------------------------------------------

Matrice_grille_gauche3_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 3
#--------------------------------------------

Matrice_grille_centrale3_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 4
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 4
#-------------------------------------------

Matrice_grille_haut4_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 4
#---------------------------------------------

Matrice_grille_gauche4_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 4
#--------------------------------------------

Matrice_grille_centrale4_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 5
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 5
#-------------------------------------------

Matrice_grille_haut5_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 5
#---------------------------------------------

Matrice_grille_gauche5_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 5
#--------------------------------------------

Matrice_grille_centrale5_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 6
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 6
#-------------------------------------------

Matrice_grille_haut6_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 6
#---------------------------------------------

Matrice_grille_gauche6_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 6
#--------------------------------------------

Matrice_grille_centrale6_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 7
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 7
#-------------------------------------------

Matrice_grille_haut7_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 7
#---------------------------------------------

Matrice_grille_gauche7_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 7
#--------------------------------------------

Matrice_grille_centrale7_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 8
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 8
#-------------------------------------------

Matrice_grille_haut8_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 8
#---------------------------------------------

Matrice_grille_gauche8_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 8
#--------------------------------------------

Matrice_grille_centrale8_niveau2 = np.matrix([])

#-------------------------------------------------------------------------------
#                              PICROSS NUMERO 9
#-------------------------------------------------------------------------------

# MATRICE DE LA GRILLE DU HAUT DU PICROSS 9
#-------------------------------------------

Matrice_grille_haut9_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE DE GAUCHE DU PICROSS 9
#---------------------------------------------

Matrice_grille_gauche9_niveau2 = np.matrix([])

# MATRICE DE LA GRILLE CENTRALE DU PICROSS 9
#--------------------------------------------

Matrice_grille_centrale9_niveau2 = np.matrix([])
