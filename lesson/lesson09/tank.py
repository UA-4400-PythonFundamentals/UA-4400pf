import pygame

import colors
import time
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('Calibri', 10, True, False)
pygame.display.set_caption("My Tank")
FPS = 30
clock = pygame.time.Clock()
font_win = pygame.font.SysFont('Calibri', 50, True, False)

TANK_POS = [100, 300]
projectiles = []


target_pos = [750, 300]
target_radius = 20
target_speed = 20
target_up = True

def dist(point_1, point_2):
    return ((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)**0.5


RUN = True
WIN = False

while RUN:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        # print(event)
        if event.type == pygame.QUIT:  # If user clicked close
            RUN = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.dict.get("key")==1073741906:
                TANK_POS[1] -= 5
            if event.dict.get("key")==1073741903:
                TANK_POS[0] += 5
            if event.dict.get("key")==1073741905:
                TANK_POS[1] += 5
            if event.dict.get("key")==1073741904:
                TANK_POS[0] -= 5
            if event.dict.get("key")==32:
                projectiles.append([TANK_POS[0]+30, TANK_POS[1]+10])




    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    gameDisplay.fill(colors.RGB_WHITE)

    if not WIN:
        # target
        if target_up:
            target_pos[1] -= target_speed
            if target_pos[1] - 2*target_radius < 0:
                target_up = False
        else:
            target_pos[1] += target_speed
            if target_pos[1] + 2*target_radius > 600:
                target_up = True
        pygame.draw.circle(gameDisplay, colors.RGB_RED, target_pos, target_radius)

        # tank
        pygame.draw.rect(gameDisplay, colors.RGB_BLACK,(TANK_POS[0], TANK_POS[1], 20, 20))
        pygame.draw.rect(gameDisplay, colors.RGB_BLACK,(TANK_POS[0]+20, TANK_POS[1]+8, 10, 4))


        # projectile
        for projectile in projectiles:
            projectile[0]+=5
            pygame.draw.circle(gameDisplay, colors.RGB_GREEN, projectile, 3)
            text_pos = font.render(f"{dist(target_pos, projectile):.2f}",True, colors.RGB_NAVY)
            gameDisplay.blit(text_pos, (projectile[0]-20, projectile[1]-10))
            if dist(target_pos, projectile)< 3 + target_radius -1:
                WIN = True
                break
            if projectile[0] > 800:
                print(f"remove{projectile}")
                projectiles.remove(projectile)
                print(projectiles)
    else:
        text = font_win.render(f"WIN!!!",True, colors.RGB_NAVY)
        gameDisplay.blit(text, (350, 100))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(FPS)
