import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

NR_OF_SAMPLES = 10000
HIGH_FREQUENCY = 50
IF_FREQUENCY = 40
FILTER_CUTOFF = 20

time = np.linspace(0, 1, NR_OF_SAMPLES)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
# high_freq_signal = np.load('Upconverted_signal.npy')
if_freq_osc = np.sin(2*PI*IF_FREQUENCY*time)
downconverted_signal = high_freq_signal*if_freq_osc
dwncnv_sig_spectrum = np.fft.fft(downconverted_signal)
dwncnv_sig_spectrum = dwncnv_sig_spectrum[0:len(dwncnv_sig_spectrum)//2]
dwncnv_sig_spectrum_abs = np.absolute(dwncnv_sig_spectrum)
comp_sine_1 =  np.cos(2*PI*(HIGH_FREQUENCY-IF_FREQUENCY)*time)
comp_sine_2 = -np.cos(2*PI*(HIGH_FREQUENCY+IF_FREQUENCY)*time)
component_sum = comp_sine_1/2 + comp_sine_2/2
filtered_signal = lpf(downconverted_signal, FILTER_CUTOFF, NR_OF_SAMPLES)
filt_sig_spectrum = np.fft.fft(filtered_signal)
filt_sig_spectrum = filt_sig_spectrum[0:len(filt_sig_spectrum)//2]
filt_sig_spectrum_abs = np.absolute(filt_sig_spectrum)



my_plot(time, {f'high_freq_signal ({HIGH_FREQUENCY}Hz)':high_freq_signal,
               f'if_freq ({IF_FREQUENCY}Hz)':if_freq_osc},
        leg_ncol = 2)
plt.xlim(0, 0.5)


my_plot(time, {'downconverted':downconverted_signal})
plt.xlim(0, 0.5)


freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

my_plot(freqs, {'dft':dwncnv_sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0, 2.5*HIGH_FREQUENCY)
plt.xticks(np.arange(0,2.5*HIGH_FREQUENCY, step=10))


my_plot(freqs, {'dft':dwncnv_sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0,2*(HIGH_FREQUENCY-IF_FREQUENCY))
plt.xticks(np.arange(0,2*(HIGH_FREQUENCY-IF_FREQUENCY), step=2))


my_plot(freqs, {'dft':dwncnv_sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(2*IF_FREQUENCY,2*HIGH_FREQUENCY)
plt.xticks(np.arange(2*IF_FREQUENCY,2*HIGH_FREQUENCY, step=2))


my_plot(time, {f'component 1 ({HIGH_FREQUENCY-IF_FREQUENCY}Hz)':comp_sine_1,
               f'component 2 ({HIGH_FREQUENCY+IF_FREQUENCY}Hz)':comp_sine_2},
        leg_ncol = 2)
plt.xlim(0, 0.5)


my_plot(time, {'component sum':component_sum})
plt.xlim(0, 0.5)


my_plot(time, {'filtered':filtered_signal})
plt.xlim(0, 0.5)


my_plot(freqs, {'dft':filt_sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0, 2.5*HIGH_FREQUENCY)
plt.xticks(np.arange(0,2.5*HIGH_FREQUENCY, step=10))


my_plot(freqs, {'dft':filt_sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0, 2*(HIGH_FREQUENCY-IF_FREQUENCY))
plt.xticks(np.arange(0,2*(HIGH_FREQUENCY-IF_FREQUENCY), step=2))

