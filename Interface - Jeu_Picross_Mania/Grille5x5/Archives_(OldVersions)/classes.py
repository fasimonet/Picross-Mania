# Créé par Fabien, le 21/03/2016 en Python 3.2
# Classes du programme "grille"

class Grille:
	"""Classe permettant de creer une grille"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def generer(self):
		"""Methode permettant de generer le niveau en fonction du fichier.
		On cree une liste generale, contenant une liste par ligne a afficher"""
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite a  la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne a la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau


	def afficher(self, fenetre):
		"""Methode permettant d'afficher la grille en fonction
		de la liste de structure renvoyee par generer()"""
		#Chargement des images (seule celle d'arrivee contient de la transparence)
		croix = pygame.image.load(image_croix).convert()
		carre_noirci = pygame.image.load(image_carre_noirci).convert()

		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position reelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'x':		   #x = Croix
					fenetre.blit(croix, (x,y))
				elif sprite == 'n':		   #n = Case Noircie
					fenetre.blit(case_noircie, (x,y))
				elif sprite == 'v':		   #v = Case Vide
					fenetre.blit(case_vide, (x,y))
				num_case += 1
			num_ligne += 1
