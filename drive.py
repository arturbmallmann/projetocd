#!/usr/bin/python3
from bottle import route, run, template,post,get,request
import json
import requests

root=dict()

@route('/root/<item>')
@get()
def getTree(*item):
    return json.dumps(root.get(item))

@route('/root/')
@post()
def newItem():
    data=request.body.read()
    root.update(json.loads(data))
    
@route('/teste')
@post()
def teste():
    stream=request.body;
    data=stream.read()
    print("input %s" % (data))
    data=json.loads(data)
    response=''

    for item in data.items():
        response+="%s : %s\n" % item
    print (response)
    return response
@route('/teste/<nome>')
@get()
def teste(nome):
    return template('<b> teste do {{name}} </b>',name=nome)


run(host = 'localhost', port=8080)
