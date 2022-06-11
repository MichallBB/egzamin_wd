import matplotlib.pyplot as plt

x = [35, 45, 15, 42, 41]
y = ['A', 'B', 'C', 'D', 'E']
x2 = [-30,-32,-37,-35,-31]

kolory = ["lightblue","pink", "darkorange", "darkgray", "purple"]
kolory2 = ["orchid","darkturquoise","darkturquoise","sienna", "olive"]

fig, axs = plt.subplots(1, 2, figsize=(7.5, 5.5))
axs[0].barh(y, x, align='center', color = kolory)
axs[1].barh(y, x2, color = kolory2)

axs[0].set_title('Wykres lewy')
axs[1].set_title('Wykres prawy')
plt.savefig('zad1.pdf', format='pdf')
plt.show()