"""
Wie erkennen wir Treffer?
Lass dieses Programm einmal so laufen.
Die Engine erkennt, ob sich Rechtecke überlappen.
Dazu muss jedes Object ein passendes Rechteck als Attribut haben.
Wie bekommen wir das passende Rechteck?
Das wird zum Glück beim Zeichnen ermittelt und an uns zurückgegeben.
Nur am Anfang in __init__ müssen wir ein Rechteck "erfinden".

In diese Programm werden die Rechtecke auch gezeichnet.
Finde die Stellen in jeder Klasse und kommentiere sie aus.
Danach sollte alles wieder "richtig ausssehe".
In der Spieleschleife schauen wir, ob die Sonne von einem Geschoss getroffen wird.
Wir geben dann das Wort "Treffer" in der Konsole aus.
Was willst du tun, wenn es einen Treffer gibt?

Dann habe ich noch die Spieleuhr eingefügt.
Sie sagt, wieviele Bildwechsel es pro Sekunde geben soll.
Ich habe 60 eingestellt. Experimientiere gerne

"""

import pygame
import time
from pygame.locals import *
pygame.init()


# Den brauchen wir, um von einer Liste ein Element auszusuchen
from random import choice

WIDTH = 800
HEIGHT = 600
FENSTER = pygame.display.set_mode((WIDTH,HEIGHT))
TITEL = "Mein erstes Spiel"

# Farben Rot, Gelb, Blau
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
FARBEN = (BLACK,WHITE,RED,YELLOW,BLUE)
RADIEN = (10,20,50,60)



# Spiele leben von der Grafik. Wir holen uns ein paar Bilder und
# stellen sie dem Spiel zur Verfügung
SPACE = pygame.image.load("Assets/space.png").convert()
SPRITE1BILD = pygame.image.load("Assets/spaceship_red.png").convert()
SPRITE2BILD = pygame.image.load("Assets/spaceship_yellow.png")


class Geschoss():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 4
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def move(self):
        self.x += 7
    def render(self):
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(FENSTER,YELLOW,self.rect)
    
    
class Sprite():
    
    def __init__(self,x,y,image):
        self.vel = 3
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.image = pygame.transform.rotate(pygame.transform.scale(image,(self.width, self.height)),90)
        self.rect = pygame.Rect(0,0,0,0)
    def geheLinks(self):
        if self.x > 0:
            self.x-= self.vel
    def geheRechts(self):
        if self.x < WIDTH:
            self.x += self.vel
    def geheHoch(self):
        if self.y > 0:
            self.y -= self.vel
    def geheRunter(self):
            if self.y < HEIGHT:
                self.y += self.vel
    def render(self,Fenster):
        self.rect = Fenster.blit(self.image,(self.x,self.y))
        pygame.draw.rect(FENSTER,WHITE,self.rect)


        
class Sonne():
    def __init__(self,color,x,y,radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.rect = pygame.Rect(self.x,self.y,self.radius,self.radius)
    def move(self):
        self.x += 0.5
        self.y = (self.x-400)**2*0.001
        if self.x > 800:
            self.x = 0
    def render(self,Fenster):
        self.move()
        self.rect = pygame.draw.circle(Fenster,self.color,(self.x,self.y),self.radius)
        pygame.draw.rect(FENSTER,WHITE,self.rect)


    

def FensterAufbauen(sonne,sprite1, geschosse):
    
    sonne.render(FENSTER)
    sprite1.render(FENSTER)
    # Geschosse
    fertigeGeschosse = []
    for g in geschosse:
        g.move()
        # An dieser Stelle prüfen wir die Kollision
        # zwischen Geschossen und der Sonne
        if pygame.sprite.collide_rect(g,sonne):
            print("Treffer")
            fertigeGeschosse.append(g)
            continue
        if g.x > 800:
            fertigeGeschosse.append(g)
            continue
        g.render()
    for g in fertigeGeschosse:
        geschosse.remove(g)
    
    
    

sonne = Sonne(YELLOW,0,0,30)
geschosse = []
sprite1 = Sprite(100,HEIGHT//2,SPRITE2BILD)

"""
ICh füge eine Spieleuhr hinzu, umd die FramesPerSeconds
zu steuern,
"""
clock = pygame.time.Clock()  
pygame.display.set_caption(TITEL)
running = True
while running:
    FENSTER.blit(SPACE, (0, 0))
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            running = False
            pygame.quit
        # Nur für das eine Mal, wo du die Taste w drückst
        if event.type == KEYDOWN:
            if event.key == K_w:
                sprite1.geheHoch()
            # Wenn Strg
            if event.key ==K_LCTRL:
                geschoss = Geschoss(sprite1.x+sprite1.height//2,sprite1.y+sprite1.height//2)
                geschosse.append(geschoss)
    # Frage ab, welche Tasten gerade gedrückt sin
    keys_pressed = pygame.key.get_pressed()
    # Wenn w,s,a,d
    if keys_pressed[K_w]:
        sprite1.geheHoch()
    if keys_pressed[K_s]:
        sprite1.geheRunter()
    if keys_pressed[K_a]:
        sprite1.geheLinks()
    if keys_pressed[K_d]:
        sprite1.geheRechts()
    
    
    FensterAufbauen(sonne,sprite1, geschosse)
    pygame.display.update()
    
    #Hier setze ich die FPS auf 60.
    # Zwischen 30 und 60 ist ein guter Wert.
    # Ist er zu niedrig, ruckelt es
    # Ist er zu hoch, wird das neue Bild evtl. geschickt,
    # noch bevor es fertig aufgebaut ist.
    
    clock.tick(60)
    
            
            




