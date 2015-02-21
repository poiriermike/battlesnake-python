import bottle
import json
import math


def getDistance(item, snakePos):

    dx = snakePos[0] - item[0]
    dy = snakePos[1] - item[1]

    dx = math.fabs(dx)
    dy = math.fabs(dy)

    return dx + dy

#sorts min-max
def sortFoodList(unsorted, snakePos):
    return sorted(unsorted, )

def sortSnakeDist(enemeySnakeList, snakePos):
    return sorted(enemeySnakeList, key=getDistance(snakePos))














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

    list = data["food"]
    sortFoodList(list)




    return json.dumps({
        'move': 'left',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
