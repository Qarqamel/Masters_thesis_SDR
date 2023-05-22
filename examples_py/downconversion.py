import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

NR_OF_SAMPLES = 10000
HIGH_FREQUENCY = 50
IF_FREQUENCY = 40
time = np.linspace(0, 1, NR_OF_SAMPLES)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
# high_freq_signal = np.load('Upconverted_signal.npy')
if_freq_sine = np.sin(2*PI*IF_FREQUENCY*time)
downconverted_signal = high_freq_signal*if_freq_sine
dwncnv_sig_spectrum = np.fft.fft(downconverted_signal)
dwncnv_sig_spectrum = dwncnv_sig_spectrum[0:len(dwncnv_sig_spectrum)//2]
dwncnv_sig_spectrum_abs = np.absolute(dwncnv_sig_spectrum)
component_sine_1 = np.sin(2*PI*(HIGH_FREQUENCY-IF_FREQUENCY)*time+PI/2)
component_sine_2 = np.sin(2*PI*(HIGH_FREQUENCY+IF_FREQUENCY)*time)
component_sum = component_sine_1/2 + component_sine_2/2
filtered_signal = lpf(downconverted_signal, 2*(HIGH_FREQUENCY-IF_FREQUENCY), NR_OF_SAMPLES)
filtered_sig_spectrum = np.fft.fft(filtered_signal)
filtered_sig_spectrum = filtered_sig_spectrum[0:len(filtered_sig_spectrum)//2]
filtered_sig_spectrum_abs = np.absolute(filtered_sig_spectrum)

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, high_freq_signal, label='high_freq_signal')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, if_freq_sine, label='if_freq')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, downconverted_signal, label='downconverted')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.stem(freqs, dwncnv_sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.legend(fontsize = 6, loc = 'lower right')
plt.xlim(0,2*HIGH_FREQUENCY)
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, component_sine_1, label='component 1')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, component_sine_2, label='component 2')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, component_sum, label='component sum')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, filtered_signal, label='filtered')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.stem(freqs, filtered_sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.legend(fontsize = 6, loc = 'lower right')
plt.xlim(0,2*HIGH_FREQUENCY)
plt.show()