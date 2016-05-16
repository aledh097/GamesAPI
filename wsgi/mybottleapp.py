from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests

HOST = '87.221.173.76'

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

@route('/perfil', method='POST')
def perfil():
    return template('perfil.tpl')

@route('/resultadoperfil', method='GET')
def resultadoperfil():
    id_perfil = request.forms.get("idperfil")
    dicc_parametros={'key':'1685786EECBF130267010877BAB447D0','steamids':id_perfil}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros)
    datos = json.loads(r.text.encode("utf-8"))
    id=datos["response"]["players"][0]["steamid"]
    nick=datos["response"]["players"][0]["personaname"]
    return template('resultadoperfil.tpl')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
