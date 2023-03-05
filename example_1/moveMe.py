import pygame;

#1. 초기화
pygame.init()

#2. 게임창 설정

size = [300, 400]
screen = pygame.display.set_mode(size)

# 3. 게임 내 필요한 설정

clock = pygame.time.Clock()


frame = 0
black = (0,0,0)
white = (255,255,255)

coordinate = {
    'x': 100,
    'y': 100
}

up, down, right, left = False, False, False, False

# 4. 메인 이벤트
gaming = True
while gaming: 
    # 4-1. FPS 설정
    clock.tick(60) #1초에 60번으로 실행제한

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            elif event.key == pygame.K_DOWN:
                down = True
            elif event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_DOWN:
                down = False
            elif event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_RIGHT:
                right = False

    # 4-3. 입력, 시간에 따른 변화
    if up:
        coordinate['y'] += 1 
    if down:
        coordinate['y'] -= 1 
    if right:
        coordinate['x'] += 1 
    if left:
        coordinate['x'] -= 1 

    # 4-4. 그리기
    screen.fill(black)
    pygame.draw.circle( screen, white, (coordinate['x'],screen.get_height()-coordinate['y']), 10 )
    

    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료
pygame.quit()