
import pandas as pd
barrios = pd.read_csv("contenido/barrios.csv", sep=",", engine="python")
comunas = pd.read_csv("contenido/comunas.csv", sep=",", engine="python")
casos = pd.read_csv("contenido/casos.csv", sep=",", engine="python")

# 1

barrioscomuna3 = barrios[barrios.comuna == 3]
print(barrioscomuna3[["barrio", "area", "perimetro"]])


# 2

barrioscomuna4y10 = barrios[(barrios.comuna > 4) & (barrios.comuna < 10)]

print(barrioscomuna4y10[["barrio", "area", "perimetro"]])


# 3

comunabarrioindice5 = barrios[["comuna"]].iat[5,0]
condicion = comunas.COMUNAS == comunabarrioindice5
print(comunas[["AREA", "PERIMETRO"]][condicion])

# 4

barriosconv = comunas[comunas.BARRIOS.str.startswith("V")]
print(barriosconv["COMUNAS"])

# 5

barrioscona = comunas[comunas.BARRIOS.str.contains("A")]
print(barrioscona["AREA"])

# 6

comunacasoindice15 = casos[["comuna"]].iat[15,0]
condicion = comunas.COMUNAS == comunacasoindice15
print(comunas[["PERIMETRO"]][condicion])

# 7

barriocasoindice15 = casos[["barrio"]].iat[7,0]
condicion = barrios.barrio == barriocasoindice15
print(barrios[["area"]][condicion])

# 8

barrioscasosmenor6y7 = casos["barrio"][(casos.numero_de_caso > 6000000) & (casos.numero_de_caso < 7000000)].dropna().drop_duplicates().tolist()
condicion = barrios.barrio.isin(barrioscasosmenor6y7)
print(barrios[["barrio", "comuna"]][condicion])
print(barrios[condicion].index)

#9

barrioindice3 = barrios[["barrio"]].iat[3,0]
condicion = casos.barrio == barrioindice3
print(casos[["genero", "edad"]][condicion])

#10

barrioseninvestigacion = casos["barrio"][casos.tipo_contagio == "En Investigación"].dropna().drop_duplicates().tolist()
condicion = barrios.barrio.isin(barrioseninvestigacion)
print(barrios[["barrio"]][condicion])
print(barrios[condicion].index)

#11

barrioscasosmenoredad= casos["barrio"][casos.edad < 18].dropna().drop_duplicates().tolist()
condicion = barrios.barrio.isin(barrioscasosmenoredad)
print(barrios[["nombre"]][condicion])
print(barrios[condicion].index)

#12

barriosmenoracuatro = barrios["barrio"][barrios.index <= 4].dropna().drop_duplicates().tolist()
condicion = casos.barrio.isin(barriosmenoracuatro)
print(casos[["numero_de_caso", "genero", "edad"]][condicion])
print(casos[condicion].index)

#13

barriosmenoracuatro = barrios["barrio"][barrios.index != 13].dropna().drop_duplicates().tolist()
condicion = casos.barrio.isin(barriosmenoracuatro)
print(casos[["numero_de_caso", "genero", "edad"]][condicion])
print(casos[condicion].index)
