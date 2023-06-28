import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot


def bpf(samples, cutoff_freq_l, cutoff_freq_h, sampling_freq):
    b, a = scipy.signal.butter(2, [2*cutoff_freq_l/sampling_freq,
                                   2*cutoff_freq_h/sampling_freq],
                               btype='bandpass')
    return scipy.signal.filtfilt(b,a,samples)

LOW_FREQUENCY = 0
MIDDLE_FREQUENCY = 10
HIGH_FREQUENCY = 100
FILTER_BANDSTART_FREQUENCY = 5
FILTER_BANDSTOP_FREQUENCY = 15

time = np.linspace(0, 1, int(10e4))
low_freq_signal = np.cos(2*PI*LOW_FREQUENCY*time)
mid_freq_signal = np.sin(2*PI*MIDDLE_FREQUENCY*time)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
signal = low_freq_signal + mid_freq_signal + high_freq_signal
spectrum = np.fft.fft(signal)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)
filtered_signal = bpf(signal,
                      FILTER_BANDSTART_FREQUENCY,
                      FILTER_BANDSTOP_FREQUENCY,
                      10e4)
spectrum_filt = np.fft.fft(filtered_signal)
spectrum_filt = spectrum_filt[0:len(spectrum_filt)//2]
spectrum_filt_abs = np.absolute(spectrum_filt)

RES=150
DISP_SPECTRUM_SIZE = 120
TIME_LIM = 0.5

my_plot(time, {f'{LOW_FREQUENCY} Hz + {MIDDLE_FREQUENCY} Hz + {HIGH_FREQUENCY} Hz':signal}, res=RES)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.xticks(list(np.arange(0, TIME_LIM, step=TIME_LIM/5)))
plt.xlim(0, TIME_LIM)
plt.yticks(list(np.arange(-2, 4, step=1)))

my_plot(time, {f'{MIDDLE_FREQUENCY} Hz':filtered_signal}, styles = ['C1'], res=RES)
plt.ylim(-2.2,2.2)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlabel('t')
plt.xticks(list(np.arange(0, TIME_LIM, step=TIME_LIM/5)))
plt.xlim(0, TIME_LIM)
plt.yticks(list(np.arange(-2, 4, step=1)))

freqs = np.linspace(0, 10e4/2, int(10e4/2))
spectrum_abs[0] = spectrum_abs[0]/2
my_plot(freqs, {'':spectrum_abs}, stem=True, res=RES)
plt.ylim(7000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=50)) + [LOW_FREQUENCY, FILTER_BANDSTART_FREQUENCY, MIDDLE_FREQUENCY, FILTER_BANDSTOP_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = FILTER_BANDSTART_FREQUENCY, color = 'r', label = 'filter cutoff frequency', linestyle = '--', linewidth = 1)
plt.axvline(x = FILTER_BANDSTOP_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)

fsamp = 10e2
coef_b, coef_a = scipy.signal.butter(1, [2*FILTER_BANDSTART_FREQUENCY/fsamp, 2*FILTER_BANDSTOP_FREQUENCY/fsamp], btype='bandpass')
freqs, response = scipy.signal.freqz(coef_b, coef_a, fs=fsamp, include_nyquist=True)
my_plot(freqs, {'Bandpass filter frequency response':response}, styles = ['C4'], res=RES)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=50)) + [LOW_FREQUENCY, FILTER_BANDSTART_FREQUENCY, MIDDLE_FREQUENCY, FILTER_BANDSTOP_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = FILTER_BANDSTART_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)
plt.axvline(x = FILTER_BANDSTOP_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_filt_abs}, styles = ['C1'], stem=True, res=RES)
plt.xlabel('f')
plt.ylim(7000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=50)) + [LOW_FREQUENCY, FILTER_BANDSTART_FREQUENCY, FILTER_BANDSTOP_FREQUENCY, HIGH_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.axvline(x = FILTER_BANDSTART_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)
plt.axvline(x = FILTER_BANDSTOP_FREQUENCY, color = 'r', linestyle = '--', linewidth = 1)
