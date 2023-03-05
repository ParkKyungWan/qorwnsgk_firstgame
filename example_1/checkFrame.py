import pygame;

#1. 초기화
pygame.init()

#2. 게임창 설정

size = [300, 400]
screen = pygame.display.set_mode(size)

# 3. 게임 내 필요한 설정

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

frame = 0
windowColor = black

# 4. 메인 이벤트
gaming = True
while gaming: 
    # 4-1. FPS 설정
    clock.tick(60) #1초에 60번으로 실행제한

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False

    # 4-3. 입력, 시간에 따른 변화

    frame += 1
    if frame%2:
        windowColor = white
    else:
        windowColor = black



    # 4-4. 그리기
    screen.fill( windowColor )
    

    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료
pygame.quit()