import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fecha_manchas.dat")
time= data[:,0]
manchas = data[:,1]






plt.plot(time, manchas, color = 'k')

plt.xlabel("Time (anos)")
plt.ylabel("Manchas solares")
plt.title("Tiempo s. Manchas Solares")
plt.savefig("fecha_manchas.pdf")

