import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI

PAYLOAD                     = [0,1,1,0,1]
SAMPLES_PER_BIT             = 1000
CARRIER_PERIODS_PER_BITS    = 3

time = np.linspace(0, len(PAYLOAD), len(PAYLOAD)*SAMPLES_PER_BIT)
signal = []
for bit in PAYLOAD:
    signal += [bit]*SAMPLES_PER_BIT
carrier = np.sin(2*PI*CARRIER_PERIODS_PER_BITS*time)
tx = carrier*signal
np.save('AM_OOK_TxSignal', tx)

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

signals_to_plot = {'Payload':signal,
                   'Carrier':carrier,
                   'Tx':tx
                   }
for name, sig in signals_to_plot.items():
    plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6') #F4E8EB
    ax = plt.axes()
    ax.set_facecolor("#FAF4F6")
    plt.grid()
    plt.title(name)
    plt.plot(time, sig, label = name)
    plt.legend(loc = 'lower right', bbox_to_anchor=(1, -0.6))
    plt.show()
