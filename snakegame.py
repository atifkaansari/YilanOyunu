import pygame
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")
clock = pygame.time.Clock()

def get_random_position():
    x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    return x, y

def show_menu():
    display.fill(BLACK)
    font = pygame.font.Font(None, 50)
    text = font.render("Yılan Oyunu", True, WHITE)
    text_start = pygame.font.Font(None, 36).render("Başlamak için ENTER'a basın", True, WHITE)
    display.blit(text, (WIDTH // 2 - 100, HEIGHT // 3))
    display.blit(text_start, (WIDTH // 2 - 160, HEIGHT // 2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def game_loop():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    apple = get_random_position()
    score = 0
    
    running = True
    while running:
        display.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)
        
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            display.fill(BLACK)
            font = pygame.font.Font(None, 50)
            text = font.render(f"Oyun Bitti! Skor: {score}", True, WHITE)
            text_restart = pygame.font.Font(None, 36).render("Tekrar oynamak için ENTER'a basın", True, WHITE)
            display.blit(text, (WIDTH // 2 - 150, HEIGHT // 3))
            display.blit(text_restart, (WIDTH // 2 - 200, HEIGHT // 2))
            pygame.display.flip()
            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            waiting = False
                            return game_loop()
        
        snake.insert(0, new_head)
        if new_head == apple:
            apple = get_random_position()
            score += 1
        else:
            snake.pop()
        
        pygame.draw.rect(display, RED, (apple[0], apple[1], GRID_SIZE, GRID_SIZE))
        for segment in snake:
            pygame.draw.rect(display, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        
        font = pygame.font.Font(None, 36)
        text = font.render(f"Skor: {score}", True, WHITE)
        display.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(10 + score)  

show_menu()
game_loop()