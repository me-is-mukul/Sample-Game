import pygame
import random
pygame.init()


WIDTH = 1280
HEIGHT = 720
running = True
FPS = 40

COLOR1 = "white"
COLOR2 = "white"
COLOR3 = "white"
COLOR4 = "white"

X_POS_BOTTOM = 580
X_POS_TOP = 580
Y_POS_RIGHT = 350
Y_POS_LEFT = 350
PLAYER_VAL_RIGHT = 0
PLAYER_VAL_LEFT = 0

BALL_X = random.randint(10, 1270)
BALL_Y = random.randint(10, 30)
BALL_VAL_x = 2
BALL_VAL_Y = 2

VAL = 0

CHANCE = ["RIGHT","TOP","LEFT",   "BOTTOM"]
GAME_OVER = pygame.image.load('main.jpg')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                CHANCE.append(CHANCE.pop(0))
            elif event.key == pygame.K_LEFT:
                VAL = -10
            elif event.key == pygame.K_RIGHT:
                VAL = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                VAL = 0

    if CHANCE[-1]=="BOTTOM":
        COLOR1="green"
        COLOR2="white"
        COLOR3="white"
        COLOR4="white"
    elif CHANCE[-1]=="RIGHT":
        COLOR1="white"
        COLOR2="green"
        COLOR3="white"
        COLOR4="white"
    elif CHANCE[-1]=="TOP":
        COLOR1="white"
        COLOR2="white"
        COLOR3="green"
        COLOR4="white"
    elif CHANCE[-1]=="LEFT":
        COLOR1="white"
        COLOR2="white"
        COLOR3="white"
        COLOR4="green"

    screen.fill("#212121")
    pygame.draw.circle(screen, "red", (BALL_X, BALL_Y), 10)
    pygame.draw.rect(screen, COLOR1, (X_POS_BOTTOM%WIDTH, 700, 120, 20))
    pygame.draw.rect(screen, COLOR2, (WIDTH-20, Y_POS_RIGHT%HEIGHT, 20, 120))
    pygame.draw.rect(screen, COLOR3, (X_POS_TOP%WIDTH, 0, 120, 20))
    pygame.draw.rect(screen, COLOR4, (0, Y_POS_LEFT%HEIGHT, 20, 120))

    if BALL_X > WIDTH-20:
        BALL_VAL_x = -4
    elif BALL_X < 20:
        BALL_VAL_x = 4
    elif BALL_Y > HEIGHT-20:
        BALL_VAL_Y = -4
    elif BALL_Y < 20:
        BALL_VAL_Y = 4

    elif CHANCE[-1]=="BOTTOM":
        X_POS_BOTTOM+=VAL
    elif CHANCE[-1]=="RIGHT":
        Y_POS_RIGHT-=VAL
    elif CHANCE[-1]=="TOP":
        X_POS_TOP+=VAL
    elif CHANCE[-1]=="LEFT":
        Y_POS_LEFT-=VAL


    BALL_X += BALL_VAL_x
    BALL_Y +=BALL_VAL_Y
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()