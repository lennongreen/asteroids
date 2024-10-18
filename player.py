from constants import *
from circleshape import *
from shoot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2 )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # go left
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        # go right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # go forward
        if keys[pygame.K_w]:
            self.move(dt)

        # go down
        if keys[pygame.K_s]:
            self.move(dt * -1)

        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer = max(0, self.timer - dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN



