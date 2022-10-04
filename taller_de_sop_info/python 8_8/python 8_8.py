import requests
import pandas as pd
from bs4 import BeautifulSoup


pagina = requests.get(
    "https://es.wikipedia.org/wiki/Anexo:Medallero_hist%C3%B3rico_de_los_Juegos_Ol%C3%ADmpicos_de_verano")

objeto_sopa = BeautifulSoup(pagina.content, 'html.parser')
e1 = objeto_sopa.find_all('table')
t1 = e1[0]
# print(t1.prettify())

e2 = t1.find('tbody')

e3 = e2.find_all('tr')
i = 0
for x in e3:
    if x != e3[0]:
        if x.find('small') != None:
            x1 = x.find_all('a')

            x2 = x.find_all('td')
            if i == 0:
                diccionario = {'pais': str(x1[1].get_text()), 'oro': str(x2[2].get_text()), 'plata': str(
                    x2[3].get_text()), 'bronce': str(x2[4].get_text()), 'total': str(x2[5].get_text())}
                dataframe = pd.DataFrame(diccionario, columns=[
                                         'pais', 'oro', 'plata', 'bronce', 'total'], index=[i])
            else:
                diccionario = {'pais': str(x1[1].get_text()), 'oro': str(x2[2].get_text()), 'plata': str(
                    x2[3].get_text()), 'bronce': str(x2[4].get_text()), 'total': str(x2[5].get_text())}
                dataframe2 = pd.DataFrame(diccionario, columns=[
                                          'pais', 'oro', 'plata', 'bronce', 'total'], index=[i])
                dataframe = pd.concat([dataframe, dataframe2])
            i = i + 1

dataframe.index.name = 'id'
dataframe.to_csv("paises.csv")
