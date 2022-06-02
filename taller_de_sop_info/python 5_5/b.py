import pandas as pd
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

df = pd.read_csv("tasa-mortalidad-infantil-deis-1990-2020.csv",sep=",", engine="python")
print (df.keys())
df = df.loc[0:8619]
df = df.groupby('indice_tiempo')['mortalidad_infantil_argentina'].sum()
x_values = df.keys()
y_values = df.values
plt1.xticks(rotation = 90, fontsize = 10)

# gráfico 1
plt1.bar(x_values,y_values)
plt1.title('Mortalidad Infantil')
plt1.xlabel('Indice Tiempo')
plt1.ylabel('Mortalidad Infantil Argentina')
plt1.show()

plt2.plot(x_values,y_values);
plt2.title('Mortalidad Infantil')
plt2.xlabel('Indice Tiempo')
plt2.ylabel('Mortalidad Infantil Argentina')
plt2.show()