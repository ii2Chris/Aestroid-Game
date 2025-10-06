# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    aestroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, aestroids)
    AsteroidField.containers = (updateable,)
    Shoot.containers = (updateable, drawable, shoots)

    asteroid_field = AsteroidField()

    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    player = Player(x, y, PLAYER_RADIUS)
    
    running = True
    while running:
        dt = clock.tick() / 1000  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)            # update player

       
        # --- collisions: shots vs asteroids ---
        for asteroid in list(aestroids):
            for shot in list(shoots):
            # If CircleShape already has collision helper:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    break  # asteroid is gone; no need to check more shots

        screen.fill((0, 0, 0))        # clear screen
        for obj in drawable:
            obj.draw(screen)          # draw player 
        pygame.display.flip()         # show everything you drew

    pygame.quit()

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
