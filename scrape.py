import requests
from bs4 import BeautifulSoup
states = [
        "acre",
"alagoas",
"amapa",
"amazonas",
"bahia",
"ceara",
"distrito-federal",
"espirito-santo",
"goias",
"maranhao",
"mato-grosso",
"mato-grosso-do-sul",
"minas-gerais",
"para",
"paraiba",
"parana",
"pernambuco",
"piaui",
"rio-de-janeiro",
"rio-grande-do-norte",
"rio-grande-do-sul",
"rondonia",
"roraima",
"santa-catarina",
"sao-paulo",
"sergipe",
"tocantins"
]    

reqs = []
locais_p = []
nome_locais = []
for state in states:
    print(state)
    req = requests.get('https://www.hemofiliabrasil.org.br/hemofilia/centros-de-tratamento-em-hemofilia/?uf={}'.format(state), verify=False)
    print(req.text)
    soup = BeautifulSoup(req.text, 'html.parser')
    occurrency = soup.find("section", {"class": "resultado"})
    #print(occurrency.contents)
    nome_estado = occurrency.find('h2')
    nome_locais = occurrency.find_next('ul').findAll('li')
    for local in nome_locais:
            locais_p = local.findAll('p')
            nome_local = local.find('h4')
     for local_p in locais_p:
             brs = local_p.findAll(text=True)
             for br in brs:
                     print(br)