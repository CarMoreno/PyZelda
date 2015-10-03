# -*- coding: utf-8 -*-
"""Integrantes:
Viviana Andrea Zuluaga
Daniela Roldan Quiroga
Carlos Andres Moreno
--------The Legend Of Zelda: A Link To The Past
"""
import pygame
import time
import menu
import scene_one
import bienvenida
from MUSIC import playSegundaria
from pygame.locals import *

"""Aca se maneja el loop inicial del juego, en este script se define quien tomara el control
del juego en un momento determinado, para ello se hace uso de distintas funciones de acuerdo
a la eleccion tomado en el menu, las funciones tendran que llamar a distintas clases para su 
correcto funcionamiento"""

#---------Configuraciones iniciales-------------

pygame.init()#Inicalizamos todos los modulos
display_width, display_height = 600,600
screen = pygame.display.set_mode((display_width, display_height))#Desplegamos el screen
pygame.display.set_caption("The Legend Of Zelda")#Nombre de la ventana
clock = pygame.time.Clock() #Reloj
teclado=pygame.key.get_pressed()

#---------Objetos necesarios--------------------
#Distintas escenas que el juego podra tomar en un momento dado
escena_uno =  scene_one.SceneOne()
intro = bienvenida.Bienvenida()
time.sleep(0.5)
intro.introduccion(screen, display_width, display_height)
 

def run():
    """Loop inicial del juego, corre el menu, quien decide a quien le cedera el control del juego"""
    menu_activo = False
    opciones = [#Opciones del juego, un arreglo que contiene tuplas ("Nombre_opcion", funcion_asociada)
        ("Jugar", comenzar_nuevo_juego),#Escena uno, donde Link se enfrenta con los minijefes
        (u"¿Como Jugar?", como_jugar),#La u al principio es para indicar a pygame el caracter unicode de las tildes y signo de pregunta. Se muestra una escena donde se dira al usuario, como jugar
        ("Creditos", creditos),
        ("Salir", salir_del_programa)#Opcion para salir del programa
        ]
    fondo = pygame.image.load("imagenes/imgInicio.png").convert()
    miMenu = menu.Menu(opciones)
    while not menu_activo:
        for e in pygame.event.get():
            if e.type == QUIT:
                # pygame.quit()
                # quit()
                import sys
                sys.exit(0)
        screen.blit(fondo, (0, 0))#Establecemos el fondo
        miMenu.actualizar()#eventos para el menu
        miMenu.imprimir(screen)#mostramos las opciones del menú
        pygame.display.update()#actualizamos !!!IMPORTANTE PARA QUE SE MUESTRE CORRECTAMENTE
        clock.tick(50)#Transicion de frames por segundo, da un efeco de transcion al menu
        #comenzar_nuevo_juego() #Funcion que comienza un nuevo juego   


def como_jugar():
    """Esta funcion se activa cuando se da enter en la opcion de: como jugar"""
    playSegundaria()
    img_comoJugar = pygame.image.load("imagenes/comoJugar.jpg")
    screen.blit(img_comoJugar, (0,0))
    pygame.display.update()
    time.sleep(10)
    run()

def creditos():
    """Esta funcion se activa cuando se da enter en la opcion creditos"""
    playSegundaria()
    img_creditos = pygame.image.load("imagenes/creditos.jpg")
    screen.blit(img_creditos, (0,0))
    pygame.display.update()
    time.sleep(8)
    run()


def comenzar_nuevo_juego():
    """Esta fucnion se activa cuando se da enter en la opcion jugar, desde aca se maneja
    la primera escena del juego, ayudado obviamente, por distintas clases"""
    escena_uno.cargarEscena1(screen, display_width, display_height)#Se pone a correr la escena
    #escena_uno.cargarEscena2(screen, display_width, display_height)

def salir_del_programa():
    """Esta fucion se ejecuta cuando se da enter en la opcion salir"""
    import sys
    sys.exit(0)

 
