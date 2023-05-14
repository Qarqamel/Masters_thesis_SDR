import numpy as np
from matplotlib import pyplot as plt
from numpy import sin
from numpy import pi as PI

PAYLOAD                 = [0,1,0,1,1,0,0,1,0,1,1,1]
SAMPLES_PER_BIT         = 1000
signal = []
for bit in PAYLOAD:
    signal += [bit]*SAMPLES_PER_BIT

time = np.arange(0, len(PAYLOAD), 1/SAMPLES_PER_BIT)  

CARRIER_AMPLITUDE       = 1
CARRIER_FREQUENCY       = 5
carrier =  CARRIER_AMPLITUDE * sin(2*PI*CARRIER_FREQUENCY*time)

tx = carrier*signal

signals_to_plot = {'Payload':signal,
                   'Carrier':carrier,
                   'Tx':tx
                   }

for name, sig in signals_to_plot.items():
    plt.figure(dpi=150)
    plt.title(name)
    plt.grid()
    plt.plot(time, sig)
    plt.show()
