import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    coord_x_left_delta = COORD_X-DELTA_STEP
    coord_x_right_delta = COORD_X+DELTA_STEP
    coord_y_up_delta = COORD_Y-DELTA_STEP
    coord_y_down_delta = COORD_Y+DELTA_STEP

    if keys[pygame.K_LEFT] and coord_x_left_delta >= 0:
        COORD_X = coord_x_left_delta
    elif keys[pygame.K_RIGHT] and (coord_x_right_delta + WIDTH_RECTANGLE) <= WIDTH_DISPLAY:
        COORD_X = coord_x_right_delta
    elif keys[pygame.K_UP] and coord_y_up_delta >= 0:
        COORD_Y = coord_y_up_delta
    elif keys[pygame.K_DOWN] and (coord_y_down_delta + HEIGHT_RECTANGLE) <= HEIGHT_DISPLAY:
        COORD_Y = coord_y_down_delta
    elif not (COORD_X >= 0 and COORD_X + WIDTH_RECTANGLE <= WIDTH_DISPLAY) and \
        (COORD_Y >= 0 and COORD_Y + HEIGHT_RECTANGLE <= HEIGHT_DISPLAY):
        continue

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
