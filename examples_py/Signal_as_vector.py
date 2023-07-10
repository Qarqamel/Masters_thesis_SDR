import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot
import string

def arb_function(x):
    return -1/3*np.sin(x) - 1/4*np.sin(2*x)

angles = np.linspace(-4, 4, 1001)
arb_func = [arb_function(ang) for ang in angles]

angles_samp = angles[0::100]
arb_func_samp = arb_func[0::100]

RES = 100

# plt.rcParams.update({'axes.facecolor':'#FAF4F6'})
plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
plt.rc('font', family='Arial')

plt.figure(figsize = [6.4, 3.2], dpi=RES)
plt.plot(angles, arb_func, 'C0-')
plt.plot(angles_samp, arb_func_samp, 'C0o')
plt.axhline(y=0,color='black', linewidth=0.8)
plt.xticks(ticks = angles_samp, labels=list(string.ascii_uppercase)[:11], color='red', weight='bold')
plt.xlabel('Współrzędne wektora')
plt.grid()