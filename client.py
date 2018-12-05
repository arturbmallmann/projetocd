#!/usr/bin/python3
import sys
import requests
import re #regex
args=sys.argv

domain='http://127.0.0.1'
porta='8080'
def main():
    history=[]
	regex0=re.compile(r"([A-Za-z]* ){1,}({.*})")
    while(True):
        res=input()
        res=res.split(' ')
        tup=tuple(res[1:])
        print(tup,file=sys.stderr)
        if(res[0]=="quit"):
            return
        try:
            method=commands[res[0]]
            answer=method(*tup)
#            print ("passou")
            print(answer.text)
#        except JSONDecodeError:
#            print ("resposta incorreta")
        except:
            print ("comando indisponível")#,file=sys.stderr)

# new/create recurso {"conteúdo":"hehe"}            
def create(uri,content):
    url=(domain,porta,uri)
    return requests.post("%s:%s/%s" % url,content)
# list recurso
# new raiz {"id":1,"nome":"artur"}

def list(uri):
    print(uri)
    url=(domain,porta,uri)
    return requests.get("%s:%s/%s" % url)
    
commands = {"list":list,"create":create,"new":create}
if __name__=='__main__':
    main()

