#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
import random
#import escenario2
class Link(pygame.sprite.Sprite):
	''' Esta clase permite manejar al personaje principal '''

	def __init__(self):
		''' Constructor '''
		pygame.sprite.Sprite.__init__(self) # constructor de la clase Sprite
		self.imagePerfil = pygame.image.load("imagenes/link2.gif").convert()
		#self.imagenTransformada = pygame.transform.rotate(self.imagePerfil, (180)).convert()
		self.imagenActual = self.imagePerfil

		self.rect = self.imagenActual.get_rect() #  obtiene un rectangulo con las dimensiones y posición 
		self.rect.centerx = 450
		self.rect.centery = 470
		self.vida = 200
		#Constantes para formar el angulo aleatorio
		self.START = 20#minimo
		self.STOP = 361#maximo
		self.STEP = 20#paso

	def obtenerImagen(self):
		''' Retorna la imagen del sprite '''
		return self.imagePerfil


	def obtenerRect(self):
		''' Retorna un rectangulo con las dimensiones de la imagen '''
		return self.rect


	def setImagen(self, nuevaImagen):
		''' Asigna la imagen del sprite '''
		self.imagePerfil = nuevaImagen


	def obtenerVida(self):
		''' Retorna el atributo vida '''
		return self.vida


	def setVida(self, numero):
		''' Asigna la vida '''
		self.vida = numero

	def getRotacion(self, angulo):
		"""Retorna una imagen rotada segun un angulo aleatorio"""
		imagenTransformada = pygame.transform.rotate(self.imagePerfil, (angulo)).convert()
		return imagenTransformada		


	def ataques(self, rival, numero):
		''' Le permite al sprite atacar a otro '''
		imagen = rival.obtenerImagen()
		if numero == 0:			
			nuevaImagen = pygame.transform.rotate(imagen, 45) # Rotación .
			rival.setImagen(nuevaImagen)
			
		if numero == 1:
			nuevaImagen = pygame.transform.smoothscale(imagen, (56, 38)) # Cambia el tamaño de una superficie con suavidad y de forma arbitraria
			rival.setImagen(nuevaImagen)
			
		if numero == 2:
			print "No se quiere atacar :)"



	def transformacion(self, screen, desplazax, desplazay, ganon, x, y):
		''' Permite detectar que hay una colision y aplicar una transformacion'''
		if pygame.sprite.collide_rect(self, ganon): # Detecta si hay colision entre dos sprites
					self.rect.move_ip(desplazax, desplazay) # mueve el rectangulo
					inverso = pygame.transform.laplacian(self.imagePerfil) # Transformacion que busca los bordes en una superficie
					inverso.set_colorkey((0,0,0)) # se usara un color como transparente, en este caso negro
					rect = inverso.get_rect() #  obtiene un rectangulo con las dimensiones y posición de la imagen
					rect.centerx = x 
					rect.centery = y
					screen.blit(inverso, rect)
					pygame.display.update()
		else:
			screen.blit(self.imagePerfil, self.rect) # muestra a link en pantalla


			
	def moverColisionGanon(self, keys, ganon, screen):
		''' Se encarga de mover a link por la ventana y aplicar la transformacion'''
		(x, y) = (self.rect.centerx, self.rect.centery)
		self.transformacion(screen, 0, 0, ganon, x, y)
		if self.rect.top >= 130:
			if keys[K_UP]:
				self.rect.move_ip(0, -2) # mueve el rectangulo
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion(screen, 0, 2, ganon, x, y)
		if self.rect.bottom <= 520:
			if keys[K_DOWN]:
				self.rect.move_ip(0, 2)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion(screen, 0, -2, ganon, x, y)

		if self.rect.right <= 500:
			if keys[K_RIGHT]:
				self.rect.move_ip(2, 0)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion(screen, -2, 0, ganon, x, y)

		if self.rect.left >= 125:
			if keys[K_LEFT]:
				self.rect.move_ip(-2, 0)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion(screen, 2, 0, ganon, x, y)



	def transformacion2(self, screen, desplazax, desplazay, arrayEnemigos, x, y):
		"""Para cada enemigo (que es un rectangulo), verificamos si ese enemigo colisiono
		con el rectangulo de link, si se ha collsionado y el enemigo esta vivo
		(No se han hecho transformaciones sobre el) entonces link sufre una transformacion
		pero si no hay colision, entonces se pinta a link normal"""	
		angulo = random.randrange(self.START, self.STOP, self.STEP)#Angulo aleatorio
		for enemigo, estado in arrayEnemigos:
			if self.rect.colliderect(enemigo) and estado:
				self.rect.move_ip(desplazax, desplazay)
				self.imagenActual = self.getRotacion(angulo)
				rect = self.imagenActual.get_rect()
				#playAtaque()
				rect.centerx = x
				rect.centery = y
				screen.blit(self.imagenActual, rect)
			else:
				screen.blit(self.imagenActual, self.rect)
				
					
	def moverSencillo(self, keys, screen, arrayEnemigos):
		''' Le permite a link moverse por el tablero'''
		(x, y) = (self.rect.centerx, self.rect.centery)#Coordenada x e y de donde se encutnra el rectangulo d Link
		self.transformacion2(screen, 0, 0, arrayEnemigos, x, y,)
		if self.rect.top >= 50:
			if keys[K_UP]:
				#print "Hola"
				self.rect.move_ip(0, -2) # mueve el rectangulo
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion2(screen, 0, 2, arrayEnemigos, x, y)
		if self.rect.bottom <= 520:
			if keys[K_DOWN]:
				self.rect.move_ip(0, 2)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion2(screen, 0, -2, arrayEnemigos, x, y)
		if self.rect.right <= 500:
			if keys[K_RIGHT]:
				self.rect.move_ip(2, 0)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion2(screen, 0, -2, arrayEnemigos, x, y)
		if self.rect.left >= 125:
			if keys[K_LEFT]:
				self.rect.move_ip(-2, 0)
				(x, y) = (self.rect.centerx, self.rect.centery)
				self.transformacion2(screen, 0, 2, arrayEnemigos, x, y)		





