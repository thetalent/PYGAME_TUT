"""
Dies ist Teil 3 
Es wird Zeit, das Fenster ein wenig zu füllen.
Damit unser Programm ein wenig organisiert ist, packen wir diese Aufgabe in die
Funktion FensterAufbauen.

Es gibt sehr viele Möglichkeiten, etwas in ein Fenster zu zeichnen.
Wir werden davon 2 verwenden:
==== Images ===========
Wenn wir ein Image in ein Fenster einzeichnen wollen, müssen wir es erst laden.
SPACE = pygame.image.load("Assets/space.png").convert()
lädt das Image space.png aus dem Verzeichnis Assets.
Im Programm heisst das Image jetzt SPACE.
Wenn wir ein Image(Bild) einzeichnen, ist das wie PIP(Picture in Picture) und die
Anweisung heisst FENSTER.blit(image,(Koordinaten von oben links))

==== geometrische Figuren ====
Das ist etwas einfacher - aber eben auch beschränkt.
Eine Sonne könnte zum Beispiel ein gelber Kreis sein
sonne_x = 0
sonne_y = 300
pygame.draw.circle(FENSTER,YELLOW,(sonne_x ,sonne_y),80)
Damit die Funktion weiss, wo sie die Sonne zeichnen soll, werden ihr die Koordinaten
von Sonne mitgegeben. Das wird ja SCHRECKLICH, wenn wir ganz viele Koordinaten
mitgeben müssen!!! Da werden wir nachher was ändern.

Ein Geschoss könnte ein Rechteck sein
Hier zeichnen wir ein Rechteck bei (200,150) ein, das 100px breit und 50px
hoch ist.
pygame.draw.rect(FENSTER,BLUE,(200,150,100,50))


==================
Zeichne noch ein paar geometrische Figuren ein .
Ändere doch einmal in der Spieleschleife die Variable sonne_x.
Zum Beispiel sonne_x = sonne_x + 0.01
Kannst du auch das Rechteck laufen lassen?
Dazu brauchst du im Hauptprgramm zwei neue Variablen r_x und r_y.
Die Funktion FensterAufbauen muss diese übernehmen.
Und dannn wird in pygame.draw.rect(FENSTER,BLUE,(200,150,100,50))
200 und 150 durch r_x und r_y ersetzt.

Koordinaten Rechteck im Hauptprogramm = r_x, r_y
FensterAufbauen soll nun neben sonne_x und sonne_y auch r_x und r_y übernehmen können.
r_x , r_y aus Hauptprogramm an FensterAufbauen
und dann aus FensterAufbauen an pygame.draw.rect








"""

import pygame
pygame.init()
from pygame.locals import *



FENSTER = pygame.display.set_mode((800,600))
TITEL = "Mein erstes Spiel"

# Farben Rot, Gelb, Blau
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
FARBEN = (BLACK,WHITE,RED,YELLOW,BLUE)
RADIEN = (10,20,50,60)

sonne_x = 0
sonne_y = 300

# Spiele leben von der Grafik. Wir holen uns ein paar Bilder und
# stellen sie dem Spiel zur Verfügung
SPACE = pygame.image.load("Assets/space.png")



def FensterAufbauen(sonne_x,sonne_y):
    seitenlänge = 100
    
    #Hintergrund: Ein Bild wird mit der Anweisung blit eingefügt (PIP)
    FENSTER.blit(SPACE, (0, 0))
    
    #Sonne
    pygame.draw.circle(FENSTER,YELLOW,(sonne_x ,sonne_y),80)
    
    # Rect(left, top, width, height) -> Rect
    pygame.draw.rect(FENSTER,BLUE,(200,150,100,50))
    
    
    
pygame.display.set_caption(TITEL)

running = True
while running:
    
    # Events abfragen
    for event in pygame.event.get():
        # Hier hast du das Fenster geschlossen (Das klappt nicht immer)
        if event.type == QUIT:
            running = False
            pygame.quit
    # In der Spieleschleife das Fenster aufbauen
    FensterAufbauen(sonne_x,sonne_y)

    # Wenn das Fenster aufgebaut ist, wird der Bildschirm damit upgedated.
    # Das neue Bild ist also fertig und
    pygame.display.update()
    














