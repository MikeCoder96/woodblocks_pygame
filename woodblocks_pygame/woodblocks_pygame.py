import sys
import pygame
from pygame.locals import *
import shapes_template as toPlace
from random import randint

activeAggregate = None

def makeAggregate(shape):
    blocksAggregate = []
    for i in range(0, len(shape)):
        for j in range(0, len(shape[i])):
            if (shape[i][j] == 1):
                blocksAggregate.append([block_size * j, block_size * i])

    return blocksAggregate

def canMove(aggregate, x, y) -> bool:
    pass

def aggregateIsPlaceable(aggregate) -> bool:
    for point in aggregate:
        x = int(point[0] / 40)
        y = int(point[1] / 40)
        if (matrix[x][y] == True):
            return False
    return True

def placeAggregateOnMatrix(aggregate):
    if (aggregateIsPlaceable(aggregate)):
        for point in aggregate:
            x = int(point[0] / 40)
            y = int(point[1] / 40)
            matrix[x][y] = True

# Initialize the game
shapes=[]
matrix = [
    [False for _ in range(0, 10)]
   for _ in range(0,10)
   ]
keys = [False, False, False, False]
playerpos=[20,95]
pygame.init()
width, height = 440, 675
screen=pygame.display.set_mode((width, height))

# Load images
block_size = 40
block = pygame.image.load("resources/assets/quad_1.png")
block = pygame.transform.scale(block, (block_size, block_size))
blockToPlace = pygame.image.load("resources/assets/quad_2.png")
blockToPlace = pygame.transform.scale(blockToPlace, (block_size, block_size))
background = pygame.image.load("resources/assets/background.jpg")
background = pygame.transform.scale(background, (width, height))

# Score
points = 0
font = pygame.font.SysFont("comicsansms", 25)
player = font.render("DLV", True, (0, 128, 0))

randShape = toPlace.state[16]
activeAggregate = makeAggregate(randShape)


while True:
    score = font.render(str(points), True, (0, 128, 0))
    # Clear the screen before drawing it again
    screen.fill(0)
    # Draw the screen elements
    screen.blit(background, (0,0))

    columnToRemove = []
    rowToRemove = []

    # Check for completed row and column and print
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]:
                screen.blit(block, (20 + (40 * x), (95 + (40 * y))))

    for column in range(len(matrix)):
        isColumnCompleted = True
        for row in range(len(matrix)):
            if matrix[column][row] == False:
                isColumnCompleted = False
        if isColumnCompleted:
            columnToRemove.append(column)

    for row in range(len(matrix)):
        isRowCompleted = True
        for column in range(len(matrix)):
            if matrix[column][row] == False:
                isRowCompleted = False
        if isRowCompleted:
            rowToRemove.append(row)

    for column in columnToRemove:
        for row in range(len(matrix)): 
            matrix[column][row] = False
        points += 10

    for row in rowToRemove:
        for column in range(len(matrix)):
            matrix[column][row] = False
        points += 10


    rowToRemove.clear()
    columnToRemove.clear()

    # Stampa blocchi player
    if activeAggregate != None:
        for point in activeAggregate:
            p = [point[0] + 20, point[1] + 95]
            screen.blit(blockToPlace, p)

    screen.blit(player, (95, 15))
    screen.blit(score, (270, 15))
    for x in shapes:
        screen.blit(x[0], x[1])
    # Update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                keys[3]=True
            elif event.key==pygame.K_SPACE:
                if (aggregateIsPlaceable(activeAggregate)):
                    placeAggregateOnMatrix(activeAggregate)
                    activeAggregate = makeAggregate(toPlace.state[randint(0, 18)])
                    points += len(activeAggregate) #Point update in base alla grandezza dello shape "attualmente 1"
                    # Generate random shape from shapes template.
                    # Da fare 3 volte, per ogni blocco da spawanre
                    randShape = toPlace.state[randint(0, 18)]
                    blockAggregate = None
                    initialPosition = [0, 0]
               # for row in randShape:
                   # for cell in row:
                        #if (cell == 1):
                            
                #playerpos = [22,97]

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                keys[3]=False

        # W
        if keys[0]:
            if (activeAggregate != None):
                for i in range(0, len(activeAggregate)):
                    activeAggregate[i][1] -= 40
        # A
        if keys[1]:
            if (activeAggregate != None):
                for i in range(0, len(activeAggregate)):
                    activeAggregate[i][0] -= 40   
        # S
        if keys[2]:
            if (activeAggregate != None):
                for i in range(0, len(activeAggregate)):
                    activeAggregate[i][1] += 40
        # D
        if keys[3]:
            if (activeAggregate != None):
                for i in range(0, len(activeAggregate)):
                    activeAggregate[i][0] += 40