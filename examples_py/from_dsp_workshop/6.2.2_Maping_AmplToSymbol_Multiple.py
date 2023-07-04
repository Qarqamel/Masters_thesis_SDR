import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

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

