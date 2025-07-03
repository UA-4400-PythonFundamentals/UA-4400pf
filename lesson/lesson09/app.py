import pygame

import colors

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("My Game")
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False)

POINTS = []

RUN = True

while RUN:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        # print(event)
        if event.type == pygame.QUIT:  # If user clicked close
            RUN = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(event)
            # print()
            if event.dict.get("button") == 1:
                POINTS.append(event.dict["pos"])
            elif event.dict.get("button") == 3:
                POINTS.pop()



    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    gameDisplay.fill(colors.RGB_WHITE)

    for point in POINTS:
        pygame.draw.circle(gameDisplay, colors.RGB_GREEN, point, 5)
        text = font.render(f"({point[0]}, {point[1]})",True, colors.RGB_NAVY)
        gameDisplay.blit(text, (point[0]-50, point[1]-30))

    if len(POINTS)>1:
        pygame.draw.polygon(gameDisplay, colors.RGB_BLUE, POINTS, 3)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(FPS)
