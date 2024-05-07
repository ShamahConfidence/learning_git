# import pywhatkit

# command = input("Enter your song: ",)
# pywhatkit.playonyt(command)

import pygame

pygame.init()

# Create a window
window = pygame.display.set_mode((350,200))

# Load a music file
pygame.mixer.music.load('C:\\Users\\LENOVO\\Desktop\\Gospel\\Bethel_Revival_Choir_-_Power_Medley_Nukunu_Mawu__CeeNaija.com_.mp3')

# Play the music 
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()