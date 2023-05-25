import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI

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
comp_freq_1 = HIGH_FREQUENCY-LOW_FREQUENCY
comp_freq_2 = HIGH_FREQUENCY+LOW_FREQUENCY
comp_sine_1 = np.sin(2*PI*comp_freq_1*time)
comp_sine_2 = np.sin(2*PI*comp_freq_2*time)
comp_sum = comp_sine_1/2 + comp_sine_2/2
# np.save('Upconverted_signal', upconverted_signal)

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('signal')
plt.plot(time, low_freq_signal, label='signal')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('carrier')
plt.plot(time, high_freq_carrier, label='carrier')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('upconverted')
plt.plot(time, low_freq_signal, label='signal')
plt.plot(time, upconverted_signal, label='upconverted')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('dft')
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.xlim(0,HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2)
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('dft')
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.xlim(HIGH_FREQUENCY-2*LOW_FREQUENCY,HIGH_FREQUENCY+2*LOW_FREQUENCY)
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 1')
plt.plot(time, comp_sine_1, label='component 1')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 2')
plt.plot(time, comp_sine_2, label='component 2')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 1/component 2')
plt.plot(time, comp_sine_1, linewidth = 1.5, label='component 1')
plt.plot(time, comp_sine_2, linewidth = 1, label='component 2')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component sum')
plt.plot(time, comp_sum, label='component sum')
# plt.plot(time, low_freq_signal, label='signal')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()