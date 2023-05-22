import numpy as np
import scipy.signal
from matplotlib import pyplot as plt

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

TIME                        = 6
SAMPLING_FREQUENCY          = 1000
FILTER_CUTOFF_FREQUENCY     = 5
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

signals_to_plot = {
                   'Rx': rx,
                   'Rectified': rectified,
                   'Envelope': envelope,
                   'Signal': signal
                   }
for name, sig in signals_to_plot.items():
    plt.figure(figsize = [6.4,1.6], dpi=150)
    # plt.title(name, fontsize=6)
    plt.grid()
    plt.plot(time, sig, label = name)
    plt.legend(fontsize = 6, loc = 'lower right')
    plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, signals_to_plot['Rx'], linewidth = 2.5, label = 'Rx')
plt.plot(time, signals_to_plot['Rectified'], linewidth = 1, label = 'Rectified')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, signals_to_plot['Rectified'], linewidth = 1.5, label = 'Rectified')
plt.plot(time, signals_to_plot['Envelope'], linewidth = 1, label = 'Envelope')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, signals_to_plot['Envelope'], linewidth = 1.5, label = 'Envelope')
plt.plot(time, signals_to_plot['Signal'], linewidth = 1, label = 'Signal')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, signals_to_plot['Rx'], linewidth = 3, label = 'Rx')
plt.plot(time, signals_to_plot['Rectified'], linewidth = 1, label = 'Rectified')
plt.plot(time, signals_to_plot['Envelope'], linewidth = 1, label = 'Envelope')
plt.plot(time, signals_to_plot['Signal'], linewidth = 1, label = 'Signal')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()