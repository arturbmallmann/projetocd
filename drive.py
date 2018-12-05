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
    print(servers)
    resp = json.dumps(servers)
    return resp

@route('/servers/<item>')
@post()
def add_servers():
    data = set(json.load(request.body))
    new = data + set(servers)
    print(new)
    #todo
@route('/<nome>')
@get()
def teste(nome):
    return template('<b> teste do {{name}} </b>',name=nome)

def testOthers():
    print("outros?")
    if (servers == False):
        return
    while(True):
        sleep(1)
        for the in servers[1:]:
         #   if (not the):
            try:
                myRequests.list( *(the[0],the[1],"servers") )
                print("Fez o request para {}".format(the))
            except:
                pass
this=False
def main():
    port=8080
    this=False
    print("vem")
    while(not this):
        try:
            this=["localhost",str(port)]
            run(host=this[0],port=this[1])
        except:
            port+=1
            this=False
            print("ups")
        
if __name__=='__main__':
    servers = environ["SERVERS"].split(',') if "SERVERS" in environ else False
    servers = [s.split(':') for s in servers]
    print (servers)
    t=threading.Thread(target=testOthers)
 #   m=threading.Thread(target=main)
  #  m.start()
   # m.join()
    t.start()
    #t.join()
    main()
   # main()
    print (servers)
