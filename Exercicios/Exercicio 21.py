import pygame
import time

# Inicializa o mixer do pygame
pygame.init()

# Carrega o arquivo de música
pygame.mixer.music.load("Exercicios/Desafio 21.mp3")  # Substitua "musica.mp3" pelo caminho do seu arquivo

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
print("Tocando musica... Pressione Ctrl+C para parar.")
try:
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Aguarda 1 segundo
except KeyboardInterrupt:
    print("Música interrompida.")
    pygame.mixer.music.stop()

