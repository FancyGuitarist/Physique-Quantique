import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.constants as ct
from scipy.optimize import curve_fit



lamb = [ct.c/366,ct.c/405,ct.c/436,ct.c/492,ct.c/546,ct.c/579]
V = [1.48, 1.15, 0.93, 0.62, 0.36, 0.24]
def f(x, A, B): # this is your 'straight line' y=f(x)
    return A*x + B
popt, pcov = curve_fit(f, lamb, V) # your data x, y to fit
freq = np.linspace(lamb[0],lamb[5],500)
func = np.linspace(popt[0]*lamb[0]+popt[1],popt[0]*lamb[5]+popt[1],500)
print(popt)
plt.plot(lamb,V)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Tension (V)')
plt.savefig('Dev1Quant.png',dpi = 600)

