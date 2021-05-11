import sys
import copy
import os
import pygame
from random import randint
from pygame.locals import *
import shapes_template as toPlace
from AI import *
from shapeAggregate import *

activeAggregate = None
base_path = os.path.dirname(__file__)
hint_count = 1
HINT_PRICE = 50
NO_MOVES_LEFT = False

#BUTTON
def create_button(button, image, position, callback):
    button["image"] = image
    button["rect"] = image.get_rect(topleft=position)
    button["callback"] = callback
 
def button_on_click(button, event):
    if event.button == 1:
        if button["rect"].collidepoint(event.pos):
            button["callback"](button)
 
def push_button_player(button):
    global MODE
    global p_name
    p_name = "Player"
    MODE = 1

def push_button_dlv(button):
    global MODE
    global p_name
    p_name = "DLV"
    MODE = 2
    
def push_button_retry(button):
    global MODE
    global NO_MOVES_LEFT
    NO_MOVES_LEFT = False
    MODE = 0

def push_button_hint(button):
    global points
    if (points < (HINT_PRICE * hint_count)):
        print("no points, no hints")
    else:
        points -= (HINT_PRICE * hint_count)
        #ai.useHint() #TODO: Add hint func in AI
#############


# An aggregate is a list of individual (x,y) points representing a shape.
# Each (x,y) point takes into account block_size.
def makeAggregate():
    shape = toPlace.state[randint(0, 18)]
    blocksAggregate = []
    for i in range(0, len(shape)):
        for j in range(0, len(shape[i])):
            if (shape[i][j] == 1):
                blocksAggregate.append([block_size * j, block_size * i])

    return blocksAggregate

def canMove(aggregate, cX, cY) -> bool:
    for x in aggregate:
        if x[0] + cX < 0 or x[0] + cX > 360:
            return False
        if x[1] + cY < 0 or x[1] + cY > 360:
            return False

    return True

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

def printShape(aggregate, x, y):
    for index in range(0, len(aggregate)):
        screen.blit(blockSelections, [x + aggregate[index][0] / 40 * 30, y + aggregate[index][1] / 40 * 30])

def generateShapesToUse():
    global shapes
    # Genero 3 tipi di blocchi da piazzare
    for x in range(3):
        if (shapes[x] == None):
            shapes[x] = makeAggregate()
            originalShapes[x] = copy.deepcopy(shapes[x])

def resetGame():
    # Initialize the game
    global shapes, originalShapes, matrix, playerpos, MODE, points, p_name
    shapes=[None, None, None]
    originalShapes=[None, None, None]
    matrix = [
        [False for _ in range(0, 10)]
       for _ in range(0,10)
       ]
    playerpos=[20,95]
    points = 0
    p_name = ""
    generateShapesToUse()


shapes=[None, None, None]
originalShapes=[None, None, None]
matrix = [
    [False for _ in range(0, 10)]
    for _ in range(0,10)
    ]
keys = [False, False, False, False]
playerpos=[20,95]
MODE = 0 #1 = player, 2 = AI
points = 0
p_name = ""

pygame.init()
width, height = 440, 675
screen=pygame.display.set_mode((width, height))
font1 = pygame.font.SysFont("fixedsys", 55)
font2 = pygame.font.SysFont("fixedsys", 34)
font3 = pygame.font.SysFont("fixedsys", 82)
select1_player = font1.render("You want to play", True, (255, 255, 255))
select2_player = font1.render("or", True, (255, 255, 255))
select3_player = font1.render("leave it to DLV?", True, (255, 255, 255))
retry_text = font3.render("Retry??", True, (255, 255, 255))
indexSelected = 0
canBeSelected = [[width / 8, 540], [width / 8 * 5, 540]]
# Load images
block_size = 40
block = pygame.image.load(os.path.join(base_path, "resources", "assets", "quad_1.png"))
block = pygame.transform.scale(block, (block_size, block_size))

blockSelections = pygame.image.load(os.path.join(base_path, "resources", "assets", "quad_1.png"))
blockSelections = pygame.transform.scale(block, (30, 30))

blockToPlace = pygame.image.load(os.path.join(base_path, "resources", "assets", "quad_2.png"))
blockToPlace = pygame.transform.scale(blockToPlace, (block_size, block_size))

blockNotPlacable = pygame.image.load(os.path.join(base_path, "resources", "assets", "quad_3.png"))
blockNotPlacable = pygame.transform.scale(blockNotPlacable, (block_size, block_size))

background = pygame.image.load(os.path.join(base_path, "resources", "assets", "background.jpg"))
background = pygame.transform.scale(background, (width, height))


hint_button = {}
hint_image = pygame.image.load(os.path.join(base_path, "resources", "assets", "hint_btn.png"))
hint_image = pygame.transform.scale(hint_image, (50, 50))

dlv_button = {}
dlv_image = pygame.image.load(os.path.join(base_path, "resources", "assets", "dlv_play.png"))
dlv_image = pygame.transform.scale(dlv_image, (180, 100))

player_button = {}
player_image = pygame.image.load(os.path.join(base_path, "resources", "assets", "player_play.png"))
player_image = pygame.transform.scale(player_image, (180, 100))

retry_button = {}
retry_image = pygame.image.load(os.path.join(base_path, "resources", "assets", "retry_btn.png"))
retry_image = pygame.transform.scale(retry_image, (180, 100))

questionBox = pygame.image.load(os.path.join(base_path, "resources", "assets", "questionbox.png"))
questionBox = pygame.transform.scale(questionBox, (400, 430))

create_button(dlv_button, dlv_image, ((width / 2) + 15, (height / 2) - 10), push_button_dlv)
create_button(player_button, player_image, ((width / 2) - 190, (height / 2) - 10), push_button_player)
create_button(hint_button, hint_image, (370, 10), push_button_hint)
create_button(retry_button, retry_image, ((width / 2) - 90, (height / 2) - 10), push_button_retry)

def createShapeImage(aggregate):
    shapeImage = block
    for i in range(1, len(aggregate)):
        screen.blit(block, (aggregate[i][0], aggregate[i][1]))
    return shapeImage

# First available shape position
availableShapesY = 95 + (block_size * 10) + block_size * 2.5
availableShapesMargin = block_size / 2
availableShapesScale = 0.75

generateShapesToUse()

originalShapes = copy.deepcopy(shapes)

#INITIALIZE AI
#ai = AI()
#print(ai.getOptimalPlacement(matrix, ShapeAggregate(shapes, 0, block_size)))

while True:
    if NO_MOVES_LEFT:
        MODE = 0
    player = font2.render(p_name, True, (0, 128, 0))
    activeAggregate = shapes[indexSelected]
    score = font2.render(str(points), True, (0, 128, 0))
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

    if MODE > 0:
        # Stampa blocchi player
        if activeAggregate != None:
            for point in activeAggregate:
                p = [point[0] + 20, point[1] + 95]
                if (aggregateIsPlaceable(activeAggregate)):
                    screen.blit(blockToPlace, p)
                else:
                    screen.blit(blockNotPlacable, p)
        
        screen.blit(hint_button["image"], hint_button["rect"])
        screen.blit(player, (87, 20))
        screen.blit(score, (270, 20))


    if MODE == 0:
        #Show player mode        
        screen.blit(questionBox, ((width / 2) - 200, (height / 2) - 253))
        if not NO_MOVES_LEFT:
            screen.blit(select1_player, ((width / 2) - 150, (height / 2) - 180))
            screen.blit(select2_player, ((width / 2) - 150, (height / 2) - 135))
            screen.blit(select3_player, ((width / 2) - 150, (height / 2) - 90))
            screen.blit(player_button["image"], player_button["rect"])
            screen.blit(dlv_button["image"], dlv_button["rect"])
        else:
            resetGame()
            screen.blit(retry_text, ((width / 2) - 90, (height / 2) - 130))
            screen.blit(retry_button["image"], retry_button["rect"])

    if MODE > 0:
        placeToUse = 0
        for i in range(3):
            if (i == indexSelected or shapes[i] == None):
                continue
            printShape(originalShapes[i], canBeSelected[placeToUse][0], canBeSelected[placeToUse][1])
            placeToUse += 1
    
    # Update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if NO_MOVES_LEFT:
                button_on_click(retry_button, event)
            else:
                button_on_click(hint_button, event)
                button_on_click(player_button, event)
                button_on_click(dlv_button, event)

        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 

        if MODE == 1:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w or event.key==pygame.K_UP:
                    keys[0]=True
                elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                    keys[1]=True
                elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                    keys[2]=True
                elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                    keys[3]=True
                elif event.key==pygame.K_TAB:
                    while True:
                        indexSelected += 1
                        if indexSelected == 3:
                            indexSelected = 0
                        if shapes[indexSelected] != None:
                            break
                        
                elif event.key==pygame.K_SPACE:
                    if (aggregateIsPlaceable(activeAggregate)):
                        placeAggregateOnMatrix(activeAggregate)
                        points += len(activeAggregate)
                        shapes[indexSelected] = None
                        activeAggregate = next((item for item in shapes if item is not None), None)
                        generateShapesToUse()
                    
                        while True:
                            indexSelected += 1
                            if indexSelected == 3:
                                indexSelected = 0
                            if shapes[indexSelected] != None:
                                break


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
                if (canMove(activeAggregate, 0 , -40)):
                    if (activeAggregate != None):
                        for i in range(0, len(activeAggregate)):
                            activeAggregate[i][1] -= 40
            # A
            if keys[1]:
                if (canMove(activeAggregate, -40, 0)):
                    if (activeAggregate != None):
                        for i in range(0, len(activeAggregate)):
                            activeAggregate[i][0] -= 40   
            # S
            if keys[2]:
                if (canMove(activeAggregate, 0, 40)):
                    if (activeAggregate != None):
                        for i in range(0, len(activeAggregate)):
                            activeAggregate[i][1] += 40
            # D
            if keys[3]:
                if (canMove(activeAggregate, 40, 0)):
                    if (activeAggregate != None):
                        for i in range(0, len(activeAggregate)):
                            activeAggregate[i][0] += 40

        #if ai.endGame():
        #    global MODE
        #    global NO_MOVES_LEFT
        #    NO_MOVES_LEFT = True
        #    MODE = 0
            