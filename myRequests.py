# new/create recurso {"conteúdo":"hehe"}            
import requests 
def create(domain,porta,uri,content):
    url=tuple(domain,porta,uri)
    #print(url)
    return requests.post("http://{}:{}/{}".format(url),content)
# list recurso
# new raiz {"id":1,"nome":"artur"}

def list(domain,porta,uri):
    url=(domain,porta,uri)
    #print ("entrou {}".format(url))
    return requests.get("http://{}:{}/{}".format(*url))
 
#class myRError (HTTP
