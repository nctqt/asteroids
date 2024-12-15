from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, player_rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(player_rotation)
        self.velocity *= PLAYER_SHOOT_SPEED
        #self.position = (x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    