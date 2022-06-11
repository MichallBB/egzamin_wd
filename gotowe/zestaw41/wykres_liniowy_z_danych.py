import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('ceny2.xlsx')
srednia_cena_produktow = data.groupby(["Rodzaje towarów"]).mean()
print(srednia_cena_produktow)

monka = data[data["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
ryz = data[data["Rodzaje towarów"] == "ryż - za 1kg"]

fig, axs = plt.subplots()
axs.plot(monka["Rok"], monka["Wartość"], color='red', label='Mąka pszenna - za 1kg')
axs.plot(ryz["Rok"], ryz["Wartość"], color='green', label='Ryż - za 1kg')
axs.set(ylabel = 'Wartość w zł', xlabel="Rok", title='Zmiany cen produktów')
axs.annotate("55555", xy=(2009.7, 1.83))
axs.legend()
plt.savefig('wykres.jpg', format='jpg')
plt.show()