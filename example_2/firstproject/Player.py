import pygame 

class Player:
    def __init__( self ):
        self.x, self.y = 100,100
        self.color = (255,255,255)
        self.size = 10
        self.up, self.down, self.left, self.right = False, False, False, False

    def draw( self, screen ):
        pygame.draw.circle( screen, self.color, (self.x, screen.get_height() - self.y ), self.size )

    def keydown( self, key ):
        if key == pygame.K_UP:
            self.up = True
        elif key == pygame.K_DOWN:
            self.down = True
        elif key == pygame.K_LEFT:
            self.left = True
        elif key == pygame.K_RIGHT:
            self.right = True

    def keyup( self, key ):
        if key == pygame.K_UP:
            self.up = False
        elif key == pygame.K_DOWN:
            self.down = False
        elif key == pygame.K_LEFT:
            self.left = False
        elif key == pygame.K_RIGHT:
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
