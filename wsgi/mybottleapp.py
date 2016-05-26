from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests
import json
import time
from HTMLParser import HTMLParser
from coc.api import ClashOfClans

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

@route('/noticia', method = ["GET"]) 
def noticia():
    return template('noticia.tpl')

@route('/twitter')
def twitter():
    return template('twitter.tpl')

@route('/clan')
def clan():
    return template('clan.tpl')

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
    return template('resultadoperfil.tpl',id_perfil=id_perfil,id=id,nick=nick,nombre_real=nombre_real,Avatar=Avatar,Pais=Pais,Codigo_del_Estado=Codigo_del_Estado,Codigo_de_la_ciudad=Codigo_de_la_ciudad,estado=estado,ultimo_logeo=ultimo_logeo,id_clan=id_clan,fecha_creacion=fecha_creacion)

@route('/resultadoperfil2', method='POST')
def resultadoperfil2():
    nick = request.forms.get("nick")
    dicc_parametros2={'key':'1685786EECBF130267010877BAB447D0','vanityurl':nick}
    r2 = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/", params=dicc_parametros2)
    datos2 = json.loads(r2.text.encode("utf-8"))
    id_nick=datos2["response"]["steamid"]
    dicc_parametros3={'key':'1685786EECBF130267010877BAB447D0','steamids':id_nick}
    r3 = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros3)
    datos2 = json.loads(r3.text.encode("utf-8"))
    try:
        nombre_real= datos2["response"]["players"][0]["realname"]    
    except:
        nombre_real="no disponible"
    try:
        id= datos2["response"]["players"][0]["steamid"]    
    except:
        id="no disponible"
    try:
        nick=datos2["response"]["players"][0]["personaname"]   
    except:
        nick="no disponible"
    try:
        Avatar=datos2["response"]["players"][0]["avatarfull"]
    except:
        Avatar="no disponible"
    try:
        Pais=datos2["response"]["players"][0]["loccountrycode"]
    except:
        Pais="no disponible"
    try:
        Codigo_del_Estado=datos2["response"]["players"][0]["locstatecode"]
    except:
        Codigo_del_Estado="no disponible"
    try:
        Codigo_de_la_ciudad=datos2["response"]["players"][0]["loccityid"]
    except:
        Codigo_de_la_ciudad="no disponible"
    try:
        estado=datos2["response"]["players"][0]["personastate"]
    except:
        estado="no disponible"
    try:
        ultimo_logeo=time.ctime(int(datos2["response"]["players"][0]["lastlogoff"]))
    except:
        ultimo_logeo="no disponible"
    try:
        id_clan=datos2["response"]["players"][0]["primaryclanid"]
    except:
        id_clan="no disponible"
    try:
        fecha_creacion=time.ctime(int(datos2["response"]["players"][0]["timecreated"]))
    except:
        fecha_creacion="no disponible"
    return template('resultadoperfil2.tpl',id_perfil=id_nick,id=id,nick=nick,nombre_real=nombre_real,Avatar=Avatar,Pais=Pais,Codigo_del_Estado=Codigo_del_Estado,Codigo_de_la_ciudad=Codigo_de_la_ciudad,estado=estado,ultimo_logeo=ultimo_logeo,id_clan=id_clan,fecha_creacion=fecha_creacion)

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

@route('/ranking', method = ["GET"])
def noticia():
    return template('ranking.tpl')

@route('/resultadoranking', method='POST')
def resultadoranking():
    api=ClashOfClans("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE1OGNiY2NlLTVkNTEtNDdkMC1iOTMwLWYwMGI3NzQ2ZGFhNCIsImlhdCI6MTQ2NDAzMDk5Nywic3ViIjoiZGV2ZWxvcGVyL2I3YjQ3ZmNjLTgxN2YtMzhmYy1jODBmLWQxZDgyNjM0ZmI3ZCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjUyLjcuMjE3LjEwIl0sInR5cGUiOiJjbGllbnQifV19.UeDlXmkYiyZUwzKkiZY6YCUVnfB19AjAQ9I4SJbVWVoZ2YI1uhGpull-ZHJ5jtHDPFV92-H_Qcjp15NXeouQmg")
    id = type(request.forms.get("nombrelocalidad"))
    #localizaciones2=api.locations(int(id)).rankings('clans').get()
    return template('resultadoranking.tpl', nombres=id)

# This must be added in order to do correct path lookups for the views
import os
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
