import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI

NR_OF_SAMPLES = 10000
LOW_FREQUENCY = 5
HIGH_FREQUENCY = 50
time = np.linspace(0, 1, NR_OF_SAMPLES)
low_freq_signal = np.sin(2*PI*LOW_FREQUENCY*time)
high_freq_carrier = np.sin(2*PI*HIGH_FREQUENCY*time)
upconverted_signal = (low_freq_signal+1)*high_freq_carrier
sig_spectrum = np.fft.fft(upconverted_signal)
sig_spectrum = sig_spectrum[0:len(sig_spectrum)//2]
sig_spectrum_abs = np.absolute(sig_spectrum)
print(np.angle(sig_spectrum[HIGH_FREQUENCY-LOW_FREQUENCY]))
print(np.angle(sig_spectrum[HIGH_FREQUENCY]))
print(np.angle(sig_spectrum[HIGH_FREQUENCY+LOW_FREQUENCY]))
component_sine_1 = np.sin(2*PI*(HIGH_FREQUENCY-LOW_FREQUENCY)*time+np.angle(sig_spectrum[HIGH_FREQUENCY-LOW_FREQUENCY]))
component_sine_2 = np.sin(2*PI*HIGH_FREQUENCY*time+np.angle(sig_spectrum[HIGH_FREQUENCY]))
component_sine_3 = np.sin(2*PI*(HIGH_FREQUENCY+LOW_FREQUENCY)*time+np.angle(sig_spectrum[HIGH_FREQUENCY+LOW_FREQUENCY]))
component_sum = component_sine_2 + component_sine_1/2 + component_sine_3/2
# np.save('Upconverted_signal', upconverted_signal)

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, low_freq_signal, label='signal')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, high_freq_carrier, label='carrier')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, low_freq_signal+1, label='signal')
plt.plot(time, upconverted_signal, label='upconverted')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.legend(fontsize = 6, loc = 'lower right')
plt.xlim(0,HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2)
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.legend(fontsize = 6, loc = 'lower right')
plt.xlim(HIGH_FREQUENCY - 2*LOW_FREQUENCY,HIGH_FREQUENCY + 2*LOW_FREQUENCY)
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
plt.plot(time, component_sine_3, label='component 3')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()

plt.figure(figsize = [6.4,1.6], dpi=150)
plt.grid()
plt.plot(time, low_freq_signal+1, label='signal')
plt.plot(time, component_sum, label='component sum')
plt.xlabel('time')
plt.legend(fontsize = 6, loc = 'lower right')
plt.show()