import webapp2
import json
from random import randint
import time

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Panda! This is the server for the cwalker client.')

class Player(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({"PlayerPosition": [randint(-24, 24), randint(-24, 24)]})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

class Pointer(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({"PointerPosition": [randint(-24, 24), randint(-24, 24)]})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getPointer', Pointer),
    ('/getPlayer', Player),
], debug=True)
