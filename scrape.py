import requests
from bs4 import BeautifulSoup

states = [
        "Acre",
        "Alagoas",
        "Amapa",
        "Amazonas",
        "Bahia",
        "Ceara",
        "Distrito Federal",
        "Espirito Santo",
        "Goias",
        "Maranhao",
        "Mato Grosso",
        "Mato Grosso do Sul",
        "Minas Gerais",
        "Para",
        "Paraiba",
        "Parana",
        "Pernambuco",
        "Piaui",
        "Rio de Janeiro",
        "Rio Grande do Norte",
        "Rio Grande do Sul",
        "Rondonia",
        "Roraima",
        "Santa Catarina",
        "Sao Paulo",
        "Sergipe",
        "Tocantins"
]

states_normalized= []

for state in states:
    state_norm = state.replace(' ', '-').lower()
    #print(state_norm)
    states_normalized = state_norm



for state in states_normalized:
    req = requests.get('https://www.hemofiliabrasil.org.br/hemofilia/centros-de-tratamento-em-hemofilia/?uf={}'.format(state))
    #print(req.text)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.prettify())

    
