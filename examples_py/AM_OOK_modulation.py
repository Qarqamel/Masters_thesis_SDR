import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

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

signals_to_plot = {'Payload':signal,
                   'Carrier':carrier,
                   'Tx':tx
                   }

my_plot(time, {'Carrier':carrier, 'Payload':signal}, leg_ncol = 2)
plt.show()

my_plot(time, {'Tx':tx})
plt.show()
