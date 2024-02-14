import time
import random
import pygame

# Inicializa la biblioteca pygame
pygame.init()

# Lista de desastres
desastres = ["Incendio Forestal", "Plaga de langostas", "Chupacabras", "Avalancha", "Terremoto"]

# Genera un número aleatorio de segundos entre 5 y 70 minutos
tiempo_aleatorio = random.randint(5*60, 70*60)

print(f"El temporizador se inicio, esperemos sobrevivir al final del dia")

# Espera el tiempo aleatorio
time.sleep(tiempo_aleatorio)

# Se elije el desastre que ocurrio
pickone = random.randint(0, len(desastres)-1)
pickstr = desastres[pickone]

# Genera una alerta al final del temporizador
print(f"¡Alerta! El temporizador ha terminado. Ocurrio :{pickstr}")

# Reproduce una alarma sonora, archivo mp3 debe estar en la misma carpeta que este script
pygame.mixer.music.load("siren01.mp3")
pygame.mixer.music.play()

# Espera a que termine la alarma
while pygame.mixer.music.get_busy():
    pass
