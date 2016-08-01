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
    favorite_genre = ndb.StringProperty()

class Artist(ndb.Model):
    artist_first = ndb.StringProperty()
    artist_last = ndb.StringProperty()
    stage_name = ndb.StringProperty()
    hometown = ndb.StringProperty()
    genre = ndb.StringProperty()
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
        template = jinja_environment.get_template('templates/listener.html')
        self.response.write(template.render())

    def post(self):
        listener_first = self.request.get('first_name')
        listener_last = self.request.get('last_name')
        favorite_genre = self.request.get('fave_genre')
        listener_info = {
            'listener_first': listener_first,
            'listener_last': listener_last,
            'favorite_genre': favorite_genre
        }
        template = jinja_environment.get_template('templates/listener-registration.html')
        self.response.write(template.render(listener_info))

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/artist.html')
        self.response.write(template.render())

    def post(self):
        artist_first = self.request.get('a_first')
        artist_last = self.request.get('a_last')
        stage_name = self.request.get('a_stage_name')
        hometown = self.request.get('a_hometown')
        genre = self.request.get('a_genre')
        bio = self.request.get('a_bio')
        artist_info = {
            'artist_first': artist_first,
            'artist_last': artist_last,
            'stage_name': stage_name,
            'hometown': hometown,
            'genre': genre,
            'bio': bio
        }
        template = jinja_environment.get_template('templates/artist-registration.html')
        self.response.write(template.render(artist_info))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/listener', ListenerHandler),
    ('/artist', ArtistHandler)
], debug=True)
