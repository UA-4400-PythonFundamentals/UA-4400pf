import pygame
from dataclasses import dataclass
from typing import Tuple

FPS = 60
SCREEN_SIZE = (500, 500)
RECT_SIZE = (40, 60)
STEP = 5

COLOR_BG   = (0,   0,   0)
COLOR_RECT = (250, 0,   0)
COLOR_TEXT = (255, 255, 255)


def clamp(value: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(value, max_value))


def handle_input(x: int, y: int) -> Tuple[int, int]:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= STEP
    if keys[pygame.K_RIGHT]:
        x += STEP
    if keys[pygame.K_UP]:
        y -= STEP
    if keys[pygame.K_DOWN]:
        y += STEP
    return x, y


@dataclass
class GameState:
    rect_x: int
    rect_y: int
    screen_w: int
    screen_h: int


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("My First Game")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 24)

    state = GameState(
        rect_x=50,
        rect_y=50,
        screen_w=SCREEN_SIZE[0],
        screen_h=SCREEN_SIZE[1]
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                state.screen_w, state.screen_h = event.w, event.h
                screen = pygame.display.set_mode(
                    (state.screen_w, state.screen_h),
                    pygame.RESIZABLE
                )

        new_x, new_y = handle_input(state.rect_x, state.rect_y)

        state.rect_x = clamp(new_x, 0, state.screen_w  - RECT_SIZE[0])
        state.rect_y = clamp(new_y, 0, state.screen_h  - RECT_SIZE[1])

        screen.fill(COLOR_BG)

        pygame.draw.rect(
            screen,
            COLOR_RECT,
            (state.rect_x, state.rect_y, *RECT_SIZE)
        )

        coord_text = f"Position: ({state.rect_x}, {state.rect_y})"
        text_surf = font.render(coord_text, True, COLOR_TEXT)
        screen.blit(text_surf, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()