import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES   = 10000
LOW_FREQUENCY   = 3
HIGH_FREQUENCY  = 50

time = np.linspace(0, 1, NR_OF_SAMPLES)
low_freq_signal     = np.sin(2*PI*LOW_FREQUENCY*time)
high_freq_carrier   = np.sin(2*PI*HIGH_FREQUENCY*time)
upconverted_signal = low_freq_signal*high_freq_carrier
sig_spectrum = np.fft.fft(upconverted_signal)
sig_spectrum = sig_spectrum[0:len(sig_spectrum)//2]
sig_spectrum_abs = np.absolute(sig_spectrum)
comp_sine_1 =  np.cos(2*PI*(HIGH_FREQUENCY-LOW_FREQUENCY)*time)
comp_sine_2 = -np.cos(2*PI*(HIGH_FREQUENCY+LOW_FREQUENCY)*time)
comp_sum = comp_sine_1/2 + comp_sine_2/2
# np.save('Upconverted_signal', upconverted_signal)


my_plot(time, {f'carrier ({HIGH_FREQUENCY}Hz)':high_freq_carrier,
               f'signal ({LOW_FREQUENCY}Hz)':low_freq_signal},
        leg_ncol = 2)
plt.show()

my_plot(time, {'upconverted':upconverted_signal})
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

my_plot(freqs, {'dft':sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0,HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2)
plt.xticks(list(np.arange(0, HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2, 10))+[HIGH_FREQUENCY-LOW_FREQUENCY,HIGH_FREQUENCY+LOW_FREQUENCY])
plt.show()

my_plot(freqs, {'dft':sig_spectrum_abs}, stem = True)
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(HIGH_FREQUENCY-2*LOW_FREQUENCY,HIGH_FREQUENCY+2*LOW_FREQUENCY)
plt.xticks(np.arange(HIGH_FREQUENCY-2*LOW_FREQUENCY,HIGH_FREQUENCY+2*LOW_FREQUENCY, step=1))
plt.show()

my_plot(time, {f'component 1 ({HIGH_FREQUENCY - LOW_FREQUENCY}Hz)':comp_sine_1,
               f'component 2 ({HIGH_FREQUENCY + LOW_FREQUENCY}Hz)':comp_sine_2},
        leg_ncol = 2)
plt.xlim(0, 0.5)
plt.show()


my_plot(time, {'component sum':comp_sum})
plt.xlim(0, 0.5)
plt.show()
