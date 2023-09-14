"""
Unser Sprite war eben viel zu gross!!!!!!!
Pygame kann aber ebenso wie Scratch die Groesse eines Sprites ändern
Dazu gibt es die Befehle pygame.transform.

mit
- translate(image,(Breite,Höhe))
-rotate(image,Grad)
-flip(image,False,True)


Ausserdem wollen wir unseren Sprite auch jetzt bewegen können
Dazu fragen wir in der Spieleschleife, ob eine der Tasten WSAD gedrückt worden sind.
... Nein, eigentlich frage wir ab, ob die Tasten WSAD gedrückt SIND!
Darüber gibt und die Spiele-Engine Auskunft.
-- Drehe den Sprite einmal anders und ändere seine Größe.
-- Vielleicht möchtest du, dass height und width vom Sprite variabel sind? oder
durch die Taste g/k verändert werden?
g und k je eine Methode im Sprite aufrufen, die die Seitenlänge des Sprites
verändert.
Was verändert werden soll, muss auch variabel sein


self.__init__ sollte die seitenlänge self.s auf 100 setzen.
Dann soll es eine Methode werdeKleiner(self) geben, die self.s um 1 vermindert
Das gleiche für die Methode werdeGroesser(self).
Und beim rendern müssen wir self.s für die Höhe und Breite einsetzen.
Wenn nun g oder k gedrückt werden, sollten die neuen Methoden aufgerufen werden.

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
        self.vel = 0.1
        self.x = x
        self.y = y
        # Der Sprite ist 100px * 100px gross
        self.image = pygame.transform.scale(image,(100,100))
        # und wird um 90 Grad gedreht
        self.image = pygame.transform.rotate(self.image,90)
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




def FensterAufbauen(sonne,sprite1):
    FENSTER.blit(SPACE, (0, 0))
    sonne.render(FENSTER)
    sprite1.render(FENSTER)
    pygame.draw.rect(FENSTER,BLUE,(0,0,100,50))

    

sprite1 = Sprite(100,HEIGHT//2,SPRITE2BILD)
sonne = Sonne(YELLOW,0,0,30)
pygame.display.set_caption(TITEL)
running = True

while running:
   
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            running = False
            pygame.quit
        # Nur für das eine Mal, wo du die Taste w drückst
        # Das kann man machen, muss man aber nicht.
        if event.type == KEYDOWN:
            if event.key == K_w:
                sprite1.geheHoch()
                
    # Frage ab, welche Tasten gerade gedrückt sind
    # ACHTUNG!!! DAS SIND KEINE EVENTS !!!
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
    FensterAufbauen(sonne,sprite1)
    pygame.display.update()
    
        
            
            
        
        
    
    














