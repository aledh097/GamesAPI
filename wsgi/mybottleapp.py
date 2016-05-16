from bottle import Bottle, route, run, request, template, default_app, static_file

@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return template('index.tpl')

@route('/coc')
def index():
    return template('coc.tpl')

@route('/steam')
def index():
    return template('steam.tpl')

@route('/noticia')
def index():
    return template('noticia.tpl')

@route('/twitter')
def index():
    return template('twitter.tpl')

@route('/perfil')
def index():
    return template('perfil.tpl')

@route('/clan')
def index():
    return template('clan.tpl')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
                                      'app-root/repo/wsgi/views/'))
application=default_app()
run(host='localhost', port=8080)