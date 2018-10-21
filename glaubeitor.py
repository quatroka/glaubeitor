import requests
import html

from filtro import WORDS_NOT_FOR_JOKE

def get_piada():
    try:
        data = requests.get('https://www.reddit.com/r/tiodopave/random/.json', headers={'User-agent': 'glaubeitor'}).json()[0]['data']['children'][0]['data']
    except:
        exit()
    if data:
        piada = data['title']
        resposta = ' '.join(data['selftext'].split('\n'))
        return html.unescape(piada + '\n\n' +  resposta).lower()

def validar_piada(piada):
    valid = True
    for palavra in WORDS_NOT_FOR_JOKE:
        if palavra in piada:
            valid = False
    return valid


def piada_valida():
    piada_valida = False
    piada = ''
    while(not piada_valida):
        piada = get_piada()
        if validar_piada(piada):
            break
    return piada

print(piada_valida())
