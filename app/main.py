import bottle
import json
import math


ourSnakeHead = [0,0]
snakeName = "cscusnake"
def getDistance(item):

    dx = ourSnakeHead[0] - item[0]
    dy = ourSnakeHead[1] - item[1]

    dx = math.fabs(dx)
    dy = math.fabs(dy)

    return dx + dy

def getDistance(itemA, itemB):

    dx = itemA[0] - itemB[0]
    dy = itemA[1] - itemB[1]

    dx = math.fabs(dx)
    dy = math.fabs(dy)

    return dx + dy

#sorts min-max
def sortListByDist(unsorted):
    return sorted(unsorted, key=getDistance)


def findBestFood(orderedFoodList, orderedSnakeList):

    for i in range(0, len(orderedFoodList)):
        item = orderedFoodList[i]

        for j in range(0, len(orderedSnakeList)):
            if( getDistance(item, orderedSnakeList[j]) < getDistance(item, ourSnakeHead)):
                #someone is closer - ignore the food
                break
            else: #we are closer, go for this food
                return item #return the item position

    # we are not closest to any food, define default behaviour

    return orderedFoodList[0]



def checkFood(foodList, enemySnakePos):

    sortedFood = sortListByDist(foodList)
    sortedEnemyPos = sortListByDist(enemySnakePos)

    return moveDown() #determine which way to go here


def check_up(location, board, distance=1):


    if location[0] > 0:
        if board[location[0] - 1][location[1]]['state'] != 'food' or  board[location[0] - 1][location[1]]['state'] != 'food':
            return False
    else:
        return True
def check_down(location, snakes, distance=1):
    pass
def check_left(location, snakes, distance=1):
    pass
def check_right(location, snakes, distance=1):
    pass

@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json

    return json.dumps({
        'name': snakeName,
        'color': '#00ff00',
        'head_url': 'http://cscusnake.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


def moveUp(taunt = ""):
    return json.dumps({
        'move': 'up',
        'taunt': taunt
    })
def moveDown(taunt = ""):
    return json.dumps({
        'move': 'down',
        'taunt': taunt
    })
def moveLeft(taunt = ""):
    return json.dumps({
        'move': 'left',
        'taunt': taunt
    })
def moveRight(taunt = ""):
    return json.dumps({
        'move': 'right',
        'taunt': taunt
    })

@bottle.post('/move')
def move():
    data = bottle.request.json
    #print (data)
    food = data["food"]
    snakes = data["snakes"]
    board = data['board']

    print(str((check_up(snakes[0]['cooreds'][0], board))))

    global ourSnakeHead
    enemySnakeHeads = []
    for i in range(0, len(snakes)):
        if(snakes[i]["name"] == snakeName):
            ourSnakeHead = snakes[i]["coords"][0] # set our snake head position
        else:
            enemySnakeHeads.add(snakes[i]["coords"][0]) #add enemy snake

    if(True):#if go for food
        return checkFood(food, enemySnakeHeads)
    elif(False): #not going for food
        pass #do nothing, remove later
    #more cases here

    #default code - to be removed
    return json.dumps({
        'move': 'left',
        'taunt': 'battlesnake-python!'
    })

#Callum doing things don't worry about this
def eachTurnMove(curX, curY, nextX, nextY):

    #goal is to give in the current position
    # (get tht from the head and pass it in here)
    #Step 1. Determine which is a greater change, the x or y
    #Step 2. Move left or right depending on blahh

    dX = abs(curX - nextX)
    dy = abs(curY - nextY)

    if(dX > dY):
        #goal here is to see which the smaller straight line is
        #dX > dY would mean that we want to do UP/DOWN FIRST then do left/right
        if(curY > nextY):
            return moveDown()
        elif(curY < nextY):
            return  moveUp()


    else:
        #means that left/right is the shortest line to the object
        if(curX > nextX):
            #goLeft
            return moveLeft()
        elif(curX < nextX):
            #goRight
            return moveRight()


    if(curX > nextX):
        #goLeft
        moveLeft()
    elif(curX < nextX):
        #goRight
        moveRight()
    elif(curX == nextX):
        #goStraight
        pass


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


def main():
    move()

if __name__ == "__main__":
    move()

# Expose WSGI app
application = bottle.default_app()
