import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot


def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

SIGNAL_FREQUENCY = 10
ALIAS_FREQUENCY = 100

time = np.linspace(0, 1, int(10e4))
signal = np.sin(2*PI*SIGNAL_FREQUENCY*time)
alias = np.sin(2*PI*ALIAS_FREQUENCY*time)
sum_signal = signal + alias
spectrum_sum = np.fft.fft(sum_signal)
spectrum_sum = spectrum_sum[0:len(spectrum_sum)//2]
spectrum_sum_abs = np.absolute(spectrum_sum)
filt_sine = lpf(sum_signal, 20, 10e4)
spectrum_filt = np.fft.fft(filt_sine)
spectrum_filt = spectrum_filt[0:len(spectrum_filt)//2]
spectrum_filt_abs = np.absolute(spectrum_filt)

RES = 150

my_plot(time, {'signal (10Hz) + potential alias (100Hz)':sum_signal}, res=RES)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'dft':spectrum_sum_abs}, stem=True, res=RES)
plt.xlabel('frequency')
plt.ylim(0,60000)
plt.xlim(0, 120)
plt.xticks(np.arange(0,120, step=10))

my_plot(time, {'Signal with alias fileterd out':filt_sine}, res=RES)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'dft':spectrum_filt_abs}, stem=True, res=RES)
plt.xlabel('frequency')
plt.ylim(0,60000)
plt.xlim(0, 120)
plt.xticks(np.arange(0,120, step=10))