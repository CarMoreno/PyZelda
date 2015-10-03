import pygame
#import enemigos
from pygame.locals import *
#import enemigos
import escenario2
import escenario1
# import cursor_mouse
#import link


class SceneOne:
	"""Desde aca se cargan todos los escenarios que tendran lugar en el juego"""
	def __init__(self):
		self.escena2 = escenario2.Escenario2()
		self.escena1 = escenario1.Escenario1()

	def cargarEscena1(self, screen, coord_x, coord_y):
		miescena = self.escena1.run(screen, coord_x, coord_y)

	def cargarEscena2(self, screen, coorx, coory):
		miescena = self.escena2.run2(screen, coorx, coory)