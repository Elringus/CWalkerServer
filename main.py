import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Panda! This is the server for the cwalker client.')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
