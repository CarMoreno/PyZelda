#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import link
import ganon
import zelda
import time
import random


class Escenario3:
	"""Escenario tres"""

	def __init__(self):
		self.miLink = link.Link()
		self.enemigo = ganon.Ganon()
		self.imagenEscenario3 = pygame.image.load("imagenes/escenario3.jpg").convert()
		self.rect = self.imagenEscenario3.get_rect()
		self.perfil1 = pygame.image.load("imagenes/ganonPerfil.gif")
		self.perfil2 = pygame.image.load("imagenes/linkPerfil.gif")
		self.letra = pygame.font.SysFont("Algerian", 20)
		self.color = (250, 0, 0)
		self.barraVida = pygame.image.load("imagenes/barraVida.png")
		self.turno = True
		self.vidaGanon = self.enemigo.obtenerVida()
		self.vidaLink = self.miLink.obtenerVida()
		self.gana = "Ninguno"


	
	def escribir(self, screen, text, color, x, y):
		''' permite escribir texto en pantalla '''
		texto = self.letra.render(text, True, color, (255, 255, 255))
		screen.blit(texto, (x, y))


	def barra(self, screen, x, y, personaje, nombre, vida):
		''' Actualiza el tamanio de la barra de vida '''
		self.escribir(screen, nombre, self.color, x, y/2)
		if vida > 0:
			width = vida*128/200
			screen.set_clip(Rect(x, y, width, 3)) # Establece el área de recorte actual de la superficie
			screen.blit(self.barraVida, (x, y))
			screen.set_clip(None)


	def ganador(self):
		return self.gana


	def combate(self, screen):
		''' Se realiza la lucha entre link y ganon '''

		ganador = False
		while ganador == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			screen.blit(self.imagenEscenario3, self.rect) 
			screen.blit(self.perfil1, (10, 0))
			screen.blit(self.perfil2, (415, 0))
			screen.blit(self.miLink.obtenerImagen(), self.miLink.obtenerRect())
			self.enemigo.mostrarSprite(screen) # Se muestra a Ganon						
				
			self.barra(screen, 462, 35, self.miLink, "LINK", self.miLink.obtenerVida())
			self.barra(screen, 75, 35, self.enemigo, "GANON", self.enemigo.obtenerVida())
			time.sleep(1)
			if self.turno == True:
				keys = random.randint(0, 2)
				self.escribir(screen, "LINK ataca a GANON", (0,0,0), 180, 450)
				self.miLink.ataques(self.enemigo, keys)
				if keys == 0:
					self.vidaGanon = self.vidaGanon - 20
					self.enemigo.setVida(self.vidaGanon) # se modela el danio a Ganon
				if keys == 1:
					self.vidaGanon = self.vidaGanon - 25
					self.enemigo.setVida(self.vidaGanon)

				if self.enemigo.obtenerVida() <= 0:
					self.gana = "Link"
					ganador = True
				self.turno = False
				
			else:
				keys = random.randint(0, 1)
				self.escribir(screen, "GANON ataca a LINK", (0,0,0), 180, 450)
				self.enemigo.ataques(self.miLink, keys)
				if keys == 0:
					self.vidaLink = self.vidaLink - 10
					self.miLink.setVida(self.vidaLink)	
				if keys == 1:
					self.vidaLink = self.vidaLink - 15
					self.miLink.setVida(self.vidaLink)	

				if self.miLink.obtenerVida() <= 0:
					self.gana = "Ganon"
					ganador = True

				self.turno = True

			pygame.display.update()
			

