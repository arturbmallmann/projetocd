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
  
