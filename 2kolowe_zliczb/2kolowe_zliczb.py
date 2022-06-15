import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wykres1 = [15.7, 25.6, 16.9, 21.5, 12.8, 7.6]
wykres2 = [20.4, 17.6, 9.7, 19.9, 15.7, 16.7]
oznaczenie = ['A', 'B', 'C', 'D', 'E', 'F']
explode = [0, 0.15, 0, 0, 0, 0]
kolory = ['tab:brown','tab:pink','wheat','lime','tab:brown','cornflowerblue']

fig, ax = plt.subplots(2,2, figsize=(6.4,4.8))
ax[0,0].axis('off')
ax[0,1].pie(wykres1, explode=explode, labels=oznaczenie, autopct='%1.1f%%', startangle=40, colors=kolory, radius=1.2)
ax[0,1].set(title='Prawo ''Góra')
ax[1,0].pie(wykres2, explode=explode, labels=oznaczenie, autopct='%1.1f%%', startangle=35, colors=kolory, radius=1.2)
ax[1,0].set(title='Lewo Dół')
ax[1,1].axis('off')
plt.savefig('zad1.png', format='png')
plt.show()