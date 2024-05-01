import pygame
import random

# Initialize pygame
pygame.init()

# Set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
font_small = pygame.font.SysFont("Verdana", 20)
speed = 1
score = 1

# Constants
TIME_LIMIT = pygame.USEREVENT + 1
pygame.time.set_timer(TIME_LIMIT, 6000)
FOOD_TIME_LIMIT = pygame.USEREVENT + 2
pygame.time.set_timer(FOOD_TIME_LIMIT, 5000)  # Фрукт исчезает через 5 секунд

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        global speed, score
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
            speed = 1
            score = 1
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Main function
def main():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    food_timer = 0

    running = True
    while running:
        global speed, score
        screen.fill((0, 0, 0))

        snake.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT
            elif event.type == FOOD_TIME_LIMIT:
                food.randomize_position()
                food_timer = pygame.time.get_ticks()

        # Проверка на столкновение змейки с самой собой
        if len(snake.positions) > 1 and snake.get_head_position() in snake.positions[1:]:
            running = False  # Если змейка столкнулась с самой собой, завершаем игру
        if len(snake.positions) > 1 and snake.get_head_position() in snake.positions[1:]:
                game_over_text = font_small.render("Game Over", True, WHITE)
                screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
                pygame.display.update()
              
        # Проверка времени существования фрукта
        current_time = pygame.time.get_ticks()
        if current_time - food_timer > 6000:  # Если прошло 6 секунд после появления фрукта
            food.randomize_position()
            food_timer = current_time

        # Проверка на столкновение с фруктом
        if snake.get_head_position() == food.position:
            snake.length += random.randint(1, 3)
            score += random.randint(1, 3)
            food.randomize_position()

            # Увеличение скорости после определенного счета
            if score % 4 == 0:
                speed += 15 + 0
                snake.color = random.choice([GREEN, (0, 255, 255), (255, 255, 0)])  # Изменить цвет змейки
                clock.tick(8 + speed)  # Увеличить скорость

        scores = font_small.render(str(score), True, "white")
        screen.blit(scores, (SCREEN_WIDTH - 25, 10))
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        clock.tick(8 + speed)

    pygame.quit()

if __name__ == '__main__':
    main()
