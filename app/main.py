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


    item = foodList[0]
    for i in range(0, len(orderedSnakeList)):
        if( getDistance(item, orderedSnakeList[i]) < getDistance(item, ourSnakeHead)):
            #someone is closer
            pass



    return foodList[0]



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


def moveUp():
    return json.dumps({
        'move': 'up'
    })
def moveDown():
    return json.dumps({
        'move': 'down'
    })
def moveLeft():
    return json.dumps({
        'move': 'left'
    })
def moveRight():
    return json.dumps({
        'move': 'right'
    })

@bottle.post('/move')
def move():
    data = bottle.request.json
    print data
    food = data["food"]
    snakes = data["snakes"]
    board = data['board']

    print check_up(snakes[snakeName][0], board)

    snakeHeads = []
    for i in range(0, len(snakes)):
        snakeHeads.add(snakes["coords"][0])

    global ourSnakeHead

    ourSnakeHead = [0,0] # We need to update this somehow

    if(True):#if go for food
        return checkFood(food, snakeHeads)
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

    if(curX - nextX > 0):
        #goLeft


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
