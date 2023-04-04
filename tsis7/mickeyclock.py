import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

main = pygame.image.load('images/mickeyN.png')
rh = pygame.image.load('images/min.png')
lh = pygame.image.load('images/sec.png')

running = True
while running:
    pygame.display.update()
    screen.blit(main, (0, 0))
    time = datetime.datetime.now()
    rot1 = pygame.transform.rotate(lh, -time.second * 6)
    rot1_rect = rot1.get_rect(center = (400, 300))
    screen.blit(rot1, rot1_rect)
    rot2 = pygame.transform.rotate(rh, -time.minute * 6)
    rot2_rect = rot2.get_rect(center = (400, 300))
    screen.blit(rot2, rot2_rect)
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()