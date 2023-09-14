"""
Im TEil3 wird unser Programm schnell unübersichtlich.
Wir arbeiten besser mit Objekten. Hier haben wir ein Objekt Sonne.
Eine Sonne hat eine bestimmte Farbe und einen bestimmten Radius.
Und sie hat bestimmte Koordinaten.

Sie zieht unabhängig vom Spielgeschehen ihre Bahnen, sie kann sich also
bewegen.

Und wenn wir eine Sonne rendern wollen, dann zeichnen wir einen Kreis in eben dieser
Farbe mit genau diese Radius an der vorgegebenen Stelle.

Findest du all das wieder in der Klasse Sonne?
Warum packe ich in die Methode rendern die Methode move?

Da die Sonne eigentlich alles selber kann, muss man dem FEnsterAufbauen nur noch sagen,
dass es die Sonne zeichnen(rendern) soll.
Die Sonne weiß selber, wo sie steht, dass sie ein Kreis ist...

Ändere die Methode move und nimm für y eine andere Funktion(einfach probieren)
Erzeuge eine zweite Sonne mit einem anderen Radius und einer anderen Farbe... 

"""

import pygame
from pygame.locals import *
pygame.init()



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



# Jetzt wird hier nur die Sonne übergeben
def FensterAufbauen(sonne):
    FENSTER.blit(SPACE, (0, 0))
    #Sonne
    sonne.render(FENSTER)
    pygame.draw.rect(FENSTER,BLUE,(0,0,100,50))
    
  
    

FENSTER = pygame.display.set_mode((800,600))
sonne = Sonne(YELLOW,0,0,30)
pygame.display.set_caption(TITEL)

running = True
while running:
   
    for event in pygame.event.get():
        
        if event.type == QUIT:
            running = False
            pygame.quit
    FensterAufbauen(sonne)
    pygame.display.update()
    
    














