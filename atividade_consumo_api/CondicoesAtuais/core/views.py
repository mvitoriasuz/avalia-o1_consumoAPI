from django.shortcuts import HttpResponse
import requests

def CondicoesAtuais(request):  # Renomeado de 'requests' para 'request'
    URL = "http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml"
    resp = requests.get(URL)

    if resp.status_code == 200:
        return HttpResponse(resp.content, content_type="application/xml")
    else:
        return HttpResponse("Erro ao acessar a API", status=resp.status_code)
