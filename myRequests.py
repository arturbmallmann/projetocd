# new/create recurso {"conteúdo":"hehe"}            
def create(url,content):
#	url=tuple(domain,porta,uri)
	print(url)
	return requests.post("%s:%s/%s" % url,content)
# list recurso
# new raiz {"id":1,"nome":"artur"}

def list(uri):
#    url=(domain,porta,uri)
    print(url)
    return requests.get("%s:%s/%s" % url)
  
