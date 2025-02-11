import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc 


chave = "e069c7ba0bd563cca4907242a77ba4ee"
cidade = "Belo Horizonte"
api_link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cidade, chave)

#chamada do api usando request
r = requests.get(api_link)

#Convertendo os dados presentes na variavel r em dicionario
dados = r.json()
print(dados)

# Informações para app de clima zona, país e hora
pais_codigo = dados["sys"]["country"]

# Zona
zona_fuso = pytz.country_timezones[pais_codigo]

# #País
pais = pytz.country_names[pais_codigo]
print(pais)

#data
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S")



# tempo 
tempo = dados["main"]["temp"]
humidade = dados["main"]["humidity"]
descricao = dados["weather"][0]["description"]


#Alterçãoes de informações
def pais_para_continente(i):
    pais_alpha = pc.country_name_to_country_alpha2(i)
    pais_continent_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continent_codigo)

    return pais_continente_nome 

continente = pais_para_continente(pais)
