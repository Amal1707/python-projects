# program to simulate snake game

import pygame, random, sys, time

# check for initializing errors
check_errors = pygame.init()
if check_errors[1] >0:

    print("Game had {0} erros".format(check_errors[1]))
    sys.exit()
else:
    print("pygame successfully initialized")

# creating a game surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')

#colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(164,42,42) #food


#FPS contoller
fpsController = pygame.time.Clock()

#variables for the game
snakePos =[100,50]
snakeBody =[[100,50], [90,50], [80,50]]

foodPos =[random.randrange(1, 72)*10, random.randrange(1, 460)*10]
foodSpawn = False

direction = 'RIGHT'
changeTo = direction

score = 0
#Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72) #name, size of font (system provided font)
    GameOverSurface = myFont.render('Game Over!', True, red)
    GameOverRectangle = GameOverSurface.get_rect()
    GameOverRectangle.midtop = (360, 15)
    playSurface.blit(GameOverSurface, GameOverRectangle)
    pygame.mixer.Sound("crash.wav")
    showScore(0)
    pygame.display.flip() #update the frame to see the changes
    time.sleep(5)
    pygame.quit() #exit pygame window
    sys.exit() #exit console

#score board
def showScore(choice=1):
    scoreFont = pygame.font.SysFont('monaco', 24)
    scoreSurface = scoreFont.render('Score : {0}'.format(str(score)), True, black)
    scoreRectangle = scoreSurface.get_rect()
    if choice == 1:
        scoreRectangle.midtop = (80, 10)
    else:
        scoreRectangle.midtop = (360, 120)
    playSurface.blit(scoreSurface, scoreRectangle)
    pygame.display.flip() #update the frame to see the changes

# game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo =  'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo =  'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo =  'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo =  'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        
    # direction validation
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # snake body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    # food
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

    if snakePos[0] > 710 or snakePos[0] <0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] <0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    

    pygame.display.flip()
    showScore()
    fpsController.tick(20)
