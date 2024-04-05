# API de Condições meteorológicas das capitais do Brasil

Este é um consumo de API simples para verificar as condições meteorológicas atuais das capitais dos estados brasileiros, que retorna uma lista de informações atualizadas de hora em hora, relativas aos dados das Estações de Superfície dos Aeroportos listando apenas os dados Metar dos aeroportos localizados nas capitais.

### Para entender a sigla de quatro letras que representa a estação meteorológica de superfície. Veja a seguinte documentação 
 - [Estações de Superfície dos Aeroportos](http://servicos.cptec.inpe.br/XML/#estacoes-metar:~:text=Topo-,Esta%C3%A7%C3%B5es%20de%20Superf%C3%ADcie%20dos%20Aeroportos,-Sigla)
 - [Siglas das condições do tempo](http://servicos.cptec.inpe.br/XML/#estacoes-metar:~:text=Topo-,Siglas%20das%20condi%C3%A7%C3%B5es%20do%20tempo,-Sigla)

### URL para requisição dos dados das condições meteorológicas atuais das capitais
http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml

# Requisitos
- Python
- Django

### 1. Configurando o Ambiente
Clone esse repositório
- Navegue até o diretório do projeto
- Na pasta do projeto, ative o ambiente virtual
```
.\atividade_consumo_api\venv\Scripts>activate
.\atividade_consumo_api\venv\Scripts>activate.bat
```
### 2. Instalação dos Pacotes
Instale o Pacote _Requests_
```
pip install requests
```
  - Dependencias necessárias
```
pip freeze > requirements.txt
```
### 3. Utilização
- No cmd retorne para a pasta do projeto e inicie o servidor de desenvolvimento Django
```
\atividade_consumo_api\CondicoesAtuais>python manage.py runserver
```
Caso o servidor de desenvolvimento Django seja iniciado com sucesso, será apresentadoo o endereço IP padrão para o seu próprio computador (localhost), e a porta, fazendo com que você acesse a aplicação Django no navegador de prefefencia

## Esse projeto foi desenvolvimento a partir das seguintes ferramentas
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>  </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
