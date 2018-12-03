import pygame
import time
import random 
import math

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (35,65,155)
green = (0,155,0)

gameDisplay = pygame.display.set_mode((1280,800))
pygame.display.set_caption('Slither')

#FPS
FPS = 60
clock = pygame.time.Clock()

#snake block size
block_size = 20

#enemy block size
block_sz = 60
speed = 20
speed2 = 15

#player health
playerHealth = 100

#Health image
healthImg = pygame.image.load('healthbarimg.png')
#enemy image
enemyImg = pygame.image.load('enemyimg.png')


font = pygame.font.SysFont(None, 25)


def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, black, [XnY[0],XnY[1],block_size,block_size])

lead_x = 300
lead_y = 300
snake.x = lead_x
snake.y = lead_y

def enemy(block_sz):
    #gameDisplay.blit(enemyImg,(900,700))
    pygame.draw.rect(gameDisplay, blue,(enemy.x,enemy.y,block_sz,block_sz))
    enemy.x = 900
    enemy.y = 700
            
def playerHp(block_sz):
    gameDisplay.blit(healthImg,(10,10))
    gameDisplay.blit(healthImg,(45,10))
    gameDisplay.blit(healthImg,(80,10))

    
##    pygame.draw.rect(gameDisplay,red,(10,10,block_sz,block_sz))
##    pygame.draw.rect(gameDisplay,red,(45,10,block_sz,block_sz))
##    pygame.draw.rect(gameDisplay,red,(80,10,block_sz,block_sz))

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [450,350])
    
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = 300
    lead_y = 300
    snake.x = lead_x
    snake.y = lead_y
    enemy.x = 900
    enemy.y = 700

    lead_x_change = 0
    lead_y_change = 0

    healthList = []
    healthLength = 1

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, 800-10))#/10.0)*10.0
    randAppleY = round(random.randrange(0, 800-10))#/10.0)*10.0
    
    while not gameExit:

        while enemy.x >= 900:
            enemy.x = speed
            while enemy.x == 10:
                enemy.x * -1 >= 900
            

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameOver = False
                        gameLoop()
                        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                if event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                if event.key == pygame.K_UP:
                    lead_y_change = -10
                if event.key == pygame.K_DOWN:
                    lead_y_change = 10   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
            if lead_x >= 1280 or lead_x < 0 or lead_y >= 800 or lead_y < 0:
                gameOver = True       
###############################ENEMY AI#######################################


             
                
                        



            #if enemy.x > 890:
                #enemy.x = -speed
            #elif enemy.x < 10:
                #enemy.x = +speed

            #if enemy.y < snake.y:
                #enemy.y = enemy.speed
            #elif enemy.y > snake.y:
                #enemy.y = enemy.speed
 
            
                    

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness,AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        snake(block_size, snakeList)
        enemy(block_sz)
        playerHp(block_sz)
        
        
        
              
        pygame.display.update()

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0, 800-10))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, 800-10))#/10.0)*10.0
##                snakeLength += 1 

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print("x crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
               
                randAppleX = round(random.randrange(0, 800-10))#/10.0)*10.0
                randAppleY = round(random.randrange(0, 800-10))#/10.0)*10.0
                snakeLength += 1 

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
               
                randAppleX = round(random.randrange(0, 800-10))#/10.0)*10.0
                randAppleY = round(random.randrange(0, 800-10))#/10.0)*10.0
                snakeLength += 1

            
                
        clock.tick(FPS)
        
    pygame.quit()
    quit()

gameLoop()
