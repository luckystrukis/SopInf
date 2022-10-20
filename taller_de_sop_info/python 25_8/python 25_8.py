from io import StringIO
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

pagina = requests.get("https://datos.gob.ar/dataset/cultura-mapa-cultural-agentes-actividades-culturales/archivo/cultura_0d1b731b-28c9-4402-a7eb-018c9cf8958b")

objeto_sopa = BeautifulSoup(pagina.content, 'html.parser')

e1 = objeto_sopa.find_all("a", {"class": "btn-green"})

print(e1)
"""
csv = requests.get("https://datos.cultura.gob.ar/dataset/0560ef96-55ca-4026-b70a-d638e1541c05/resource/0d1b731b-28c9-4402-a7eb-018c9cf8958b/download/diario_impreso.csv").text

ruta_base = Path.cwd()
ruta_completa = Path(ruta_base, "python 25_8", "nombre_ejemplo.csv")
df = pd.read_csv(StringIO(str(pagina)), sep=  ",")
df.to_csv("ej.csv", index=False)
"""