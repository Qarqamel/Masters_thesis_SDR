import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

NR_OF_SAMPLES = 10000
HIGH_FREQUENCY = 12
IF_FREQUENCY = 10
FILTER_CUTOFF = 5

time = np.linspace(0, 1, NR_OF_SAMPLES)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
# high_freq_signal = np.load('Upconverted_signal.npy')
if_freq_osc = np.sin(2*PI*IF_FREQUENCY*time)
downconverted_signal = high_freq_signal*if_freq_osc
dwncnv_sig_spectrum = np.fft.fft(downconverted_signal)
dwncnv_sig_spectrum = dwncnv_sig_spectrum[0:len(dwncnv_sig_spectrum)//2]
dwncnv_sig_spectrum_abs = np.absolute(dwncnv_sig_spectrum)
comp_sine_1 =  (1/2) * np.cos(2*PI*(HIGH_FREQUENCY-IF_FREQUENCY)*time)
comp_sine_2 = -(1/2) * np.cos(2*PI*(HIGH_FREQUENCY+IF_FREQUENCY)*time)
component_sum = comp_sine_1 + comp_sine_2
filtered_signal = lpf(downconverted_signal, FILTER_CUTOFF, NR_OF_SAMPLES)
filt_sig_spectrum = np.fft.fft(filtered_signal)
filt_sig_spectrum = filt_sig_spectrum[0:len(filt_sig_spectrum)//2]
filt_sig_spectrum_abs = np.absolute(filt_sig_spectrum)

RES = 150
DISP_SPECTRUM_SIZE = HIGH_FREQUENCY+IF_FREQUENCY+HIGH_FREQUENCY/2

my_plot(time, {f'high_freq_signal ({HIGH_FREQUENCY}Hz)':high_freq_signal,
               f'if_freq ({IF_FREQUENCY}Hz)':if_freq_osc},
        styles = ['C0', 'C2'],
        leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.xlim(0,1)

my_plot(time, {'downconverted signal':downconverted_signal}, res = RES,  styles = ['C8'])
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,1)
plt.xlabel('t')

signals_spectrums = []
for sig in [high_freq_signal, if_freq_osc]:
    spectrum = np.fft.fft(sig)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)
    signals_spectrums.append(spectrum_abs/2)

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))
my_plot(freqs, {'':dwncnv_sig_spectrum_abs,
                ' ':signals_spectrums[0],
                '  ':signals_spectrums[1]},
        stem = True, res = RES,  styles = ['C8', 'C0', 'C2'])
plt.xlabel('f')
plt.ylim(200,3000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {f'{HIGH_FREQUENCY-IF_FREQUENCY}Hz':comp_sine_1,
               f'{HIGH_FREQUENCY+IF_FREQUENCY}Hz':comp_sine_2},
        styles = ['C8', 'C8'],
        leg_ncol = 2, res = RES)
plt.ylim(-1.1,1.1)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,1)
plt.xlabel('t')

my_plot(time, {'downconverted signal':downconverted_signal}, res = RES,  styles = ['C8'])
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,1)
plt.xlabel('t')

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))
my_plot(freqs, {'':dwncnv_sig_spectrum_abs}, stem = True, res = RES,  styles = ['C8'])
plt.xlabel('f')
plt.ylim(200,3000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

fsamp = 10e2
coef_b, coef_a = scipy.signal.butter(1, 2*FILTER_CUTOFF/fsamp, btype='lowpass')
freqs, response = scipy.signal.freqz(coef_b, coef_a, fs=fsamp, include_nyquist=True)
my_plot(freqs, {'Lowpass filter frequency response':response}, styles = ['C4'], res=RES)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10)) + [HIGH_FREQUENCY, IF_FREQUENCY, FILTER_CUTOFF])
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.xlabel('f')

my_plot(time, {'filtered signal':filtered_signal}, res = RES,  styles = ['C1'])
plt.ylim(-1.1,1.1)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,1)
plt.xlabel('t')

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))
my_plot(freqs, {'':filt_sig_spectrum_abs}, stem = True, res = RES,  styles = ['C1'])
plt.xlabel('f')
plt.ylim(200,3000)
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
