import numpy as np
from matplotlib import pyplot as plt

TIMEFRAME               = 1
NR_OF_SAMPLES           = 1000
time = np.linspace(0, TIMEFRAME, NR_OF_SAMPLES)   

AMPLITUDE               = 1
CARRIER_FREQUENCY       = 20
PHASE                   = 0*np.pi
carrier = AMPLITUDE * np.sin(time*2*np.pi*CARRIER_FREQUENCY + PHASE) 

SIG_FREQUENCY           = 10
LOGIC_LVLS              = 2
signal = []
for i in range(SIG_FREQUENCY):
    signal += [np.random.randint(LOGIC_LVLS)/(LOGIC_LVLS-1)]*int(TIMEFRAME*NR_OF_SAMPLES/SIG_FREQUENCY)

modulated_carrier = carrier*signal

plt.figure(dpi=150)
plt.title('Signal')
plt.xlabel('time [s]')
plt.grid()
plt.plot(time, signal)
plt.show()

plt.figure(dpi=150)
plt.title('Carrier')
plt.xlabel('time [s]')
plt.grid()
plt.plot(time, carrier)
plt.show()

plt.figure(dpi=150)
plt.title('Modulated Carrier')
plt.xlabel('time [s]')
plt.grid()
plt.plot(time, modulated_carrier)
plt.show()

fig, axs = plt.subplots(3, dpi=150)
fig.suptitle('OOK modulation', fontsize=12)
axs[-1].set_xlabel('time [s]')
axs[0].set_title('Signal', fontsize=8)
axs[0].plot(time, signal)
axs[0].grid()
axs[1].set_title('Carrier', fontsize=8)
axs[1].plot(time, carrier)
axs[1].grid()
axs[2].set_title('Modulated Carrier', fontsize=8)
axs[2].plot(time, modulated_carrier)
axs[2].grid()
fig.tight_layout()
fig.show()

