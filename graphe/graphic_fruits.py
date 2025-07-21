import numpy as np 
import matplotlib.pyplot as plt 

categories = ['Apples', 'Bananas', 'cherries', 'Dates', 'Elderberries']
values = [25, 40, 35, 30, 50]

colors = plt.cm.viridis(np.linspace(0,1,len(categories)))

plt.bar(categories,values,color=colors)
plt.title('Colored Bar graphic fruits')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()