import numpy as np
import scipy.signal
from matplotlib import pyplot as plt

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

signals_to_plot = {
                   'Rx': rx,
                   'Rectified': rectified,
                   'Envelope': envelope,
                   'Signal': signal
                   }

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('Rx/Rectified')
plt.plot(time, signals_to_plot['Rx'], linewidth = 2.5, label = 'Rx')
plt.plot(time, signals_to_plot['Rectified'], linewidth = 1, label = 'Rectified')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('Rectified/Envelope')
plt.plot(time, signals_to_plot['Rectified'], linewidth = 1.5, label = 'Rectified')
plt.plot(time, signals_to_plot['Envelope'], linewidth = 1, label = 'Envelope')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('Envelope/Signal')
plt.plot(time, signals_to_plot['Envelope'], linewidth = 1.5, label = 'Envelope')
plt.plot(time, signals_to_plot['Signal'], linewidth = 1, label = 'Signal')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()
