# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    player = Player(x, y, PLAYER_RADIUS)

    running = True
    while running:
        dt = clock.get_time() / 1000  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)             # update player


        screen.fill((0, 0, 0))        # clear screen
        player.draw(screen)           # draw player
        pygame.display.flip()         # show everything you drew
        clock.tick(60)                # limit to 60 FPS

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
