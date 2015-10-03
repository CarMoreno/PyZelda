#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *


class Ganon(pygame.sprite.Sprite):


	def __init__(self):
		''' Constructor '''
		pygame.sprite.Sprite.__init__(self) # constructor de la clase Sprite
		self.ganon = pygame.image.load("imagenes/ganon3.gif").convert()
		self.rect = self.ganon.get_rect() #  obtiene un rectangulo con las dimensiones y posición de la imagen
		self.rect.centerx = 280
		self.rect.centery = 180
		self.vida = 200


	def ataques(self, rival, numero):
		''' Permite a Ganon lanzar dos ataques distintos '''
		imagen = rival.obtenerImagen()
		if numero == 0:			
			nuevaImagen = pygame.transform.laplacian(imagen) # Busca los bordes en una superficie
			nuevaImagen.set_colorkey((0,0,0)) # se usara un color como transparente, en este caso negro
			rival.setImagen(nuevaImagen) # se asigna la nueva imagen
		if numero == 1:
			nuevaImagen = pygame.transform.scale(imagen, (33, 53))
			#nuevaImagen.set_colorkey((255,255,255)) # se usara un color como transparente, en este caso blanco
			rival.setImagen(nuevaImagen)


	def obtenerImagen(self):
		''' Retona la imagen que representa al sprite '''
		return self.ganon


	def setImagen(self, nuevaImagen):
		''' Se asigna la imagen que representa al sprite '''
		self.ganon = nuevaImagen

	
	def obtenerRect(self):
		''' Retorna un rectangulo con las dimensiones de la imagen '''
		return self.rect


	def obtenerVida(self):
		''' Retorna el atributo vida del sprite '''
		return self.vida


	def setVida(self, numero):
		''' Se asigna la vida al sprite '''
		self.vida = numero


	def mostrarSprite(self, screen):
		''' Muestra la imagen que representa al enemigo en pantalla '''
		screen.blit(self.ganon, self.rect)


	def mover(self, keys):
		''' Hace posible que el personaje se mueva en pantalla '''
		if self.rect.top >= 100:
			if keys[K_u]:
				self.rect.move_ip(0, -2) # mueve el rectangulo
		if self.rect.bottom <= 520:
			if keys[K_d]:
				self.rect.move_ip(0, 2)
		if self.rect.right <= 500:
			if keys[K_r]:
				self.rect.move_ip(2, 0)
		if self.rect.left >= 98:
			if keys[K_l]:
				self.rect.move_ip(-2, 0)
