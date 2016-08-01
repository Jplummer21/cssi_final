import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Listener(ndb.Model):
    listener_first = ndb.StringProperty()
    listener_last = ndb.StringProperty()

class Artist(ndb.Model):
    artist_first = ndb.StringProperty()
    artist_last = ndb.StringProperty()
    stage_name = ndb.StringProperty()
    bio = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome %s! (<a href="%s">Sign Out</a>)') % (user.nickname(), users.create_logout_url('/'))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.') % users.create_login_url('/')
        template = jinja_environment.get_template('templates/forms.html')
        self.response.write(template.render({'greeting': greeting}))

class ListenerHandler(webapp2.RequestHandler):
    def get(self):
        artist1 = "this is my favorite artist"
        fav_artists = {
            'artist1': artist1
        
        }
        template = jinja_environment.get_template('templates/listener.html')
        self.response.write(template.render(fav_artists))



class ArtistHandler(webapp2.RequestHandler):
    def get(self):
       template = jinja_environment.get_template('templates/artist.html')
       self.response.write("This is the Artist Page!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/listener', ListenerHandler),
    ('/artist', ArtistHandler)
], debug=True)
