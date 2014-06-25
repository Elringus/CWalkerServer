import webapp2
import json
from random import randint

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Panda! This is the server for the cwalker client.')

class Player(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({'PlayerPosition': get_spawn_point()})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

class Pointer(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({'PointerPosition': get_spawn_point()})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

class Obstacles(webapp2.RequestHandler):
    def get(self):
        c = {'Obstacles': []}
        for i in range(0, 100):
            spawn_point = get_spawn_point()
            c['Obstacles'].append(['house' if randint(0, 3) == 3 else 'tree', spawn_point[0], spawn_point[1]])
        data = json.dumps(c)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

# exclude lake from the spawn area
def get_spawn_point():
    quadrant = randint(1, 3)
    return {
        1: [randint(8, 24), randint(-24, 24)],
        2: [randint(-10, 9), randint(-24, -4)] if randint(0, 1) == 0 else [randint(-11, 9), randint(11, 24)],
        3: [randint(-24, -11), randint(-24, 24)],
    }[quadrant]

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getPointer', Pointer),
    ('/getPlayer', Player),
    ('/getObstacles', Obstacles),
], debug=True)
