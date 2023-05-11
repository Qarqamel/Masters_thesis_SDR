import numpy as np
from matplotlib import pyplot as plt

AMPLITUDE       = [1, 2, 4]
FREQUENCY       = [10, 20, 50]
PHASE           = [0, np.pi/2, np.pi]

time = np.linspace(0, 1, 1000)

fig, axs = plt.subplots(3, dpi=150)
fig.suptitle('Sinewaves', fontsize=12)
axs[-1].set_xlabel('time [s]')
for grph, amp in zip(axs, AMPLITUDE):
    sinewave = amp * np.sin((time*2*np.pi*FREQUENCY[0] + PHASE[0]))    
    grph.set_title(f'amplitude = {amp}', fontsize=8)
    grph.set_ylim([-5, 5])    
    grph.grid()
    grph.plot(time, sinewave)
fig.tight_layout()
fig.show()

fig, axs = plt.subplots(3, dpi=150)
fig.suptitle('Sinewaves', fontsize=12)
axs[-1].set_xlabel('time [s]')
for grph, freq in zip(axs, FREQUENCY):
    sinewave = AMPLITUDE[0] * np.sin((time*2*np.pi*freq + PHASE[0]))    
    grph.set_title(f'frequency = {freq} Hz', fontsize=8)  
    grph.grid()
    grph.plot(time, sinewave)
fig.tight_layout()
fig.show()

fig, axs = plt.subplots(3, dpi=150)
fig.suptitle('Sinewaves', fontsize=12)
axs[-1].set_xlabel('time [s]')
for grph, phs in zip(axs, PHASE):
    sinewave = AMPLITUDE[0] * np.sin((time*2*np.pi*FREQUENCY[0] + phs))    
    grph.set_title(f'phase = {phs/np.pi}π', fontsize=8) 
    grph.grid()
    grph.plot(time, sinewave)
fig.tight_layout()
fig.show()