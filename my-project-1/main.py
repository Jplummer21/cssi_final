#-*- coding: utf-8 -*-

import webapp2
import os
import jinja2
import logging
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
    soundcloud = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            greeting = ('Welcome %s! (<a href="%s">Sign Out</a>)') % (user.nickname(), users.create_logout_url('/'))
        else:
            greeting = ('<a href="%s">Sign In!</a>') % users.create_login_url('/')
        template = jinja_environment.get_template('templates/forms.html')
        self.response.write(template.render({'greeting': greeting}))

    def post(self):
        user_value = self.request.get('user_type')
        template_val = 'templates/' + user_value + '.html'
        if user_value == 'artist':
            url_val = '/createartist'
        elif user_value == 'listener':
            url_val = '/' + user_value
        else:
            pass
        template = jinja_environment.get_template(template_val)
        self.response.write(template.render({'user_value': user_value}))
        self.redirect(url_val)

class ListenerHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/listener.html')
        self.response.write(template.render())

    def post(self):
        user = users.get_current_user()
        if not user:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)
            return
        listener_first = self.request.get('first_name')
        listener_last = self.request.get('last_name')
        favorite_genre = self.request.get('fave_genre')

        listener_record = {
            'listener_first': listener_first,
            'listener_last': listener_last,
            'favorite_genre': favorite_genre
        }

        new_listener = Listener(
            listener_first=listener_first,
            listener_last=listener_last,
            favorite_genre=favorite_genre,
            # id = user.user_id()
        )
        listener_key = new_listener.put()
        template = jinja_environment.get_template('templates/listener_output.html')
        # template_values = {
        #     'listener': listener_record,
        #     'artist': artist_record, #somehow, get this info from the datastore.
        # }

        self.response.write(template.render(listener_record))
        if favorite_genre == 'Rap':
            artist_query = Artist.query().filter(Artist.genre == 'Rap')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Jazz':
            artist_query = Artist.query().filter(Artist.genre == 'Jazz')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Hip-Hop':
            artist_query = Artist.query().filter(Artist.genre == 'Hip-Hop')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'R&B':
            artist_query = Artist.query().filter(Artist.genre == 'R&B')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Pop':
            artist_query = Artist.query().filter(Artist.genre == 'Pop')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Country':
            artist_query = Artist.query().filter(Artist.genre == 'Country')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Classical':
            artist_query = Artist.query().filter(Artist.genre == 'Classical')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'EDM':
            artist_query = Artist.query().filter(Artist.genre == 'EDM')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Alternative':
            artist_query = Artist.query().filter(Artist.genre == 'Alternative')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Dubstep':
            artist_query = Artist.query().filter(Artist.genre == 'Dubstep')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')
        elif favorite_genre == 'Rock':
            artist_query = Artist.query().filter(Artist.genre == 'Rock')
            artist_link = artist_query.fetch()
            for x in artist_link:
                self.response.write('<p><a href = "artist/' + str(x.key.id()) + '">'  + x.stage_name + '</a>' + '</p>')

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/artist.html')
        self.response.write(template.render())

    def post(self):
        user = users.get_current_user()
        if not user:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)
            return
        artist_first = self.request.get('a_first')
        artist_last = self.request.get('a_last')
        stage_name = self.request.get('a_stage_name')
        hometown = self.request.get('a_hometown')
        genre = self.request.get('a_genre')
        bio = self.request.get('a_bio')
        soundcloud = self.request.get('a_soundcloud')

        artist_info = {
            'artist_first': artist_first,
            'artist_last': artist_last,
            'stage_name': stage_name,
            'hometown': hometown,
            'genre': genre,
            'bio': bio,
            'soundcloud': soundcloud
        }

        new_artist = Artist(
            artist_first = artist_first,
            artist_last = artist_last,
            stage_name = stage_name,
            hometown = hometown,
            genre = genre,
            bio = bio,
            soundcloud = soundcloud)
            # id = user.user_id()
        artist_key = new_artist.put()
        new_artist = artist_key.get()
        # ident = str(artist_key.id())
        url_string = artist_key.urlsafe()
        template = jinja_environment.get_template('templates/artist_output.html')
        self.response.write(template.render(artist_info))

class ArtistPage(webapp2.RequestHandler):
    def get(self):
        # artist_url = self.request.url
        # # url = urlparse(artist_url)
        # key = ndb.Key(urlsafe=artist_url)
        # new_artist = key.get()
        # # artist_id =
        # content = Artist.all()
# class ArtistPage(webapp2.RequestHandler):
#     def get(self):
        template = jinja_environment.get_template('templates/artist_output.html')
        self.response.write(template.render())
#
#     def post(self):
#         template_val = 'templates/artist.html'
#         url_val = '/' + user.id()
#         template = jinja_environment.get_template(template_val)
#         self.response.write(template.render())
#         self.redirect(url_val)

class Redirect(webapp2.RequestHandler):
    def get(self, artist_id):
        artist_id = int(artist_id)

        artist_info = ndb.Key('Artist', long(artist_id)).get()
        artist_info = {
            'artist_first': artist_info.artist_first,
            'artist_last': artist_info.artist_last,
            'stage_name': artist_info.stage_name,
            'hometown': artist_info.hometown,
            'genre': artist_info.genre,
            'bio': artist_info.bio,
            'soundcloud': artist_info.soundcloud
        }
        template = jinja_environment.get_template('templates/output.html')
        # self.response.write(template.render(artist_link))
        template = jinja_environment.get_template('templates/artist_output.html')
        self.response.write(template.render(artist_info))





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/listener', ListenerHandler),
    ('/createartist', ArtistHandler),
    # ('/getartist', ArtistPage),
    ('/artist/([0-9]+)', Redirect)
], debug=True)
