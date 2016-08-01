#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
        template = jinja_environment.get_template('')
        self.response.write(template.render())


class ArtistHandler(webapp2.RequestHandler):
    def get(self):
       template = jinja_environment.get_template('')
       self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/listener', ListenerHandler),
    ('/artist', ArtistHandler)
], debug=True)
