from io import StringIO
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

"""
diarios
https://datos.gob.ar/dataset/cultura-mapa-cultural-agentes-actividades-culturales/archivo/cultura_0d1b731b-28c9-4402-a7eb-018c9cf8958b
editoriales
https://datos.gob.ar/dataset/cultura-mapa-cultural-agentes-actividades-culturales/archivo/cultura_2bcb7ee9-1c75-4a37-adec-2e8c822d2e3d
cine
https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_f7a8edb8-9208-41b0-8f19-d72811dcea97
"""


def ObtenerPagina(pagina):
    link = requests.get(pagina)

    objeto_sopa = BeautifulSoup(link.content, 'html.parser')

    return objeto_sopa.find("a", {"class": "btn-green"}).get("href")


"""
for x in range(3):
    print("de que pagina quiere el dataset:")
    pagina = input()
    print("nombre para el dataset:")
    nombre = input()
    csv = requests.get(ObtenerPagina(pagina)).text

    ruta_base = Path.cwd()
    ruta_completa = str(
        str(ruta_base) + "/taller_de_sop_info/python25_8/" + nombre + ".csv")
    df = pd.read_csv(StringIO(str(csv)), sep=",")
    df.to_csv(ruta_completa, index=False)
"""
ruta_base = Path.cwd()
ruta_completa = str(
    str(ruta_base) + "/taller_de_sop_info/python25_8/")
cines = pd.read_csv(ruta_completa + "cines.csv", sep=",", engine="python")
editoriales = pd.read_csv(
    ruta_completa + "editoriales.csv", sep=",", engine="python")
diarios = pd.read_csv(ruta_completa + "diarios.csv", sep=",", engine="python")

diccionariocines = {'Cod_Loc': cines["cod_localidad"], 'IdProvincia': cines["id_provincia"], 'IdDepartamento': cines["id_departamento"], 'Categoria': cines["categoria"],
                    'Provincia': cines["provincia"], 'Localidad': cines["localidad"], 'Nombre': cines["nombre"], 'Domicilio': cines["direccion"], 'CP': cines["cp"], 'Web': cines["web"]}
diccionarioeditoriales = {'Cod_Loc': editoriales["Cod_Loc"], 'IdProvincia': editoriales["IdProvincia"], 'IdDepartamento': editoriales["IdDepartamento"], 'Categoria': editoriales["CategorÃ­a"], 'Provincia': editoriales["Provincia"],
                          'Localidad': editoriales["Localidad"], 'Nombre': editoriales["Nombre"], 'Domicilio': editoriales["Domicilio"], 'CP': editoriales["CP"], 'Telefono': editoriales["TelÃ©fono"], 'Mail': editoriales["Mail"], 'Web': editoriales["Web"]}
diccionariodiarios = {'Cod_Loc': diarios["Cod_Loc"], 'IdProvincia': diarios["IdProvincia"], 'IdDepartamento': diarios["IdDepartamento"], 'Categoria': diarios["CategorÃ­a"], 'Provincia': diarios["Provincia"],
                      'Localidad': diarios["Localidad"], 'Nombre': diarios["Nombre"], 'Domicilio': diarios["Domicilio"], 'CP': diarios["CP"], 'Telefono': diarios["TelÃ©fono"], 'Mail': diarios["Mail"], 'Web': diarios["Web"]}
dataframecines = pd.DataFrame(
    diccionariocines, columns=['Cod_Loc', "IdProvincia", "IdDepartamento", "Categoria", "Provincia", "Localidad", "Nombre", "Domicilio", "CP", "Telefono", "Mail", "Web"])
dataframeeditoriales = pd.DataFrame(
    diccionarioeditoriales, columns=['Cod_Loc', "IdProvincia", "IdDepartamento", "Categoria", "Provincia", "Localidad", "Nombre", "Domicilio", "CP", "Telefono", "Mail", "Web"])
dataframediarios = pd.DataFrame(
    diccionariodiarios, columns=['Cod_Loc', "IdProvincia", "IdDepartamento", "Categoria", "Provincia", "Localidad", "Nombre", "Domicilio", "CP", "Telefono", "Mail", "Web"])

dataframefinal = pd.concat(
    [dataframecines, dataframeeditoriales, dataframediarios])

dataframefinal.to_csv(ruta_completa + "final.csv", index=False)
df2 = dataframefinal[(dataframefinal["Categoria"] == "Editoriales de Libros")]

Diarios =  dataframediarios.groupby('Provincia').count()
Diarios = Diarios[['Categoria']]
Diarios.columns = ['Diarios']

Editoriales =  dataframeeditoriales.groupby('Provincia').count()
Editoriales = Editoriales[['Categoria']]
Editoriales.columns = ['Editoriales']


cines =  dataframecines.groupby('Provincia').count()
cines2 = cines[['Categoria']]
cines2.columns = ['cines']

finalfinal = pd.concat([Editoriales, Diarios, cines2])
print(finalfinal)
