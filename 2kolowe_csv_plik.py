import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nieruchomosci2.csv', sep=';', header=None, encoding='utf-8')
data = data.T

rynek_wtorny = data[data[0] == 'rynek wtórny']
rynek_pierwotny = data[data[0] == 'rynek pierwotny']

fig, ax = plt.subplots(2, 1, figsize=(5, 6.55))

ax[0].pie(rynek_pierwotny[3], labels=rynek_pierwotny[1], autopct='%1.1f%%', shadow=True)
ax[1].pie(rynek_wtorny[3], labels=rynek_wtorny[1], autopct='%1.1f%%', shadow=True, startangle=-20)
ax[0].set(title='Rynek pierwotny')
ax[1].set(title='Rynek wtórny')

plt.savefig('nieruchomosci.pdf', format='pdf')
plt.show()
