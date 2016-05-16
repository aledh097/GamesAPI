from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests
import json
import time

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
    dicc_parametros={'key':'1685786EECBF130267010877BAB447D0','steamids':id_perfil}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=dicc_parametros)
    datos = json.loads(r.text.encode("utf-8"))
    try:
        nombre_real= datos["response"]["players"][0]["realname"]
        
    try:
        id=datos["response"]["players"][0]["steamid"]
    try:
        nick=datos["response"]["players"][0]["personaname"]
    try:
        Avatar=datos["response"]["players"][0]["avatarfull"]
    try:
        Pais=datos["response"]["players"][0]["loccountrycode"]
    try:
        Codigo_del_Estado=datos["response"]["players"][0]["locstatecode"]
    try:
        Codigo_de_la_ciudad=datos["response"]["players"][0]["loccityid"]
    try:
        estado=datos["response"]["players"][0]["personastate"]
    try:
        ultimo_logeo=time.ctime(int(datos["response"]["players"][0]["lastlogoff"]))
    try:
        id_clan=datos["response"]["players"][0]["primaryclanid"]
    try:
        fecha_creacion=time.ctime(int(datos["response"]["players"][0]["timecreated"]))

    return template('resultadoperfil.tpl',id_perfil=id_perfil,id=id,nick=nick,nombre_real=nombre_real,Avatar=Avatar,Pais=Pais,Codigo_del_Estado=Codigo_del_Estado,Codigo_de_la_ciudad=Codigo_de_la_ciudad,estado=estado, ultimo_logeo=ultimo_logeo,id_clan=id_clan,fecha_creacion=fecha_creacion)

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
