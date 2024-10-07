import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1280, 720
running = True
FPS = 40

COLORS = ["white", "white", "white", "white"]
X_POS_BOTTOM, X_POS_TOP = 580, 580
Y_POS_RIGHT, Y_POS_LEFT = 350, 350
VAL = 0

BALL_X, BALL_Y = random.randint(10, 1270), random.randint(10, 30)
BALL_VEL_X, BALL_VEL_Y = 2, 2

CHANCE = ["RIGHT", "TOP", "LEFT", "BOTTOM"]

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

    # Reset colors to white
    COLORS = ["white", "white", "white", "white"]
    
    # Set active paddle color to green
    if CHANCE[-1] == "BOTTOM":
        COLORS[0] = "green"
    elif CHANCE[-1] == "RIGHT":
        COLORS[1] = "green"
    elif CHANCE[-1] == "TOP":
        COLORS[2] = "green"
    elif CHANCE[-1] == "LEFT":
        COLORS[3] = "green"

    screen.fill("#212121")
    pygame.draw.circle(screen, "red", (BALL_X, BALL_Y), 10)
    pygame.draw.rect(screen, COLORS[0], (X_POS_BOTTOM, HEIGHT-20, 120, 20))
    pygame.draw.rect(screen, COLORS[1], (WIDTH-20, Y_POS_RIGHT, 20, 120))
    pygame.draw.rect(screen, COLORS[2], (X_POS_TOP, 0, 120, 20))
    pygame.draw.rect(screen, COLORS[3], (0, Y_POS_LEFT, 20, 120))

    # Ball movement and collision
    if BALL_X >= WIDTH - 20 or BALL_X <= 20:
        BALL_VEL_X *= -1
    if BALL_Y >= HEIGHT - 20 or BALL_Y <= 20:
        BALL_VEL_Y *= -1

    # Paddle movement
    if CHANCE[-1] == "BOTTOM":
        X_POS_BOTTOM = max(0, min(WIDTH - 120, X_POS_BOTTOM + VAL))
    elif CHANCE[-1] == "RIGHT":
        Y_POS_RIGHT = max(0, min(HEIGHT - 120, Y_POS_RIGHT - VAL))
    elif CHANCE[-1] == "TOP":
        X_POS_TOP = max(0, min(WIDTH - 120, X_POS_TOP + VAL))
    elif CHANCE[-1] == "LEFT":
        Y_POS_LEFT = max(0, min(HEIGHT - 120, Y_POS_LEFT - VAL))

    BALL_X += BALL_VEL_X
    BALL_Y += BALL_VEL_Y

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
