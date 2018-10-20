import requests
import html

from filtro import WORDS_NOT_FOR_JOKE

def get_piada():
    try:
        data = requests.get('https://www.reddit.com/r/tiodopave/random/.json', headers={'User-agent': 'glaubeitor'}).json()[0]['data']['children'][0]['data']
    except:
        pass
    if data:
        piada = data['title']
        resposta = ' '.join(data['selftext'].split('\n'))
        return piada + '\n\n' +  resposta

def piada_valida():
    piada_invalida = True
    piada = html.unescape(get_piada()).lower()
    while(piada_invalida):
        for palavra in WORDS_NOT_FOR_JOKE:
            if palavra in piada:
                piada = get_piada()
                continue
        piada_invalida = False
    return piada

print(piada_valida())