import pygame
import random

# Pygame Setup
pygame.init() 
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

class Dot:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, "white", self.pos, self.radius)

# List to store the dots
dots = [Dot() for _ in range(10)]

while running:
  #Poll for events
  # Pygame.Quit means user clicked x to quit the game 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  #Fill the screen with a color to wipe anything from last frame
  screen.fill("Black")
  
  pygame.draw.circle(screen, "red", player_pos, 40)
  
  # Draw the dots
  for dot in dots:
      dot.draw()

  # Check for collision with dots
  for dot in dots[:]:
      if player_pos.distance_to(dot.pos) < player_radius + dot.radius:
          player_radius += 1  # Increase the radius of the player circle
          dots.remove(dot)  # Remove the dot from the list
          dots.append(Dot())  # Add a new dot
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_pos.y -= 300 * dt
  if keys[pygame.K_s]:
    player_pos.y += 300 * dt
  if keys[pygame.K_a]:
    player_pos.x -= 300 * dt
  if keys[pygame.K_d]:
    player_pos.x += 300 * dt
    
  # flip() the display to put your work on the screen
  pygame.display.flip()
  
  # limit fps to 60
  # dt is delta time in seconds since last frame
  # used for framerate independet physics 
  dt = clock.tick(60) / 1000
  
pygame.quit()
