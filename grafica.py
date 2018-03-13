import numpy as np
import matplotlib.pyplot as plt

th= np.linspace(0,2*np.pi)
x= np.sin(th)
y= np.sin(x)

plt.plot(x,y)
plt.show()
plt.savefig('grafica1.png')
