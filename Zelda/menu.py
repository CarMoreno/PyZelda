# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import opcion
import cursor
#import scene_one
from MUSIC import playMenu

class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        """Inicializa el menu de opciones"""
        playMenu()
        # musica_inicial = pygame.mixer.music.load("melodias/melodia1.mp3")#cargamos la melodia inicial
        # pygame.mixer.music.play(-1)#La ponemos a reproducir infinitamente
        self.opciones = []#Una arreglo donde se guardaran las opciones cada opciones una tupla ("Nombre_opcion", funcion_asociada)
        fuente = pygame.font.SysFont( "Algerian" , 20, italic = True, bold = True)#Fuente para la tipografia del menu
        x = 20# coord x del menu 
        y = 420# coord y del menu
        paridad = 1 
        self.cursor = cursor.Cursor(x , y, 30)#Creamos un objeto cursor, dandole su coordenada x e y, ademas de un dy, que sera la separacion del cursor de las opciones
        #self.escena_uno = scene_one.SceneOne()
        for titulo, funcion in opciones:
            self.opcion = opcion.Opcion(fuente, titulo, x, y, paridad, funcion)
            self.opciones.append(self.opcion)
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        k = pygame.key.get_pressed()#Me retorna la tecla presionada

        if not self.mantiene_pulsado:
            if k[K_UP]:#Si se presiona la telca de nagecacion de arriba
                self.seleccionado -= 1
            elif k[K_DOWN]:#Si se presiona la telca de navegacio abajo
                self.seleccionado += 1
            elif k[K_RETURN]:#Si se presiona enter
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()
        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica que el usuario mantiene pulsada las teclas de arriba, abajo y enter.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]
        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""
        self.cursor.imprimir(screen)
        for opcion in self.opciones:
            opcion.imprimir(screen)



