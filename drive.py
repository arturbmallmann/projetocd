#!/usr/bin/python3
from bottle import route, run, template,post,get,request
import json
import myRequests
from os import environ #para as variáveis locais
import threading 
#import sys #para argumentos
from time import sleep

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

def testOthers():
	print("outros?")
	while(True):
		sleep(1)
		for the in servers:
			url=the.split(':')
			myRequests.list( (url[0],url[1],"servers") )

def main():
	port=8080
	teste=True
	while(teste):
		try:
			teste=False
			run(host = 'localhost', port=port)
		except:
			port+=1
			teste=True
		
if __name__=='__main__':
	servers = environ["SERVERS"].split(',') if "SERVERS" in environ else False
	t=threading.Thread(target=testOthers)
	t.run()
	main()
	print (servers)
