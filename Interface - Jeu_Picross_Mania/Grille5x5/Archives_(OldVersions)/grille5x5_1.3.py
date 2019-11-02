# Créé par Fabien ( et Quentin ) le 21/03/2016 en Python 3.2
# création d'une grille de jeu picross de dimension 5x5
# corps du programme

# on importe le module pygame qui nous permet de créer l'interface graphique
import pygame
from pygame.locals import *

# on rattache le corps du programme aux annexes pour plus de clarté:
# les classes et les constantes du programme
from classes import *
from constantes import *

# initialisation du module pygame (étape nécessaire pour utiliser le module)
pygame.init()

# création d'une variable fenetre qui affiche la fenetre du jeu
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

# Variable qui continue la boucle si = 1, stoppe si = 0
# cela permet de garder la fenetre ouverte
continuer = 1

#BOUCLE PRINCIPAL
# fermeture de la fenetre
while continuer:
	for event in pygame.event.get():   #On parcourt la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle ce qui ferme la fenetre

    #Chargement du fond blanc
	"""fond = pygame.image.load(fond_contour).convert()"""

    #Affichages du fond blanc aux nouvelles positions
	"""fenetre.blit(fond, (150,150))"""

    # Classe grille qui génère la grille (suite de petites images)
    # a partir du fichier texte "fichier"
    # SI ON SUPPRIME LES TROIS LIGNES CI DESSOUS, LE RESTE DU PROGRAMME TOURNE NORMALEMENT !!!

	#Rafraichissement de la fenetre (nécessaire pour afficher l'image)
	pygame.display.flip()

#Génération d'un niveau à partir d'un fichier


# permet de fermet la fenetre sans bug (sans cela le programme ne repond plus
# lors de la fermeture de la fenetre)
pygame.quit()
