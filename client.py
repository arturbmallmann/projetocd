#!/usr/bin/python3
import sys
import requests
args=sys.argv

domain='http://127.0.0.1'
porta='8080'
def main():
    while(True):
        res=input()
        res=res.split(' ')
        tup=tuple(res[1:])
        if(res[0]=="quit"):
            return
        try:
            answer=commands[res[0]](*tup)
            print(answer.text)
        except:
            print ("comando indisponível")
            
def create(uri,content):
    url=(domain,porta,uri)
    return requests.post("%s:%s/%s" % url,content)

def list(uri):
    print(uri)
    url=(domain,porta,uri)
    return requests.get("%s:%s/%s" % url)
    
commands = {"list":list,"create":create,"new":create}
if __name__=='__main__':
    main()

