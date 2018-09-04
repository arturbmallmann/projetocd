#!/usr/bin/python3
from bottle import route, run, template,post,get,request
import json
import requests
import os

root=dict()
servers=list()
@route('/raiz')
@post()
def raiz():
    print("entrou")
#    stream=request.body;
#    data=stream.read()
#    print("input %s" % (data))
#    data=json.loads(data)
    data=json.load(request.body)
    root.update({data.get('id'):(data)})
    response=''

    for item in data.items():
        response+="%s : %s\n" % item
    print (response)
    return response

@route('/raiz/<item>')
@get()
def getTree(item):
    print (root)
    return root.get(int(item)) if int(item) in root else '{}'

@route('/servers')
@get()
def servers():
    resp = json.dumps(servers)
    return resp

@route('/<nome>')
@get()
def teste(nome):
    return template('<b> teste do {{name}} </b>',name=nome)


def main():
    run(host = 'localhost', port=8080)

if __name__=='__main__':
    servers = os.environ["SERVERS"].split(',') if "SERVERS" in os.environ else False
    main()
    print (servers)
