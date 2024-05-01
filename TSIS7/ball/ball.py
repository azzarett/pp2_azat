'''
Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up,
Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of 
pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of 
the screen should be ignored
'''

import pygame

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)


size = weight, hight = 690, 690
screen = pygame.display.set_mode(size) 
pygame.display.set_caption('Red Ball') 
clock = pygame.time.Clock()

color = RED

x, y = 100, 100
dx, dy = 0, 0

done = False

while not done:
    for event in pygame.event.get():

        key = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            done = True

        if key[pygame.K_UP]: 
            dx, dy = 0, -20
            x += dx
            y += dy

            if y < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) 

        if key[pygame.K_DOWN]:
            dx, dy = 0, 20
            x += dx
            y += dy

            if y > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) 

        if key[pygame.K_LEFT]:
            dx, dy = -20, 0
            x += dx
            y += dy

            if x < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50])

        if key[pygame.K_RIGHT]: 

            dx, dy = 20, 0
            x += dx
            y += dy

            if x > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) 

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, color, [x, y, 50,50]) 
    clock.tick(60)
    pygame.display.update()
pygame.quit()