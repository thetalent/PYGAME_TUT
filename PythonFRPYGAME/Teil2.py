"""
Dies ist Teil 2 
Jede Spiele-Engine hat eine SPIELESCHLEIFE
Diese Spieleschleife lauert auch auf irgendwelche Ereignisse
Es könnte zum Beispiel eine Taste betätigt werden.
Oder es könnte das Fenster geschlossen werden.

Gib doch einmal in der Spieleschleife alle events aus.
Die Schleife for event in events geht alle events durch.
Dort ist ein print sinnvoll.
Dann lass das Programm laufen und drücke Tasten etc.
===========Wir haben einen weiteren Import eingeführt =============

"""


import pygame
pygame.init()
from pygame.locals import *

FENSTER = pygame.display.set_mode((800,600))


TITEL = "Mein erstes Spiel"
pygame.display.set_caption(TITEL)

# Hier fängt die Spielschleife an
running = True

while running:
    # Was ist denn alles so passiert, seit wir das letze Mal gerendert haben?
    # Wir gehen alle Ereignisse durch und reagieren darauf
    for event in pygame.event.get():
        # Wenn du neugierig bist, schau dir mal an, was so alles passiert
        #print(event)

        # Hier hast du das Fenster geschlossen (Das klappt nicht immer)
        if event.type == QUIT:
            running = False
            pygame.quit
    
    














