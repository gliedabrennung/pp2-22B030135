import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Mixer")

playlist = ['music/ЗАМАЙ, Слава КПСС - Antihypeintro.mp3', 
            'music/ЗАМАЙ, Слава КПСС - Похуист.mp3', 
            'music/ЗАМАЙ, Слава КПСС - Сиротская отрыжка.mp3',
            'music/СД, ЗАМАЙ feat. Слава КПСС - Горец.mp3',
            'music/Слава КПСС - Red Widow.mp3',
            'music/Слава КПСС - Икар.mp3']

i = 0
j = 0

x = pygame.mixer.music.load(playlist[0])
pygame.mixer.music.play()

n = False
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                i += 1
                if i % 2 == 0:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                j += 1
                if j < len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
            elif event.key == pygame.K_LEFT:
                j -= 1
                if j > -len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
                