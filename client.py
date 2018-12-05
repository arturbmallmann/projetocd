#!/usr/bin/python3
import sys
import re #regex
import myRequests
from requests import HTTPError
from os import environ

args=sys.argv

#domain='http://127.0.0.1'
#porta='8080'

servers=environ['SERVERS'].split(',') if "SERVERS" in environ else False
def getServer():
    for s in servers:
        r=s.split(':')
        print("tentando %s" % (r))
        try:
            myRequests.list( *(r[0],r[1],"servers") )
            return (r[0],r[1])
        except:
            print("opqp")
            continue
        
def main():
    history=[]
    #regex0=re.compile(r"([A-Za-z]* ){1,}({.*})")
    while(True):
        res=input()
        res=res.split(' ')
        tup=tuple(res[1:])
        print("%s %s" % (res[0],tup),file=sys.stderr)
        if(res[0]=="quit"):
            return
        try:
            method=commands[res[0]]
            print (method)
            param = tuple(*getServer(),*tup) 
            print(param)
            answer=method(*param)
            print(answer.text)
        except HTTPError:
            print ("URL incorreta")
        except:
            print ("comando indisponível")#,file=sys.stderr)

  
commands = {"list":myRequests.list,"create":myRequests.create,"new":myRequests.create}
if __name__=='__main__':
    print(getServer())
    main()


    print(myRequests.list)
    print(myRequests.create)
