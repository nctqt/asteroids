# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    delta_ms = 0

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, 0)

        for item in updateable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player):
                print("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        delta_ms = clock.tick(60)
        dt = delta_ms / 1000

if __name__ == "__main__":
    main()