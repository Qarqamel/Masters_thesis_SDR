import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot


def hpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(1, 2*cutoff_freq/sampling_freq,btype='highpass')
    return scipy.signal.filtfilt(b,a,samples)

LOW_FREQUENCY = 10
HIGH_FREQUENCY = 100
FILTER_CUTOFF_FREQUENCY = 80

time = np.linspace(0, 1, int(10e4))
low_freq_signal = np.sin(2*PI*LOW_FREQUENCY*time)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
signal = low_freq_signal + high_freq_signal
spectrum = np.fft.fft(signal)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)
filtered_signal = hpf(signal, FILTER_CUTOFF_FREQUENCY, 10e4)
spectrum_filt = np.fft.fft(filtered_signal)
spectrum_filt = spectrum_filt[0:len(spectrum_filt)//2]
spectrum_filt_abs = np.absolute(spectrum_filt)

RES=150
DISP_SPECTRUM_SIZE = 120

my_plot(time, {f'{LOW_FREQUENCY} Hz + {HIGH_FREQUENCY} Hz':signal}, res=RES)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.xticks(list(np.arange(0, 0.5, step=0.1)))
plt.xlim(0, 0.5)

my_plot(time, {f'{HIGH_FREQUENCY} Hz':filtered_signal}, styles = ['C1'], res=RES)
plt.ylim(-2.2,2.2)
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.xlabel('t')
plt.xticks(list(np.arange(0, 0.5, step=0.1)))
plt.xlim(0, 0.5)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_abs}, stem=True, res=RES)
plt.ylim(5000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10)) + [LOW_FREQUENCY, FILTER_CUTOFF_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = FILTER_CUTOFF_FREQUENCY, color = 'r', label = 'filter cutoff frequency', linestyle = '--', linewidth = 1)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)

fsamp = 10e2    # Number of coefficients.
coef_b, coef_a = scipy.signal.butter(1, 2*FILTER_CUTOFF_FREQUENCY/fsamp, btype='highpass')
freqs, response = scipy.signal.freqz(coef_b, coef_a, fs=fsamp, include_nyquist=True)
my_plot(freqs, {'Lowpass filter frequency response':response}, styles = ['C4'], res=RES)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10)) + [LOW_FREQUENCY, FILTER_CUTOFF_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = FILTER_CUTOFF_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_filt_abs}, styles = ['C1'], stem=True, res=RES)
plt.xlabel('f')
plt.ylim(5000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10)) + [LOW_FREQUENCY, FILTER_CUTOFF_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.axvline(x = FILTER_CUTOFF_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)
