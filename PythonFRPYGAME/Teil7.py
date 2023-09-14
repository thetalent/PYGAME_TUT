"""
Jetzt soll der Sprite schießen können.
Dazu nutzen wir die Taste Strg.
Die Geschosse sind wieder Objekte
Sie bewegen sich nur in der Horizontalen

Also: Neues Objekt Geschoss
Und auf die Taste Strg wird ein neues Geschoss erzeugt
Das Geschoss muss wieder gerendert werden, das machen wir wieder in der Funktion
FEnsterAufbauen.

Das Problem ist nur: Wann haben wir ein Geschoss und wann nicht?
Und wir können ja auch mehrere Geschosse haben.
Wir erstellen eine Liste aller Geschosse und übergeben sie an Fenster_aufbauen
WEnn sie leer ist, passiert gar nichts, ansonsten bewegen sich alle Geschosse in der Liste



"""

import pygame
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

SPACE = pygame.image.load("Assets/space.png").convert()
SPRITE1BILD = pygame.image.load("Assets/spaceship_red.png")
SPRITE2BILD = pygame.image.load("Assets/spaceship_yellow.png")


class Geschoss():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 4
    def move(self):
        self.x += 0.1
    def render(self):
        self.move()
        pygame.draw.rect(FENSTER,YELLOW,(self.x,self.y,self.width,self.height))
    
    





class Sprite():
    
    def __init__(self,x,y,image):
        self.vel = 0.05
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.image = pygame.transform.rotate(pygame.transform.scale(image,(self.width, self.height)),90)
      
        #self.rect = self.image.get_rect(topleft = (self.x,self.y)
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
        Fenster.blit(self.image,(self.x,self.y))
        #pygame.draw.rect(FENSTER,WHITE,self.rect)


            






class Sonne():
    def __init__(self,color,x,y,radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def move(self):
        self.x += 0.01
        self.y = (self.x-400)**2*0.001
        if self.x > 800:
            self.x = 0
    def render(self,Fenster):
        self.move()
        pygame.draw.circle(Fenster,self.color,(self.x,self.y),self.radius)

sonne = Sonne(YELLOW,0,0,30)
geschosse = []
sprite1 = Sprite(100,HEIGHT//2,SPRITE2BILD)
    

def FensterAufbauen(sonne,sprite1, geschosse):
    
    FENSTER.blit(SPACE, (0, 0))
    
    sonne.render(FENSTER)

    sprite1.render(FENSTER)
    
    #pygame.draw.rect(FENSTER,BLUE,(0,0,100,50))

    # Geschosse
    for g in geschosse:
        g.move()
        if g.x > 800:
            geschosse.remove(g)
            break
        g.render()
    
    


pygame.display.set_caption(TITEL)
running = True
while running:
   
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
            if event.key == K_LCTRL:
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

       
            





