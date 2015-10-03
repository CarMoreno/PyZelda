import pygame
class CursorMouse(pygame.Rect):
	"""docstring for CursorMouse
	Clase que se encarga de gestionar el corsor del mouse para que este pueda interactuar con
	distintos elementos de la aplicacion"""
	def __init__(self):
		pygame.Rect.__init__(self, 0, 0, 4, 4)#Definimos un rectangulo con ancho y largo de 1 y poscion x,y de 0
			
	def actualizar(self):
		self.left, self.top = pygame.mouse.get_pos()#Devuelve una tupla con la posicion del mouse
		#print self.left, self.top