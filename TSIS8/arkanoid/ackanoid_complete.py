import pygame 
import random
import time
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('lab8/arkanoid/audio/catch.mp3')

# Additional parameters
unbreakable_chance = 0.05  # Chance for a brick to be unbreakable
bonus_chance = 0.2  # Chance for a block to give a bonus
bonus_speed_increase = 2  # Speed increase bonus for the ball

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = [(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), random.random() > unbreakable_chance, random.random() < bonus_chance) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)] 

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

bonus_time = 0.5
is_bonus = False

def bonus_timer(dt,bonus_time,is_bonus): 
    if is_bonus:
        bonus_time -= dt
        if bonus_time <= 0:
            is_bonus = False
            bonus_time = 1
        print(ballSpeed)
    return bonus_time,is_bonus

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    dt = clock.tick(FPS) / 1000

    screen.fill(bg)
    
    # Drawing blocks
    for idx, (block, breakable,bonus) in enumerate(block_list):
        if breakable:
            pygame.draw.rect(screen, color_list[idx], block)
        elif bonus:
            #draw bonus blocks with white border
            pygame.draw.rect(screen, (255, 255, 255), block)
        else:
            pygame.draw.rect(screen, (100, 100, 100), block)  # Unbreakable blocks

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    for idx, (block, breakable,bonus) in enumerate(block_list):
        if ball.colliderect(block):
            if breakable:
                block_list.pop(idx)
                color_list.pop(idx)
                dx, dy = detect_collision(dx, dy, ball, block)
                game_score += 1
                paddle[2] -= 4
                paddleSpeed += 0.25

                collision_sound.play()

                # Bonus
                if bonus:
                    ballSpeed += bonus_speed_increase  # Increase ball speed
                    print(ballSpeed)
                    is_bonus = True

            else:
                dx, dy = detect_collision(dx, dy, ball, block)

    # Bonus timer
    bonus_time,is_bonus = bonus_timer(dt,bonus_time,is_bonus)
    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    pygame.display.flip()
    clock.tick(FPS)


