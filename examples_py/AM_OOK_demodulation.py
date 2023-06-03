import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

TIME                        = 5
SAMPLING_FREQUENCY          = 1000
FILTER_CUTOFF_FREQUENCY     = 3
ADC_THRESHOLD               = 0.5

time = np.linspace(0, TIME, TIME*SAMPLING_FREQUENCY)
rx = np.load('AM_OOK_TxSignal.npy')
rectified = np.absolute(rx)
envelope = lpf(rectified, FILTER_CUTOFF_FREQUENCY, SAMPLING_FREQUENCY)
signal = []
for sample in envelope:
    if sample > ADC_THRESHOLD:
        signal.append(1)
    else:
        signal.append(0)

RES = 150

signals_to_plot = {
                   'Rx': rx,
                   'Rectified': rectified,
                   'Envelope': envelope,
                   'Signal': signal
                   }

my_plot(time, {'Rx':rx, 'Rectified':rectified}, [2.5, 1], ['tab:blue', 'tab:olive'],leg_ncol = 2, res = RES)

my_plot(time, {'Rectified':rectified, 'Envelope':envelope}, [1.5, 1], ['tab:olive', 'tab:purple'], leg_ncol = 2, res = RES)

treshold_line = [ADC_THRESHOLD]*TIME*SAMPLING_FREQUENCY
my_plot(time, {'Envelope':envelope, 'Signal':signal, 'Threshold':treshold_line},
              [1.5, 1, 1],
              ['tab:purple', 'tab:orange', 'r--'],
              leg_ncol = 3, res = RES)
