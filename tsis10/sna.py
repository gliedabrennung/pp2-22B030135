import pygame
import time
import random
import psycopg2
import itertools

pygame.init()

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password= "sss13.08"
)

connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS snake_table(
    username VARCHAR(25),
    score VARCHAR(25)
    ) """) 

# DEFINE ALL STTAEMENTS
SPEED = 15
SCORE = 0
LEVEL = 1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DIRECTION = 'RIGHT'  # <- INITIAL SNAKE DIRECTION
CHANGE_TO = DIRECTION
CLOCK = pygame.time.Clock() # <- DEFINE FPS
SNAKE_POS = [300, 300] # <- DEFINE SNAKE FIRST POS
SNAKE_BODY = [[300, 300], [290, 300], [280, 300], [270, 300]] # <- DEFINE FIRST 4 SNAKE BODY POS
FRUIT_POS = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, # <- DEFINE FRUIT POS
             random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
FRUIT_SPAWN = True

positions = []


# DEFINE SCORE FUNCTION
def show_score():
    # CREATE FONT OBJECT
    SCORE_FONT = pygame.font.SysFont('Verdana', 20)

    # create the display surface object
    # score_surface
    SCORE_SURFACE = SCORE_FONT.render('Score : ' + str(SCORE), True, (255, 255, 255))
    SCORE_RECT = SCORE_SURFACE.get_rect()

    # DISPLAY TEXT
    SCREEN.blit(SCORE_SURFACE, SCORE_RECT)

def show_level():
    # creating font object level_font
    LEVEL_FONT = pygame.font.SysFont('Verdana', 20)

    # display surface object level_surface
    LEVEL_SURFACE = LEVEL_FONT.render('Level: ' + str(LEVEL), True, (255, 255, 255))

    # rectangular object for font
    LEVEL_RECT = LEVEL_SURFACE.get_rect()
    LEVEL_RECT.midtop = (40 , 20)

    # DISPLAY TEXT
    SCREEN.blit(LEVEL_SURFACE, LEVEL_RECT)
# GAME OVER FUNCTION

def login():
    global name
    global max_score
    FONT_SIZE = 24
    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    text_box = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 4 + 50, 200, 40)
    text = ""
    cursor = "|"
    ch = True
    while ch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    ch = False
                else:
                    text += event.unicode
                    
        name = text
        
        SCREEN.fill((0, 0, 0))
        pygame.draw.rect(SCREEN, (255, 255, 255), text_box, 2)
        text_surface = FONT.render(text + cursor, True, (255, 255, 255))
        SCREEN.blit(text_surface, (text_box.x + 5, text_box.y + 5))
        pygame.display.flip()
        
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, score FROM snake_table")
        m_s = cursor.fetchall()
        m_s1 = dict(m_s)
        if name in list(m_s1):
            max_score = m_s1[name]
        else:
            max_score = 0     
        
    with connection.cursor() as cursor:
        cursor.execute("SELECT username FROM snake_table")
        row = cursor.fetchall()
        rows = list(itertools.chain(*row))
        if name not in rows:
            cursor.execute("INSERT INTO snake_table (username, score) VALUES ('{}', '{}')".format(name, SCORE))
        
        
def game_over():
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, score FROM snake_table")
        row_1 = cursor.fetchall()
        rows_1 = dict(row_1)
        if int(SCORE) >= int(max_score):
            update = "UPDATE snake_table SET score = %s WHERE username = %s"
            cursor.execute(update, (SCORE, name))
        else:
            update = "UPDATE snake_table SET score = %s WHERE username = %s"
            cursor.execute(update, (int(max_score), name))
    print("Your current level -> ", LEVEL)
    print("Your current score -> ", SCORE)
    print("Your previous best score -> ", max_score)  
    SCREEN.fill("Black")
    go_font = pygame.font.SysFont('Verdana', 50)
    game_over_surface = go_font.render(
        'Your Score is : ' + str(SCORE), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    SCREEN.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

login()

running = True
# MAIN FUNC
while running:
    with connection.cursor() as cursor:
        update = "UPDATE snake_table SET score = %s WHERE username = %s"
        cursor.execute(update, (str(SCORE), name))    
        
    # KEY TRACKING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                CHANGE_TO = 'UP'
            if event.key == pygame.K_DOWN:
                CHANGE_TO = 'DOWN'
            if event.key == pygame.K_LEFT:
                CHANGE_TO  = 'LEFT'
            if event.key == pygame.K_RIGHT:
                CHANGE_TO = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                for i in range(0, len(SNAKE_BODY)):
                    positions.append(SNAKE_BODY[i])
                print("Your current positions -> ", positions)
                print("Your current level -> ", LEVEL)
                print("Your current score -> ", SCORE)
                print("Your previous best score -> ", max_score)  
                running = False

    if CHANGE_TO == 'UP' and DIRECTION != 'DOWN':
        DIRECTION = 'UP'
    if CHANGE_TO == 'DOWN' and DIRECTION != 'UP':
        DIRECTION = 'DOWN'
    if CHANGE_TO == 'LEFT' and DIRECTION != 'RIGHT':
        DIRECTION = 'LEFT'
    if CHANGE_TO == 'RIGHT' and DIRECTION != 'LEFT':
        DIRECTION = 'RIGHT'

    # SNAKE MOVING
    if DIRECTION == 'UP':
        SNAKE_POS[1] -= 10
    if DIRECTION == 'DOWN':
        SNAKE_POS[1] += 10
    if DIRECTION == 'LEFT':
        SNAKE_POS[0] -= 10
    if DIRECTION == 'RIGHT':
        SNAKE_POS[0] += 10

    #BY COLLIDING SNAKE AND FRUIT, THE SCORE WILL INCREASE BY 5
    SNAKE_BODY.insert(0, list(SNAKE_POS))
    if SNAKE_POS[0] == FRUIT_POS[0] and SNAKE_POS[1] == FRUIT_POS[1]:
        SCORE += 1
        if SCORE % 5 == 0:
            SPEED  += 5
            LEVEL += 1
        FRUIT_SPAWN = False
    else:
        SNAKE_BODY.pop()

    if not FRUIT_SPAWN:
        FRUIT_POS = [random.randrange(1, (SCREEN_WIDTH  // 10)) * 10,
                          random.randrange(1, (SCREEN_HEIGHT  // 10)) * 10]

    FRUIT_SPAWN = True
    SCREEN.fill((0,0,0))

    for pos in SNAKE_BODY:
        pygame.draw.rect(SCREEN, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(SCREEN, (255, 255, 255), pygame.Rect(FRUIT_POS[0], FRUIT_POS[1], 10, 10))

    # GAME OVER CONDITIONS
    if SNAKE_POS[0] < 0 or SNAKE_POS[0] > SCREEN_WIDTH - 10:
        game_over()
    if SNAKE_POS[1] < 0 or SNAKE_POS[1] > SCREEN_HEIGHT - 10:
        game_over()

    # IF HEAD COLLIDES BODY
    for block in SNAKE_BODY[1:]:
        if SNAKE_POS[0] == block[0] and SNAKE_POS[1] == block[1]:
            game_over()

    # DISPLAYING SCORE
    show_score()
    show_level()
    
    # REFRESH SCREEN
    pygame.display.update()

    # FPS RATE
    CLOCK.tick(SPEED)
    
    
#ЖОПАААААААААААААААААА ВРРРРРРРРРРРРРРР КЧАУ ФШШШШШШ ФШ ФШФ ФШФШФШФФШФ БРРРРРРРРРРРРРРРРРРЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ МЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯУ МУУУУУУУУУУУУР ГАВ ГАВ ПУК