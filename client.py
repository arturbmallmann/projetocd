#!/usr/bin/python3
import sys
import requests
import myRequests
args=sys.argv

domain='http://127.0.0.1'
porta='8080'
def main():
    history=[]
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

  
commands = {"list":myRequests.list,"create":myRequests.create,"new":myRequests.create}
if __name__=='__main__':
    main()

