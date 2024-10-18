from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        print("split")
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y , new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = vel1
        a2.velocity = vel2

        self.kill()

        

