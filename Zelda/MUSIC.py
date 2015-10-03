import pygame
pygame.mixer.init()
"""Script para gestionar las melodias que tendran lugar en el juego"""
# ataqueLink = pygame.mixer.Sound("melodias/ataque.mp3")
def playIntro():
	intro = pygame.mixer.music.load("melodias/title.mp3")
	pygame.mixer.music.play(-1)

def playMenu():
	menu = pygame.mixer.music.load("melodias/melodia1.mp3")
	pygame.mixer.music.play(-1)	

def playPrincipal():
	principal = pygame.mixer.music.load("melodias/castilloHyrule.mp3")
	pygame.mixer.music.play(-1)	

def playSegundaria():
	segundaria = pygame.mixer.music.load("melodias/creditos.mp3")
	pygame.mixer.music.play(-1)


