# -*- coding: utf-8 -*-

import pygame
from MUSIC import playIntro 

class Bienvenida:
    ''' Esta clase muestra la introduccion del juego '''

    def __init__(self):
        ''' Constructor '''
        playIntro()
        self.pinta = True
        self.pinta_all = True
        self.color = 0
        self.letraGrande = pygame.font.SysFont("Algerian", 50)
        self.letraPeque = pygame.font.SysFont("Algerian", 16)


    def evento(self):
        #Se verifica un evento de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # cuando se desea cerrar la ventana
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE): # Al presionar enter se sale de la presentacion y se pasa al menu
                    self.pinta_all = False


    def pintar(self, screen, x, y):
        ''' Escribe en pantalla '''
        disp = self.letraGrande.render("The Legend Of Zelda", 1, (self.color, self.color, self.color))
        screen.blit(disp, ((x / 2) - disp.get_rect().width / 2, (y / 2) - disp.get_rect().height))
        disp2 = self.letraPeque.render("A Link To The Past", 1, (self.color, self.color, self.color))
        screen.blit(disp2, ((x / 2) + disp2.get_rect().width / 2, (y / 2)))



    def introduccion(self, screen, x, y):
        ''' Maneja el cambio de color en pantalla '''
        reloj = pygame.time.Clock()
        espera = 71

        while self.pinta and self.pinta_all:
            reloj.tick(espera)
            screen.fill((0, 0, 0)) # self.pinta el fondo de negro
            self.pintar(screen, x, y)
            self.color += 1
            if self.color >= 255:
                self.pinta = False

            #Se verifica un evento
            self.evento()
            pygame.display.update()

        self.pinta = True
        self.color = 0

        while self.pinta and self.pinta_all:
            reloj.tick(espera)
            screen.fill((self.color, self.color, self.color))
            self.pintar(screen, x, y)
            self.color += 1
            if self.color >= 255:
                self.pinta = False

            self.evento()
            pygame.display.update()

        self.pinta = True
        self.color = 255

        while self.pinta and self.pinta_all:
            reloj.tick(espera)
            screen.fill((255, 255, 255))
            self.pintar(screen, x, y)
            self.color -= 1
            if self.color <= 75:
                self.pinta = False

            self.evento()
            pygame.display.update()

        self.pinta = True
        self.color = 75

        while self.pinta and self.pinta_all: 
            reloj.tick(espera)
            screen.fill((255, 255, 255))
            self.pintar(screen, x, y)
            self.color += 1
            if self.color >= 255:
                self.pinta = False

            self.evento()
            pygame.display.update()

        self.pinta = True
        self.color = 255

        while self.pinta and self.pinta_all:
            reloj.tick(espera)
            screen.fill((self.color, self.color, self.color))
            self.pintar(screen, x, y)
            self.color -= 1
            if self.color <= 0:
                self.pinta = False

            self.evento()
            pygame.display.update()