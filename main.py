import pygame
import random
pygame.init()


WIDTH = 1280
HEIGHT = 720
running = True
FPS = 40
VELOCITY = 0
X_POS = 580
BOX_X = random.randint(10, 1270)
BOX_Y = random.randint(10, 30)
VEL_BOX_X = 10
VEL_BOX_Y = 10

GAME_OVER = pygame.image.load('main.jpg')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                VELOCITY = 15
            elif event.key == pygame.K_LEFT:
                VELOCITY = -15
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                VELOCITY = 0
    screen.fill("#212121")
    pygame.draw.circle(screen, "red", (BOX_X, BOX_Y), 10)
    pygame.draw.rect(screen, "white", (X_POS, 700, 120, 20))
    if (BOX_Y>(HEIGHT-32)) and (BOX_X<X_POS-10 or BOX_X>X_POS+130):
        screen.blit(GAME_OVER, [0,0])
    elif BOX_Y>690:
        VEL_BOX_Y=-10
    elif BOX_Y<10:
        VEL_BOX_Y=10
    elif BOX_X>1270:
        VEL_BOX_X=-10
    elif BOX_X<0:
        VEL_BOX_X=10

    elif X_POS>1160:
        VELOCITY=-15
    elif X_POS<0:
        VELOCITY=15
    X_POS += VELOCITY
    BOX_X+=(VEL_BOX_X)
    BOX_Y+=(VEL_BOX_Y)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()