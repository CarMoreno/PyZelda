# -*- coding: utf-8 -*-
import pygame
class Cursor:
    """Clase que se encarga de la gestion del cursor de seleccion del menu"""
    def __init__(self, x, y, dy):#Constructor de la clase, se inicializan los atributos basicos
        self.image = pygame.image.load("imagenes/cursor.png").convert_alpha()#Cargamos la imagen
        self.rect = self.image.get_rect()#Manejamos la imagen como un rectangulo
        self.rect.x = x#Coordenada x del rectangulo (cursor)
        self.y_inicial = y#Coordenada y inicial del rectangulo (cursor)
        self.dy = dy#Separacion entre el rectangulo (cursor) y las opciones del menu
        self.y = 0#Coordenada y del rectangulo (cursor), esta coordeanda se ira actualizando cuando lo movamos con las teclas de navegacion
        self.seleccionar(0)

    def actualizar(self):
        """Acutaliza la coordenanada y del cursor, 
        se usa cuando movemos el cursor con las telcas de navegacion"""
        self.y += (self.to_y - self.y) / 5.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        """Imprimer la imagen del cursor"""
        screen.blit(self.image, self.rect)