import pygame
import enemigos
import cursor_mouse
import link
import escenario2
import sys
from MUSIC import playPrincipal
# import scene_one


class Escenario1:
	"""Escena uno"""
	def __init__(self):
		self.cursor_mouse = cursor_mouse.CursorMouse()
		self.imagen = pygame.image.load("imagenes/escena1.png").convert()
		self.puerta = pygame.image.load("imagenes/puerta.png").convert()
		self.rect_puerta = self.puerta.get_rect()#Rectangulo de la puerta
		self.rect_puerta.centerx = 300
		self.rect_puerta.centery = 50
		self.rect = self.imagen.get_rect()
		self.enemigos = enemigos.Enemigos()
		self.miLink = link.Link()
		self.rect_link = self.miLink.obtenerRect()
		self.miEscena2 = escenario2.Escenario2()
		#self.sceneoOne = scene_one.SceneOne()

	# def estadoFinal(self):
	# 	self.enemigos.getEstadoFinal()

	def cambiar_escena2(self, screen, coorx, coory, estadosEnemigo):#def run2(self, screen, coord_x, coord_y):
		"""Se gestiona el cambio de escena"""
		estadoFinal = True 
		for estado in estadosEnemigo:
			if estado == False:
				estadoFinal = False
			else:
				estadoFinal = True	 

		if self.rect_link.colliderect(self.rect_puerta) and estadoFinal == False :
			#print "Link colisiono con la puerta"
			self.miEscena2.run2(screen, coorx, coory)

				

	def run(self, screen, coord_x, coord_y):
		"""Corremos el escenario 2"""
		juego_activo = False #variable de control del juego
		playPrincipal()
		while not juego_activo:
			keys = pygame.key.get_pressed() # Tecla presionada
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#pygame.quit()
					sys.exit(0)
						
			screen.blit(self.imagen, self.rect)#Dibuja el fondo de pantalla
			screen.blit(self.puerta, self.rect_puerta)#Dibuja la puerta
			self.miLink.moverSencillo(keys, screen, self.enemigos.getEnemigos())#Mueve a link por la escena
			self.cursor_mouse.actualizar()#Nos sirve para detectar clicks sobre un cuadro en la escena
			self.enemigos.morir(screen, self.cursor_mouse)#Aplica muerte para los enemigos
			self.cambiar_escena2(screen, coord_x, coord_y, self.enemigos.getEstadosEnemigos())#Cambia la escena
			pygame.display.update()	
