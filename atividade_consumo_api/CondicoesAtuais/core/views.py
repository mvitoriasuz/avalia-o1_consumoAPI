from django.shortcuts import HttpResponse
import requests

def CondicoesAtuais(request): 
    try:
        URL = "http://servicos.cptec.inpe.br/XML/estacao/SBGR/condicoesAtuais.xml"
        resp = requests.get(URL)

        if resp.status_code == 200:
            return HttpResponse(resp.content, content_type="application/xml")
        else:
            return HttpResponse("Erro ao acessar a API", status=resp.status_code)
    except:
        return HttpResponse("Erro ao conectar-se à API", status=500)


