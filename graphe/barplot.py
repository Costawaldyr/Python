import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10,10)
y = 2 * x + 2
y_erros = np.random.rand(len(x)) * 2
colors = plt.cm.plasma(np.linspace(0, 1, len(x)))

plt.figure()
for i in range(len(x)):
    plt.errorbar(
        x[i], y[i], yerr = y_erros[i], fmt = '*', capsize= 5, color=colors[i], ecolor= colors[i],
        elinewidth=2, markersize=8
    )
plt.title('Colorful Error Bar Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()