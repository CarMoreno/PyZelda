#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import link
import ganon
import escenario3
import sys

class Escenario2:
	"""Esta clase permite la creacion del escenario dos"""

	def __init__(self):
		''' Constructor '''
		self.imagen = pygame.image.load("imagenes/escenario2.png").convert()
		self.antorcha = pygame.image.load("imagenes/laantorcha.gif").convert()
		self.win = pygame.image.load("imagenes/creditos.jpg").convert()
		#self.antorchaRect = self.antorcha.get_rect()
		self.miLink = link.Link()
		self.enemigo = ganon.Ganon()
		self.rect = self.imagen.get_rect()
		self.escena3 = escenario3.Escenario3()


	def imprimir(self, screen, x, y, angulo):
		''' Permite rotar la superficie que representa una antorcha y la muestra en pantalla '''
		rotar = pygame.transform.rotate(self.antorcha, angulo) # Se realiza una rotacion de la superficie
		rect = rotar.get_rect()
		screen.blit(rotar, (x, y), rect)


	def mouseInput(self, screen, cx, cy):
		''' Se confirma si hay un evento de mouse '''
		for event in pygame.event.get(): # Lista de eventos
			if event.type == MOUSEBUTTONDOWN: # Si se presiona un boton del mouse
				( mouse_x, mouse_y ) = pygame.mouse.get_pos() # Obtiene la posicion del mouse
				pos = self.enemigo.obtenerRect()
				if pygame.mouse.get_pressed() == (1, 0, 0) and pos.collidepoint ( mouse_x, mouse_y ): 
					# Se verifica que se halla hecho click izquierdo y si el mouse esta sobre el enemigo
					self.cargarEscena3(screen, cx, cy) # Se carga el tercer escenario


	def cargarEscena3(self, screen, coorx, coory):
		''' Se dibuja el escenario 3 sobre la ventana '''
		miescena = self.escena3.combate(screen)


	def run2(self, screen, coord_x, coord_y):
		juego_activo = False #variable de control del juego
		while not juego_activo:
			keys = pygame.key.get_pressed() # Tecla presionada
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#pygame.quit()
					sys.exit(0)
			screen.blit(self.imagen, (0,0), self.rect) # se pinta la imagen de fondo
			self.escena3.escribir(screen, 'GANADOR '+str(self.escena3.ganador()), (255, 0,0), 0, 0)
			self.imprimir(screen, 100, 100, -30)
			self.imprimir(screen, 100, 490, -30)
			self.imprimir(screen, 470, 100, 10)
			self.imprimir(screen, 470, 490, 10)
			self.enemigo.mostrarSprite(screen) # Se muestra a Ganon
			self.miLink.moverColisionGanon(keys, self.enemigo, screen)
			self.mouseInput(screen, coord_x, coord_y)			
			pygame.display.update()	

