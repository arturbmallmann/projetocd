#!/usr/bin/python3
from bottle import route, run, template,post,get,request
import json
import requests
@route('/teste')
@post()
def teste():
    nome=request.forms.get('nome');
    return template('<b> teste do {{name.nome}} </b>',name=json.loads(data))

@route('/teste/<nome>')
@get()
def teste(nome):
    return template('<b> teste do {{name}} </b>',name=nome)


run(host = 'localhost', port=8080)
