import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI

PAYLOAD                     = [1,0,1,0,1,1]
SAMPLES_PER_BIT             = 1000
CARRIER_PERIODS_PER_BITS    = 5
time = np.linspace(0, len(PAYLOAD), len(PAYLOAD)*SAMPLES_PER_BIT)
signal = []
for bit in PAYLOAD:
    signal += [bit]*SAMPLES_PER_BIT
carrier = np.sin(2*PI*CARRIER_PERIODS_PER_BITS*time)
tx = carrier*signal
np.save('AM_OOK_TxSignal', tx)

signals_to_plot = {'Payload':signal,
                   'Carrier':carrier,
                   'Tx':tx
                   }
for name, sig in signals_to_plot.items():
    plt.figure(figsize = [6.4,1.6], dpi=150)
    # plt.title(name, fontsize=6)
    plt.grid()
    plt.plot(time, sig)
    plt.show()
