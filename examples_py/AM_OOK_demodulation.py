import numpy as np
from matplotlib import pyplot as plt
from numpy import sin, absolute
from numpy import pi as PI
from scipy.signal import butter, filtfilt

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return filtfilt(b,a,samples)

# modulation    
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

# demodulation
rx = tx

rectified = absolute(rx)

envelope = lpf(rectified, CARRIER_FREQUENCY, SAMPLES_PER_BIT)

rcvd_signal = [0 if s<0.5 else 1 for s in envelope]

signals_to_plot = {'Payload':signal,
                   'Carrier':carrier,
                   'Tx':tx,
                   'Rx':rx,
                   'Rectified':rectified,
                   'Envelope':envelope,
                   'Received Payload': rcvd_signal
                   }

for name, sig in signals_to_plot.items():
    plt.figure(dpi=150)
    plt.title(name)
    plt.grid()
    plt.plot(time, sig)
    plt.show()
