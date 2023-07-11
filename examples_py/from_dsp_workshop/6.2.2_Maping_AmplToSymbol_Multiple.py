import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol
from auxiliary_lib import my_plot

plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
plt.rc('font', family='Arial')

RES = 100

# PRESENTATION  
plt.figure(figsize = [6.4, 2.4], dpi=RES)

for symbol_nr in 2,4,8:
    amplitudes_l = np.linspace(-1.5, 1.5, 100)
    symbol_l = list()
    for amp in amplitudes_l:
        symbol = ampl_to_symbol(symbol_nr,amp)
        symbol_l.append(symbol)    
    plt.plot(amplitudes_l,symbol_l,'p-', label=f'symbol nr = {symbol_nr}')    

plt.legend()      
plt.grid()
plt.xlabel('Amplitude')
plt.ylabel('Symbol')

