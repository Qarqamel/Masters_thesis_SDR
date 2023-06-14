import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot


def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(1, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

SIGNAL_FREQUENCY = 10
ALIAS_FREQUENCY = 55
SAMPLING_FREQUENCY = 50
FILTER_CUTOFF_FREQUENCY = 20

time = np.linspace(0, 1, int(10e4))
signal = np.sin(2*PI*SIGNAL_FREQUENCY*time)
alias = np.sin(2*PI*ALIAS_FREQUENCY*time)
sum_signal = signal + alias
spectrum_sum = np.fft.fft(sum_signal)
spectrum_sum = spectrum_sum[0:len(spectrum_sum)//2]
spectrum_sum_abs = np.absolute(spectrum_sum)
time_samples = np.linspace(0, 1-(1/SAMPLING_FREQUENCY), SAMPLING_FREQUENCY)
sum_sig_samples = sum_signal[0::int(10e4/SAMPLING_FREQUENCY)]
spectrum_samp = np.fft.fft(sum_sig_samples)
spectrum_samp = spectrum_samp[0:len(spectrum_samp)//2+1]
spectrum_samp_abs = np.absolute(spectrum_samp)
filt_sine = lpf(sum_signal, FILTER_CUTOFF_FREQUENCY, 10e4)
spectrum_filt = np.fft.fft(filt_sine)
spectrum_filt = spectrum_filt[0:len(spectrum_filt)//2]
spectrum_filt_abs = np.absolute(spectrum_filt)
sum_sig_filt_samples = filt_sine[0::int(10e4/SAMPLING_FREQUENCY)]
spectrum_samp_filt = np.fft.fft(sum_sig_filt_samples)
spectrum_samp_filt = spectrum_samp_filt[0:len(spectrum_samp_filt)//2+1]
spectrum_samp_filt_abs = np.absolute(spectrum_samp_filt)

RES = 150
DISP_SPECTRUM_SIZE = 70
TIME_LIM = 0.6

wrong_sig = np.sin(2*PI*SIGNAL_FREQUENCY*time) + np.sin(2*PI*abs(ALIAS_FREQUENCY-SAMPLING_FREQUENCY)*time)

my_plot([time, time_samples, time], {f'signal ({SIGNAL_FREQUENCY}Hz) + potential alias ({ALIAS_FREQUENCY}Hz)':sum_signal,
                                     f'samples (fs = {SAMPLING_FREQUENCY}Hz)':sum_sig_samples,
                                     '':wrong_sig},
        styles = ['C0', 'C1.', 'C1--'],
        line_widths = [1.5, 0.5, 0.5],
        res=RES, leg_ncol=3)
plt.ylim(-2.2,2.2)
plt.xlim(0, TIME_LIM)
plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.xlabel('t')

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_sum_abs}, stem=True, res=RES)
plt.ylim(5000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY, ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = SAMPLING_FREQUENCY/2, color = 'r', label = 'sampling frequency/2', linestyle = '--', linewidth = 1)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)

spectrum_samp_abs = list(spectrum_samp_abs)+ [0]*(DISP_SPECTRUM_SIZE - len(spectrum_samp_abs))
freqs = np.linspace(0, DISP_SPECTRUM_SIZE, DISP_SPECTRUM_SIZE)
my_plot(freqs, {'':spectrum_samp_abs}, styles = ['C1'], stem=True, res=RES)
plt.xlabel('f')
plt.ylim(2,30)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY, abs(ALIAS_FREQUENCY-SAMPLING_FREQUENCY), ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.axvline(x = SAMPLING_FREQUENCY/2, color = 'r', label = '', linestyle = '--', linewidth = 1)

my_plot([time, time, time_samples],
        {f'Signal ({SIGNAL_FREQUENCY}Hz) + alias ({ALIAS_FREQUENCY}Hz)':sum_signal,
         'Fileterd signal':filt_sine,
         f'Samples (fs = {SAMPLING_FREQUENCY}Hz)':sum_sig_filt_samples},
        styles = ['C0', 'C2', 'C1.'],
        res=RES,
        leg_ncol=3)
plt.xlim(0, TIME_LIM)
plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_sum_abs}, stem=True, res=RES)
plt.ylim(5000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY, ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2, FILTER_CUTOFF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = SAMPLING_FREQUENCY/2, color = 'r', label = 'sampling frequency/2', linestyle = '--', linewidth = 1)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)

fsamp = 10e2
coef_b, coef_a = scipy.signal.butter(1, 2*FILTER_CUTOFF_FREQUENCY/fsamp, btype='lowpass')
freqs, response = scipy.signal.freqz(coef_b, coef_a, fs=fsamp, include_nyquist=True)
my_plot(freqs, {'Lowpass filter frequency response':response}, styles = ['C4'], res=RES)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10)) + [SIGNAL_FREQUENCY, ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2, FILTER_CUTOFF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)

freqs = np.linspace(0, 10e4/2, int(10e4/2))
my_plot(freqs, {'':spectrum_filt_abs}, styles = ['C2'], stem=True, res=RES)
plt.ylim(5000,60000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY, ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2, FILTER_CUTOFF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.axvline(x = SAMPLING_FREQUENCY/2, color = 'r', label = '', linestyle = '--', linewidth = 1)

spectrum_samp_filt_abs = list(spectrum_samp_filt_abs)+ [0]*(DISP_SPECTRUM_SIZE - len(spectrum_samp_filt_abs))
freqs = np.linspace(0, DISP_SPECTRUM_SIZE, DISP_SPECTRUM_SIZE)
my_plot(freqs, {'':spectrum_samp_filt_abs}, styles = ['C1'], stem=True, res=RES)
plt.xlabel('f')
plt.ylim(2,30)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+[SIGNAL_FREQUENCY, ALIAS_FREQUENCY, SAMPLING_FREQUENCY/2, FILTER_CUTOFF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.axvline(x = SAMPLING_FREQUENCY/2, color = 'r', label = '', linestyle = '--', linewidth = 1)
