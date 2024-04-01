"""
Programm has 3 tools:
- Rectangle (default)
- Circle
- Eraser

How to draw rectangle:
- Press R to select rectangle tool
- Click and hold LMB to start drawing rectangle
- Release LMB to finish drawing rectangle

How to draw circle:
- Press C to select circle tool
- Click and hold LMB to start drawing circle
- Release LMB to finish drawing circle

How to erase:
- Press E to select eraser tool
- Click the area where you want to erase the shapes

How to change color:
- Click on the color panel on the right side of the screen to change the color

"""



import pygame

###Creating DrawRectangle function. This function will use pygame's event handler to get the mouse position when LMB is pressed and when it is released. It will then draw a rectangle using the two points as the opposite corners.
def drawRectangle(screen):
    done = False
    start = None
    current = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start = event.pos
            if event.type == pygame.MOUSEMOTION:
                if start is not None:
                    current = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    start = None

        screen.fill((0, 0, 0))  # Clear the screen with a black background
        if start is not None and current is not None:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(start, (current[0]-start[0], current[1]-start[1])), 1)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    
    radius = 15
    mode = 'blue'
    points = []
    rectangles = []  # List to store rectangles
    circles = []  # List to store circles
    start = None
    current = None
    tool = 'rectangle'  # Initialize tool to 'rectangle'
    color = (255, 255, 255)  # Current color

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
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
                    if start is not None:
                        end = event.pos
                        # When a shape is created, store its color
                        if tool == 'rectangle':
                            rectangles.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
                        elif tool == 'circle':
                            radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
                            circles.append((start, radius, color))
                        if tool == 'eraser':
                            # Erase rectangles
                            rectangles = [(rect, rect_color) for rect, rect_color in rectangles if not rect.collidepoint(end)]
                            # Erase circles
                            circles = [(center, radius, circle_color) for center, radius, circle_color in circles if ((end[0]-center[0])**2 + (end[1]-center[1])**2)**0.5 > radius]
                        start = None
                        current = None

        screen.fill((0, 0, 0))

        # # When a shape is created, store its color
        # if tool == 'rectangle':
        #     rectangles.append((pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), color))
        # elif tool == 'circle':
        #     radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
        #     circles.append((start, radius, color))

        # When a shape is drawn, use its stored color
        for rect, rect_color in rectangles:
            pygame.draw.rect(screen, rect_color, rect, 1)
        for center, radius, circle_color in circles:
            pygame.draw.circle(screen, circle_color, center, radius, 1)

        # When the temporary shape is drawn, use the current color
        if start is not None and current is not None:
            if tool == 'rectangle':
                pygame.draw.rect(screen, color, pygame.Rect(start, (current[0]-start[0], current[1]-start[1])), 1)
            elif tool == 'circle':
                radius = int(((current[0]-start[0])**2 + (current[1]-start[1])**2)**0.5)
                pygame.draw.circle(screen, color, start, radius, 1)

         # Draw color selection panel
        for i, col in enumerate(colors):
            pygame.draw.rect(screen, col, pygame.Rect(screen.get_width() - 20, i * 20, 20, 20))



        # # draw all points
        # i = 0
        # while i < len(points) - 1:
        #     drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        #     i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
# if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1: # left click grows radius
            #         radius = min(200, radius + 1)
            #     elif event.button == 3: # right click shrinks radius
            #         radius = max(1, radius - 1)
            
            # if event.type == pygame.MOUSEMOTION:
            #     # if mouse moved, add point to list
            #     position = event.pos
            #     points = points + [position]
            #     points = points[-256:]
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()