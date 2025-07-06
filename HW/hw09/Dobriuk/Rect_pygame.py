import pygame

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")

    rect = pygame.Rect(0, 0, 50, 50)
    speed = 5
    clock = pygame.time.Clock()
    screen_rect = screen.get_rect()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect.x -= speed
        if  keys[pygame.K_RIGHT]:
            rect.x += speed
        if keys[pygame.K_UP]:
            rect.y -= speed
        if keys[pygame.K_DOWN]:
            rect.y += speed

        rect.clamp_ip(screen_rect)

        screen.fill(( 0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()