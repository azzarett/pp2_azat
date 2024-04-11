import pygame
import math

def draw_parallelogram(screen, color, rect, depth):
    points = [rect.topleft, rect.topright, (rect.topright[0] + depth, rect.topright[1] - depth), (rect.topleft[0] + depth, rect.topleft[1] - depth)]
    pygame.draw.polygon(screen, color, points)  # Draw the parallelogram

def draw_right_triangle(screen, color, rect):
    points = [rect.topleft, rect.bottomleft, rect.topright]
    pygame.draw.polygon(screen, color, points)  # Draw the right triangle

def draw_equilateral_triangle(screen, color, rect):
    points = [rect.topleft, rect.topright, (rect.centerx, rect.bottom)]
    pygame.draw.polygon(screen, color, points)  # Draw the equilateral triangle

def draw_rhombus(screen, color, rect):
    points = [rect.midtop, rect.midright, rect.midbottom, rect.midleft]
    pygame.draw.polygon(screen, color, points)  # Draw the rhombus



def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    rectangles = []  # List to store rectangles
    circles = []  # List to store circles
    squares = []
    right_triangles = []
    equilateral_triangles = []
    rhombuses = []
    tool = 'rectangle'  # Initialize tool to 'rectangle'
    color = (255, 255, 255)  # Current color
    start = None  # Initialize start
    current = None  # Initialize current

    DRAWING_AREA = pygame.Rect(50, 50, screen.get_width() - 70, screen.get_height() - 50)

    tools = ['rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']  # List of tools

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 165, 0)]  # List of colors

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    tool = 'rectangle'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_t:
                    tool = 'right_triangle'
                elif event.key == pygame.K_q:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_b:
                    tool = 'rhombus'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Check if a tool was clicked
                    for i, t in enumerate(tools):
                        if pygame.Rect(i * 50, 0, 50, 50).collidepoint(event.pos):
                            tool = t
                            break
                    else:
                        if DRAWING_AREA.collidepoint(event.pos):  # Check if the click is within the drawing area
                            start = event.pos
            if event.type == pygame.MOUSEMOTION:
                if start is not None:
                    current = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for i, col in enumerate(colors):
                        if pygame.Rect(screen.get_width() - 20, i * 20, 20, 20).collidepoint(event.pos):
                            color = col
                            break
                    if start is not None and DRAWING_AREA.collidepoint(event.pos):  # Check if the release is within the drawing area
                        end = event.pos
                        if tool == 'rectangle':
                            rectangles.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'circle':
                            radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
                            circles.append((start, radius, color))
                        elif tool == 'square':
                            squares.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'right_triangle':
                            right_triangles.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'equilateral_triangle':
                            equilateral_triangles.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'rhombus':
                            rhombuses.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'eraser':
                            rectangles = [(rect, rect_color) for rect, rect_color in rectangles if not rect.collidepoint(end)]
                            circles = [(center, radius, circle_color) for center, radius, circle_color in circles if ((end[0]-center[0])**2 + (end[1]-center[1])**2)**0.5 > radius]
                        start = None
                        current = None

        screen.fill((0, 0, 0))

        for i, t in enumerate(tools):
            rect = pygame.Rect(i * 50, 0, 50, 50)
            if t == tool:
                pygame.draw.rect(screen, (255, 255, 255), rect)  # Fill the selected tool with white
            if t == 'rectangle':
                pygame.draw.rect(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 10, 10, 30, 30), 2)
            elif t == 'circle':
                pygame.draw.circle(screen, (0, 0, 0) if t == tool else (255, 255, 255), (i * 50 + 25, 25), 15, 2)
            elif t == 'eraser':
                draw_parallelogram(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 5, 30, 30, 30), 10)
            elif t == 'square':
                pygame.draw.rect(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 10, 10, 30, 30), 2)
            elif t == 'right_triangle':
                draw_right_triangle(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 10, 10, 30, 30))
            elif t == 'equilateral_triangle':
                draw_equilateral_triangle(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 10, 10, 30, 30))
            elif t == 'rhombus':
                draw_rhombus(screen, (0, 0, 0) if t == tool else (255, 255, 255), pygame.Rect(i * 50 + 10, 10, 30, 30))

        for square, square_color in squares:
            pygame.draw.rect(screen, square_color, square, 0)
        for triangle, triangle_color in right_triangles:
            draw_right_triangle(screen, triangle_color, triangle)
        for triangle, triangle_color in equilateral_triangles:
            draw_equilateral_triangle(screen, triangle_color, triangle)
        for rhombus, rhombus_color in rhombuses:
            draw_rhombus(screen, rhombus_color, rhombus)
        for rect, rect_color in rectangles:
            pygame.draw.rect(screen, rect_color, rect, 0)
        for center, radius, circle_color in circles:
            pygame.draw.circle(screen, circle_color, center, radius, 0)

        if start is not None and current is not None:
            if tool == 'rectangle':
                pygame.draw.rect(screen, color, pygame.Rect(start, (current[0]-start[0], current[1]-start[1])), 0)
            elif tool == 'circle':
                radius = int(((current[0]-start[0])**2 + (current[1]-start[1])**2)**0.5)
                pygame.draw.circle(screen, color, start, radius, 0)

        for i, col in enumerate(colors):
            pygame.draw.rect(screen, col, pygame.Rect(screen.get_width() - 20, i * 20, 20, 20))

        pygame.display.flip()
        clock.tick(60)

main()