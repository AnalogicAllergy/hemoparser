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
for state in states:
    print(state)
    req = requests.get('https://www.hemofiliabrasil.org.br/hemofilia/centros-de-tratamento-em-hemofilia/?uf={}'.format(state), verify=False)
    print(req.text)
    #soup = BeautifulSoup(req.text, 'html.parser')
    #occurrency = soup.find("section", {"class": "resultado"})
    #print(occurrency.contents)
    #ocr_h2 = occurrency.find('h2')
    #print(ocr_h2.contents)
#print(reqs.text)