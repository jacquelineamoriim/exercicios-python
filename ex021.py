#utiliza a biblioteca pygame
import pygame

pygame.init()
pygame.mixer.music.load('ex0021.wav')
pygame.mixer.music.play()
input('Pressione ENTER para parar a música...')