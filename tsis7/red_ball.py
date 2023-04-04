import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Red Ball')

x = 400
y = 300
radius = 25
speed = 20

running = True
while running:
    pygame.time.delay(50)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y - 20 <= 0:
            y += 0
        else:
            y -= 20
    elif keys[pygame.K_DOWN]:
        if y - 20 <= 0:
            y += 0
        else:
            y += 20
    elif keys[pygame.K_LEFT]:
        if x - 20 <= 0:
            x += 0
        else:
            x -= 20
    elif keys[pygame.K_RIGHT]:
        if x - 20 <= 0:
            x += 0
        else:
            x += 20

    screen.fill('White')
    pygame.draw.circle(screen, 'Red', (x, y), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()