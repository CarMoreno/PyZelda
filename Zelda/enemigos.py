import pygame
import cursor_mouse
class Enemigos(pygame.sprite.Sprite):
	"""Se encarga de gestionar tareas de enemigos"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)#Heredamos de la clase sprite
		#Imagenes
		self.rata1 = pygame.image.load("imagenes/enemigos/rata1.png")#ENEMIGO RATA
		self.rata2 = pygame.image.load("imagenes/enemigos/rata2.png")#ENEMIGO RATA
		self.rata3 = pygame.image.load("imagenes/enemigos/rata3.png")#ENEMIGO RATA
		self.rata4 = pygame.image.load("imagenes/enemigos/rata4.png")#ENEMIGO RATA

		self.guardia1 = pygame.image.load("imagenes/enemigos/guardia1.png")#ENEMIGO GUARDIA
		self.guardia2 = pygame.image.load("imagenes/enemigos/guardia2.png")#ENEMIGO GUARDIA
		self.guardia3 = pygame.image.load("imagenes/enemigos/guardia3.png")#ENEMIGO GUARDIA
		self.guardia4 = pygame.image.load("imagenes/enemigos/guardia4.png")#ENEMIGO GUARDIA
		
		self.esqueleto1 = pygame.image.load("imagenes/enemigos/esqueleto1.png")#ENEMIGO ESQUELETO
		self.esqueleto2 = pygame.image.load("imagenes/enemigos/esqueleto2.png")#ENEMIGO ESQUELETO
		self.esqueleto3 = pygame.image.load("imagenes/enemigos/esqueleto3.png")#ENEMIGO ESQUELETO
		self.esqueleto4 = pygame.image.load("imagenes/enemigos/esqueleto4.png")#ENEMIGO ESQUELETO
		
		# self.eliminado= pygame.image.load("imagenes/eliminado.png")
		self.piso = pygame.image.load("imagenes/piso.png")#Imagen del piso
		self.piso2 = pygame.image.load("imagenes/piso2.png")#Imagen del piso
		self.piso3 = pygame.image.load("imagenes/piso3.png")#Imagen del piso

		#Rectangulos de las imagenes
		self.rata1_rect = self.rata1.get_rect(x = 100, y = 100)
		self.rata2_rect = self.rata2.get_rect(x = 200, y = 100)
		self.rata3_rect = self.rata3.get_rect(x = 300, y = 100)
		self.rata4_rect = self.rata4.get_rect(x = 400, y = 100)

		self.guardia1_rect = self.guardia1.get_rect(x = 100, y = 200)
		self.guardia2_rect = self.guardia2.get_rect(x = 200, y = 200)
		self.guardia3_rect = self.guardia3.get_rect(x = 300, y = 200)
		self.guardia4_rect = self.guardia4.get_rect(x = 400, y = 200)

		self.esqueleto1_rect = self.esqueleto1.get_rect(x = 100, y = 300)
		self.esqueleto2_rect = self.esqueleto2.get_rect(x = 200, y = 300)
		self.esqueleto3_rect = self.esqueleto3.get_rect(x = 300, y = 300)
		self.esqueleto4_rect = self.esqueleto4.get_rect(x = 400, y = 300)

		#Transformaciones
		self.rata_transformada = pygame.transform.scale(self.rata1, (30,40))
		self.guardia_transformado = pygame.transform.laplacian(self.guardia1)
		self.esqueleto_transformado = pygame.transform.scale(self.esqueleto1, (30,40)) 

		#Estados. 
		self.VIVO = True 
		self.MUERTO = False
		self.estadoRata1 = self.estadoRata2 = self.estadoRata3 = self.estadoRata4 =  self.VIVO
 		self.estadoGuardia1 = self.estadoGuardia2 = self.estadoGuardia3 = self.estadoGuardia4 = self.VIVO
 		self.estadoEsqueleto1 = self.estadoEsqueleto2 = self.estadoEsqueleto3 = self.estadoEsqueleto4 = self.VIVO

	def getEnemigos(self):
		"""Retorna un arreglo con tuplas en su interior, cuyo par es (rectanguloEnemigo, estadoEnemigo)"""
		informacionEnemigos = [

		(self.rata1_rect, self.estadoRata1), 
		(self.rata2_rect, self.estadoRata2),
		(self.rata3_rect, self.estadoRata3),
		(self.rata4_rect, self.estadoRata4),
		(self.guardia1_rect, self.estadoGuardia1),
		(self.guardia2_rect, self.estadoGuardia2),
		(self.guardia3_rect, self.estadoGuardia3),
		(self.guardia4_rect, self.estadoGuardia4),
		(self.esqueleto1_rect, self.estadoEsqueleto1),
		(self.esqueleto2_rect, self.estadoEsqueleto2),
		(self.esqueleto3_rect, self.estadoEsqueleto3),
		(self.esqueleto4_rect, self.estadoEsqueleto4)
		
		]		

		return informacionEnemigos

	def getEstadosEnemigos(self):
		"""Retorna un arreglo con los estados de los enemigos"""
		estadosEnemigos = [
			self.estadoRata1, self.estadoRata2, self.estadoRata3, self.estadoRata4,
			self.estadoGuardia1, self.estadoGuardia2, self.estadoGuardia3, self.estadoGuardia4,
			self.estadoEsqueleto1, self.estadoEsqueleto2, self.estadoEsqueleto3, self.estadoEsqueleto4
		]
		return estadosEnemigos				


	def morir(self, screen, cursor):
		'''Aplica la trasformacion y mata al enemigo con un click'''	
		click = pygame.mouse.get_pressed()
		if cursor.colliderect(self.rata1_rect):#Si hay colision entre le cursor y el rectangulo de la img
			if click[0] == 1:#si hay click entonces
				self.rata1 = self.piso#Primero se cambia la imagen del enemigo por un pedazo de piso
				screen.blit(self.rata1, self.rata1_rect)#dibujamos el pdazo de piso
				self.rata1 = self.rata_transformada#Luego transformamos al enemigo
				self.estadoRata1 = self.MUERTO #Si se dio click fue porque matamos a un enemigo, y su estado cambia a self.MUERTO
				screen.blit(self.rata1, self.rata1_rect)#Y encima la transformacion de la imagen
		if cursor.colliderect(self.rata2_rect):
			if click[0] == 1:
				self.rata2 = self.piso2
				screen.blit(self.rata2, self.rata2_rect)
				self.rata2 = self.rata_transformada
				self.estadoRata2 = self.MUERTO #Porque esta convertido
				screen.blit(self.rata2, self.rata2_rect)
		if cursor.colliderect(self.rata3_rect):
			if click[0] == 1:
				self.rata3 = self.piso3
				screen.blit(self.rata3, self.rata3_rect)
				self.rata3 = self.rata_transformada
				screen.blit(self.rata3, self.rata3_rect)
				self.estadoRata3 = self.MUERTO #Porque esta convertido

		if cursor.colliderect(self.rata4_rect):
			if click[0] == 1:
				self.rata4 = self.piso
				screen.blit(self.rata4, self.rata4_rect)
				self.rata4 = self.rata_transformada
				screen.blit(self.rata4, self.rata4_rect)
				self.estadoRata4 = self.MUERTO
		if cursor.colliderect(self.guardia1_rect):
			if click[0] == 1:
				self.guardia1 = self.piso
				screen.blit(self.guardia1, self.guardia1_rect)
				self.guardia1 = self.guardia_transformado
				screen.blit(self.guardia1, self.guardia1_rect)
				self.estadoGuardia1 = self.MUERTO

		if cursor.colliderect(self.guardia2_rect):
			if click[0] == 1:
				self.guardia2 = self.piso
				screen.blit(self.guardia2, self.guardia2_rect)
				self.guardia2 = self.guardia_transformado
				screen.blit(self.guardia2, self.guardia2_rect)
				self.estadoGuardia2 = self.MUERTO
		if cursor.colliderect(self.guardia3_rect):
			if click[0] == 1:
				self.guardia3 = self.piso
				screen.blit(self.guardia3, self.guardia3_rect)
				self.guardia3 = self.guardia_transformado
				screen.blit(self.guardia3, self.guardia3_rect)
				self.estadoGuardia3 = self.MUERTO
		if cursor.colliderect(self.guardia4_rect):
			if click[0] == 1:
				self.guardia4 = self.piso
				screen.blit(self.guardia4, self.guardia4_rect)
				self.guardia4 = self.guardia_transformado
				screen.blit(self.guardia1, self.guardia4_rect)							
				self.estadoGuardia4 = self.MUERTO
		if cursor.colliderect(self.esqueleto1_rect):
			if click[0] == 1:
				self.esqueleto1 = self.piso
				screen.blit(self.esqueleto1, self.esqueleto1_rect)
				self.esqueleto1 = self.esqueleto_transformado
				screen.blit(self.esqueleto1, self.esqueleto1_rect)		
				self.estadoEsqueleto1 = self.MUERTO
		if cursor.colliderect(self.esqueleto2_rect):
			if click[0] == 1:
				self.esqueleto2 = self.piso
				screen.blit(self.esqueleto2, self.esqueleto2_rect)
				self.esqueleto2 = self.esqueleto_transformado
				screen.blit(self.esqueleto2, self.esqueleto2_rect)
				self.estadoEsqueleto2 = self.MUERTO
		if cursor.colliderect(self.esqueleto3_rect):
			if click[0] == 1:
				self.esqueleto3 = self.piso
				screen.blit(self.esqueleto3, self.esqueleto3_rect)
				self.esqueleto3 = self.esqueleto_transformado
				screen.blit(self.esqueleto3, self.esqueleto3_rect)
				self.estadoEsqueleto3 = self.MUERTO
		if cursor.colliderect(self.esqueleto4_rect):
			if click[0] == 1:
				self.esqueleto4 = self.piso
				screen.blit(self.esqueleto4, self.esqueleto4_rect)
				self.esqueleto4 = self.esqueleto_transformado
				screen.blit(self.esqueleto4, self.esqueleto4_rect)
				self.estadoEsqueleto4 = self.MUERTO

		screen.blit(self.rata1, self.rata1_rect)
		screen.blit(self.rata2, self.rata2_rect)
		screen.blit(self.rata3, self.rata3_rect)
		screen.blit(self.rata4, self.rata4_rect)
		screen.blit(self.guardia1, self.guardia1_rect)
		screen.blit(self.guardia2, self.guardia2_rect)
		screen.blit(self.guardia3, self.guardia3_rect)
		screen.blit(self.guardia4, self.guardia4_rect)
		screen.blit(self.esqueleto1, self.esqueleto1_rect)
		screen.blit(self.esqueleto2, self.esqueleto2_rect)
		screen.blit(self.esqueleto3, self.esqueleto3_rect)
		screen.blit(self.esqueleto4, self.esqueleto4_rect)
	