import pandas as pd
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

# gráfico 1
a = "Esta al tanto de la situacion economica del pais?"
df = (pd.read_csv("Formulario sin título.csv",sep=",", engine="python"))
df.set_index("Conoce usted el teorema de imposibilidad de Arrow?")
df = df.loc[df[a] == "Si"]
df = df.groupby("Conoce usted el teorema de imposibilidad de Arrow?")[a].count()
x_values = df.keys()
y_values = df.values

plt1.bar(x_values,y_values)
plt1.title('sí esta al tanto de la situacion economica del pais')
plt1.xlabel('Conoce usted el teorema de imposibilidad de Arrow?', fontsize = 15)
plt1.ylabel('Cantidad', fontsize = 15)
plt1.show()

# gráfico 2
a = "Esta al tanto de la situacion economica del pais?"
df2 = pd.read_csv("Formulario sin título.csv",sep=",", engine="python")
df2.set_index("Que opina del liberalismo?")
df2 = df2.loc[df2[a] == "Si"]
df2 = df2.groupby("Que opina del liberalismo?")[a].count()
x_values = df2.keys()
y_values = df2.values

plt2.bar(x_values,y_values)
plt2.title('Que opina sobre el liberalismo la gente que esta al tanto de la situación del pais')
plt2.xlabel('Que opina del liberalismo', fontsize = 15)
plt2.ylabel('Cantidad', fontsize = 15)
plt2.show()
