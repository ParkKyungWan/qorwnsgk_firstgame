import pygame 
import math

class Player:
    def __init__( self ):
        self.x, self.y = 100,100
        self.color = (255,255,255)
        self.size = 10
        self.up, self.down, self.left, self.right = False, False, False, False

        self.keys = [ pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT ]

    def setLocation( self, x, y ):
        self.x = x
        self.y = y
    
    def setKeys( self, keys ):
        self.keys = keys

    def setColor( self, color ):
        self.color = color

    def draw( self, screen ):
        pygame.draw.circle( screen, self.color, (self.x, screen.get_height() - self.y ), self.size )

    def keydown( self, key ):
        if key == self.keys[0]:
            self.up = True
        elif key == self.keys[1]:
            self.down = True
        elif key == self.keys[2]:
            self.left = True
        elif key == self.keys[3]:
            self.right = True

    def keyup( self, key ):
        if key == self.keys[0]:
            self.up = False
        elif key == self.keys[1]:
            self.down = False
        elif key == self.keys[2]:
            self.left = False
        elif key == self.keys[3]:
            self.right = False

    def move( self ):
        if self.up:
            self.y += 1
        if self.down:
            self.y -= 1 
        if self.right:
            self.x += 1 
        if self.left:
           self.x -= 1 

def playerDistance( p1: Player, p2: Player ):
    tmp = ( p1.x - p2.x )*( p1.x - p2.x ) + ( p1.y - p2.y )*( p1.y - p2.y )
    distance = math.sqrt( abs(tmp) )
    return distance
