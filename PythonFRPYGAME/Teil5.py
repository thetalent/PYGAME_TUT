"""
Jetzt kommen wir zu einem Sprite, und der soll mit WSAD bewegt werden
Der Sprite ist ein Objekt und er wird über ein Image gerendert
Immer wenn eine Taste WSAD gedrückt wird, soll sich der Sprite bewegen.

Welche Attribute hat ein Image-Sprite?
Erstmal hat er ein Kostüm(Bild)
Dann hat er eine Position (Koordinaten x,y)
Wir nehmen noch eine Geschwindigkeit dazu.

Und welche Methoden?
Da wir den Sprite mit der Tastatur in alle vier Richtungen bewegen wollen,
muss er sich auch in alle 4 Richtungen bewegen können.
Und dann muss er auch noch gerendert werden!

Zeige auch noch einen weiteren Sprite an.

"""

import pygame
from pygame.locals import *
pygame.init()

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

SPACE = pygame.image.load("Assets/space.png")
SPRITE1BILD = pygame.image.load("Assets/spaceship_red.png")
SPRITE2BILD = pygame.image.load("Assets/spaceship_yellow.png")

class Sprite():
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.vel = 3
        self.image = image
        
        #self.rect = self.image.get_rect(topleft = (self.x,self.y)
    def geheLinks(self):
        if self.x > 0:
            selx.x-= vel
    def geheRechts(self):
        if self.x < WIDTH:
            self.x += vel
    def geheHoch(self):
        if self.y > 0:
            self.y -=vel
    def geheRunter(self):
            if self.y < HEIGHT:
                self.y += vel
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
        self.x += 0.1
        self.y = (self.x-400)**2*0.001
        if self.x > 800:
            self.x = 0
    def render(self,Fenster):
        self.move()
        pygame.draw.circle(Fenster,self.color,(self.x,self.y),self.radius)




def FensterAufbauen(sonne,sprite1):
    FENSTER.blit(SPACE, (0, 0))
    
    #Sonne
    sonne.render(FENSTER)

    #SPRITE1
    sprite1.render(FENSTER)
    
    # Rect(left, top, width, height) -> Rect
    pygame.draw.rect(FENSTER,BLUE,(0,0,100,50))

    
    
sprite1 = Sprite(10,HEIGHT//2,SPRITE2BILD)
sonne = Sonne(YELLOW,0,0,30)
pygame.display.set_caption(TITEL)
running = True

while running:   
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit
    FensterAufbauen(sonne,sprite1)
    pygame.display.update()
    
    














