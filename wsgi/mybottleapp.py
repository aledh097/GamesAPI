from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests


@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return template('index.tpl')

@route('/coc')
def coc():
    return template('coc.tpl')

@route('/steam')
def steam():
    return template('steam.tpl')

@route('/noticia')
def noticia():
    return template('noticia.tpl')

@route('/twitter')
def twitter():
    return template('twitter.tpl')

@route('/clan')
def clan():
    return template('clan.tpl')

@route('/perfil', method = ["GET"])
def perfil():
    return template('perfil.tpl')

@route('/resultadoperfil', method='POST')
def resultadoperfil():
    id_perfil = request.forms.get("idperfil")


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
