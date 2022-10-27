from folium import Map,Marker
import pandas as pd

df = pd.read_csv("oferta_gastronomica.csv",sep=",",engine="python")

ubicaciones = []
nombres = []
cocinas = []
direcciones = []
telefonos = []
barrios = []

for index, row in df.iterrows():
    ubicaciones.append((row["lat"], row["long"]))
    nombres.append(row["nombre"].replace("`", "´"))
    cocinas.append(row["cocina"])
    direcciones.append(row["direccion_completa"])
    telefonos.append(row["telefono"])
    barrios.append(row["barrio"])

ubicacion_de_buenos_aires = [-34.603722, -58.381592]
mapa = Map(location=ubicacion_de_buenos_aires,
zoom_start=12 )
for i, coordenada in enumerate(ubicaciones):
    latitud = coordenada[0]
    longitud = coordenada[1]
    marcador = Marker( location=[latitud,longitud],
    popup=str(direcciones[i]) + " // " + str(telefonos[i]) + " // " + barrios[i],
    tooltip=nombres[i] + ", " + str(cocinas[i]))
    mapa.add_child(marcador)
mapa.save('mapa_con_ubicaciones.html')
