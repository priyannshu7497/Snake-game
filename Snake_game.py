import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Set colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set game variables
snake = [(200, 200), (210, 200), (220, 200)]
food = (random.randint(0, (WIDTH-CELL_SIZE)//CELL_SIZE)*CELL_SIZE, 
        random.randint(0, (HEIGHT-CELL_SIZE)//CELL_SIZE)*CELL_SIZE)
direction = (CELL_SIZE, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
                
    snake.insert(0, (snake[0][0] + direction[0], snake[0][1] + direction[1]))
    if snake[0] == food:
        food = (random.randint(0, (WIDTH-CELL_SIZE)//CELL_SIZE)*CELL_SIZE, 
                random.randint(0, (HEIGHT-CELL_SIZE)//CELL_SIZE)*CELL_SIZE)
    else:
        snake.pop()
        
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or 
        snake[0][1] < 0 or snake[0][1] >= HEIGHT or 
        snake[0] in snake[1:]):
        running = False
        
    pygame.draw.rect(screen, GREEN, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    for part in snake:
        pygame.draw.rect(screen, RED, (part[0], part[1], CELL_SIZE, CELL_SIZE))
        
    pygame.display.update()
    clock.tick(10)

# Quit pygame
pygame.quit()
