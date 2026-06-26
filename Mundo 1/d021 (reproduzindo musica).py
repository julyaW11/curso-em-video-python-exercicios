import pygame 

#inicializando o mixer, tem que iniciar ele primeiro
pygame.mixer.init()

#inicializando o Pygame
pygame.init()

pygame.mixer.music.load('021bl.mp3')
pygame.mixer.music.play()
pygame.event.wait()