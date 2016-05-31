from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests
import json
import time
from HTMLParser import HTMLParser
from coc.api import ClashOfClans
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import os

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


CONSUMER_KEY = "bIkflkYaMdPDbJPkU4JJo3vk4"
CONSUMER_SECRET = "jdZa2HB3ZAnRwZB8aNWgOJWz5mFaKmOwfOIJVxyCa0qvJThk2R"

TOKENS = {}

def get_access_token(TOKENS):
  
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
  
  
  r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
  credentials = parse_qs(r.content)
  TOKENS["access_token"] = credentials.get('oauth_token')[0]
  TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]

@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return template('index.tpl')

@route('/csgo')
def coc():
    return template('csgo.tpl')

@route('/steam')
def steam():
    return template('steam.tpl')

@route('/noticia', method = ["GET"]) 
def noticia():
    return template('noticia.tpl')

@route('/estadisticas', method = ["GET"])
def estadisticas():
    return template('estadisticas.tpl')

@route('/perfilopciones')
def perfil():
    return template('perfilopciones.tpl')

@route('/opcionid', method = ["GET"])
def perfil():
    return template('opcionid.tpl')

@route('/opcionnick', method = ["GET"])
def perfil():
    return template('opcionnick.tpl')

@route('/resultadoperfil', method='POST')
def resultadoperfil():
    id_perfil = request.forms.get("idperfil")
    dicc_parametros={'key':'1685786EECBF130267010877BAB447D0','steamids':id_perfil}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros)
    datos = json.loads(r.text.encode("utf-8"))
    try:
        nombre_real= datos["response"]["players"][0]["realname"]    
    except:
        nombre_real="no disponible"
    try:
        id= datos["response"]["players"][0]["steamid"]    
    except:
        id="no disponible"
    try:
        nick=datos["response"]["players"][0]["personaname"]   
    except:
        nick="no disponible"
    try:
        Avatar=datos["response"]["players"][0]["avatarfull"]
    except:
        Avatar="no disponible"
    try:
        Pais=datos["response"]["players"][0]["loccountrycode"]
    except:
        Pais="no disponible"
    try:
        Codigo_del_Estado=datos["response"]["players"][0]["locstatecode"]
    except:
        Codigo_del_Estado="no disponible"
    try:
        Codigo_de_la_ciudad=datos["response"]["players"][0]["loccityid"]
    except:
        Codigo_de_la_ciudad="no disponible"
    try:
        estado=datos["response"]["players"][0]["personastate"]
    except:
        estado="no disponible"
    try:
        ultimo_logeo=time.ctime(int(datos["response"]["players"][0]["lastlogoff"]))
    except:
        ultimo_logeo="no disponible"
    try:
        id_clan=datos["response"]["players"][0]["primaryclanid"]
    except:
        id_clan="no disponible"
    try:
        fecha_creacion=time.ctime(int(datos["response"]["players"][0]["timecreated"]))
    except:
        fecha_creacion="no disponible"
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('resultadoperfil.tpl',id_perfil=id_perfil,id=id,nick=nick,nombre_real=nombre_real,Avatar=Avatar,Pais=Pais,Codigo_del_Estado=Codigo_del_Estado,Codigo_de_la_ciudad=Codigo_de_la_ciudad,estado=estado,ultimo_logeo=ultimo_logeo,id_clan=id_clan,fecha_creacion=fecha_creacion,authorize_url=authorize_url)

@route('/resultadoperfil2', method='POST')
def resultadoperfil2():
    nick = request.forms.get("nick")
    dicc_parametros2={'key':'1685786EECBF130267010877BAB447D0','vanityurl':nick}
    r2 = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/", params=dicc_parametros2)
    datosnick = json.loads(r2.text.encode("utf-8"))
    id_nick=datosnick["response"]["steamid"]
    dicc_parametros3={'key':'1685786EECBF130267010877BAB447D0','steamids':id_nick}
    r3 = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros3)
    datos2 = json.loads(r3.text.encode("utf-8"))
    
    if datosnick["response"]["message"] == 'No match':
        return template('404.tpl', nick=nick)

@route('/resultadonoticia', method='POST')
def resultadonoticia():
    nombrejuego = request.forms.get("nombrejuego")
    r=requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
    lineas=json.loads(r.text)
    fichero=lineas["applist"]["apps"]
    for f in fichero:
        if f["name"]==nombrejuego:
            id_juego_nombre=f["appid"]
    dicc_parametros4={'appid':id_juego_nombre}
    r4 = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/", params=dicc_parametros4)
    datos3 = json.loads(r4.text.encode("utf-8"))
    titulo=datos3["appnews"]["newsitems"][0]["title"]
    detalles=datos3["appnews"]["newsitems"][0]["contents"]
    url_noticia=datos3["appnews"]["newsitems"][0]["url"]
    return template('resultadonoticia.tpl', titulo=titulo, detalles=detalles, url_noticia=url_noticia)

@route('/resultadoestadisticas', method='POST')
def resultadoestadisticas():
    nick = request.forms.get("nickcsgo")
    dicc_parametros5={'key':'1685786EECBF130267010877BAB447D0','vanityurl':nick}
    r5 = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/", params=dicc_parametros5)
    datos4 = json.loads(r5.text.encode("utf-8"))
    id_nick=datos4["response"]["steamid"]
    dicc_parametros6={'key':'1685786EECBF130267010877BAB447D0','steamid':id_nick}
    r6 = requests.get("http://api.steam powered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730", params=dicc_parametros6)
    datos5 = json.loads(r6.text.encode("utf-8"))
    dicc_parametros7={'key':'1685786EECBF130267010877BAB447D0','steamids':id_nick}
    r7 = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros7)
    datos7 = json.loads(r7.text.encode("utf-8"))
    avatar=datos7["response"]["players"][0]["avatarfull"]
    total_victimas=datos5["playerstats"]["stats"][0]["value"]
    total_muertes=datos5["playerstats"]["stats"][1]["value"]
    cabeza=datos5["playerstats"]["stats"][25]["value"]
    bombas_colocadas=datos5["playerstats"]["stats"][3]["value"]
    bombas_desactivadas=datos5["playerstats"]["stats"][4]["value"]
    rehenes=datos5["playerstats"]["stats"][8]["value"]
    jugadas=datos5["playerstats"]["stats"][128]["value"]
    ganadas=datos5["playerstats"]["stats"][127]["value"]
    estrellas=datos5["playerstats"]["stats"][102]["value"]
    armas_equipo=datos5["playerstats"]["stats"][38]["value"]
    victimas_arma_enemiga=datos5["playerstats"]["stats"][26]["value"]
    cegadas=datos5["playerstats"]["stats"][40]["value"]
    disparos=datos5["playerstats"]["stats"][47]["value"]
    impactos=datos5["playerstats"]["stats"][46]["value"]
    dominaciones=datos5["playerstats"]["stats"][43]["value"]
    victimas_dominaciones=datos5["playerstats"]["stats"][44]["value"]
    venganzas_dominaciones=datos5["playerstats"]["stats"][45]["value"]
    rondas_pistolas=datos5["playerstats"]["stats"][27]["value"]
    zeus=datos5["playerstats"]["stats"][179]["value"]
    ventanas=datos5["playerstats"]["stats"][39]["value"]
    media=round(float(datos5["playerstats"]["stats"][0]["value"])/float(datos5["playerstats"]["stats"][1]["value"]),3)
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('resultadoestadistica.tpl', media=media, avatar=avatar,nick=nick,total_victimas=total_victimas,total_muertes=total_muertes, cabeza=cabeza,bombas_colocadas=bombas_colocadas,bombas_desactivadas=bombas_desactivadas,rehenes=rehenes,jugadas=jugadas,ganadas=ganadas,estrellas=estrellas,armas_equipo=armas_equipo,victimas_arma_enemiga=victimas_arma_enemiga,cegadas=cegadas,disparos=disparos,impactos=impactos,dominaciones=dominaciones,victimas_dominaciones=victimas_dominaciones,venganzas_dominaciones=venganzas_dominaciones,rondas_pistolas=rondas_pistolas,zeus=zeus,ventanas=ventanas,authorize_url=authorize_url)

def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
 
def get_access_token(TOKENS):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["access_token"] = credentials.get('oauth_token')[0]
    TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]

@get('/callback')

def get_verifier():
  TOKENS["request_token"]=request.get_cookie("request_token", secret='some-secret-key')
  TOKENS["request_token_secret"]=request.get_cookie("request_token_secret", secret='some-secret-key')
  TOKENS["verifier"] = request.query.oauth_verifier
  get_access_token(TOKENS)
  response.set_cookie("access_token", TOKENS["access_token"],secret='some-secret-key')
  response.set_cookie("access_token_secret", TOKENS["access_token_secret"],secret='some-secret-key')
  redirect('/twittear')

@get('/twitter')
def twitter():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    return template('twitter.tpl', authorize_url=authorize_url)


@get('/twittear')
def twittear():
    if request.get_cookie("access_token", secret='some-secret-key'):
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      return template('tweet.tpl')  
    else:
      redirect('/twitter')


@post('/twittear')
def tweet_submit():
  texto = request.forms.get("tweet")
  TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
  TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
  print CONSUMER_KEY
  print CONSUMER_SECRET
  print TOKENS["access_token"]
  print TOKENS["access_token_secret"]
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
  url = 'https://api.twitter.com/1.1/statuses/update.json'
  r = requests.post(url=url,
                      data={"status":texto},
                      auth=oauth)
  if r.status_code == 200:
    return "<p>Tweet enviado correctamente :D</p>"
  else:
    return "<p>No puede enviar el tweet, intentelo mas tarde...</p>"+r.content

# This must be added in order to do correct path lookups for the views
import os
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
