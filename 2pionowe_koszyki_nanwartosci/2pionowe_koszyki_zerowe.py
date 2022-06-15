import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('cechy51.csv', sep=';', encoding='utf-8', decimal=',')
data = data.fillna(0)

koszyk = np.arange(0, 250, 50)
data['cecha1-1'] = pd.cut(data.Cecha1, koszyk, include_lowest=True, labels=False)
data['cecha2-1'] = pd.cut(data.Cecha2, koszyk, include_lowest=True, labels=False)

ilosc_dla_cechy1 = data.value_counts(subset='cecha1-1').sort_index()
ilosc_dla_cechy2 = data.value_counts(subset='cecha2-1').sort_index()

label = ['[0,50]', '(50,100]', '(100,150]', '(150,200]']
x = np.arange(len(ilosc_dla_cechy1))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].bar(x, ilosc_dla_cechy1, edgecolor='black', color=['orchid', 'deepskyblue', 'yellowgreen', 'lightsalmon'])
ax[0].set_xticks(x, label)
ax[0].set(title='Wykres cechy 1', xlabel='Koszyki', ylabel='Ilość liczb z danego koszyka')

ax[1].bar(x, ilosc_dla_cechy2, edgecolor='black', color=['firebrick', 'khaki', 'darkslategray', 'darkorchid'])
ax[1].set_xticks(x, label)
ax[1].set(title='Wykres cechy 2', xlabel='Koszyki', ylabel='Ilość liczb z danego koszyka')

plt.savefig('2pionowe_koszyki_zerowe.pdf', format='pdf')
plt.show()
