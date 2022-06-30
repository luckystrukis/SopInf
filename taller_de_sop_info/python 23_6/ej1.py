import pandas as pd
import seaborn as sns

df = pd.read_csv("pc-proy21-finxobjdelgasto.csv",sep=",", engine="python")
df = df.loc[0:5000]
grafico = sns.pairplot(df,hue="Crédito_2021",palette="Spectral")