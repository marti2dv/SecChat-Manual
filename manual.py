import os
import urllib

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())


class UserInterfacePage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('userInterface.html')
        self.response.write(template.render())

class FAQPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('FAQ.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/UserInterface', UserInterfacePage),
    ('/FAQ', FAQPage),
], debug=True)
