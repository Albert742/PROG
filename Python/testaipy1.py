import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

# Colors
WHITE = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self):
        self.radius = 30
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.speed_x = random.choice([-5, 5]) * 3
        self.speed_y = random.choice([-5, 5]) * 3

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the walls
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.speed_y = -self.speed_y

# Create balls
balls = [Ball() for _ in range(10)]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update balls
    for ball in balls:
        ball.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw balls
    for ball in balls:
        ball.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()