import pygame
from Player import Player, playerDistance

#1. 초기화
pygame.init()

#2. 게임창 설정
size = [500, 500]
screen = pygame.display.set_mode(size)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
players = [ Player(), Player() ]

players[0].setLocation( 300, 100 )
players[0].setImg("./imgs/yellow.png")

players[1].setKeys( [ pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d ] )
players[1].setLocation( 100, 100 )
players[1].setColor( (255,200,200) )
players[1].setImg("./imgs/red.png")


space = pygame.image.load("./imgs/space.png")

time = 0
font = pygame.font.Font(None, 32)

gaming = True
while gaming: 

    # 4-1. FPS 설정
    clock.tick(60) #1초에 60번으로 실행제한

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.KEYDOWN:
            for p in players:  p.keydown( event.key ) 
           
        elif event.type == pygame.KEYUP:
            for p in players:  p.keyup( event.key ) 

    # 4-3. 입력, 시간에 따른 변화
    for p in players: p.move()

    # 4-4. 그리기
    screen.blit(space, (0,0))
    for p in players: p.draw( screen )

    time = (time+1/60) 
    score = font.render( f"{time:.3f}" , True, (255,255,255))    
    screen.blit(score, (10,10))
 

    

    # 4-5. 업데이트
    pygame.display.flip()

    if playerDistance( players[0], players[1] ) < players[0].size*2:
        gaming = False

# 5. 게임 종료
while( True ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
