import pandas as pd
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

df = pd.read_csv("pc-proy21-finxobjdelgasto.csv",sep=",", engine="python")
print (df.keys())
df = df.loc[0:8619]
df = df.groupby('Descripción Jurisdicción')['Crédito 2021'].sum().astype(float)/10000000000
x_values = df.keys()
y_values = df.values
plt1.xticks(rotation = 90, fontsize = 10)

# gráfico 1
plt1.bar(x_values,y_values)
plt1.title('Presupuesto 2021')
plt1.xlabel('Descripción Jurisdicción')
plt1.ylabel('Crédito 2021(Mil MM)')
plt1.show()

plt2.plot(x_values,y_values);
plt2.title('Presupuesto 2021')
plt2.xlabel('Descripción Jurisdicción')
plt2.ylabel('Crédito 2021(Mil MM)')
plt2.show()