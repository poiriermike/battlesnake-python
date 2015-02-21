import bottle
import json
import math


ourSnakeHead = [0,0]

def getDistance(item):

    dx = ourSnakeHead[0] - item[0]
    dy = ourSnakeHead[1] - item[1]

    dx = math.fabs(dx)
    dy = math.fabs(dy)

    return dx + dy

#sorts min-max
def sortListByDist(unsorted):
    return sorted(unsorted, key=getDistance)



def checkFood(foodList, enemySnakePos):

    sortedFood = sortListByDist(foodList)
    sortedEnemyPos = sortListByDist(enemySnakePos)













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
        'name': 'battlesnake-python',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
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

    food = data["food"]
    snakes = data["snakes"]

    global ourSnakeHead

    ourSnakeHead = [0,0] # We need to update this somehow
    checkFood(food, snakes)



    return json.dumps({
        'move': 'left',
        'taunt': 'battlesnake-python!'
    })


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
