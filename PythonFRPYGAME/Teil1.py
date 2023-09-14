"""
Python hat eine Spiele-Engine namens Pygame
Die müssen wir erst installieren.
Das geht über pip --user install pygame
Nach dem Installieren müssen wir pygame einbinden.


Ändere die Überschrift und die Größe des Fensters
"""


# Wir holen uns die pygame-Befehle ins Programm und schmeissen die
# Game-Engine an.
import pygame
pygame.init()

# In diesem Fenster findet das Spiel statt 
FENSTER = pygame.display.set_mode((800,600))

# Ein schöner Titel
TITEL = "Mein erstes Spiel"
pygame.display.set_caption(TITEL)


