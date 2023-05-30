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
comp_sine_1 =  np.cos(2*PI*(HIGH_FREQUENCY-LOW_FREQUENCY)*time)
comp_sine_2 = -np.cos(2*PI*(HIGH_FREQUENCY+LOW_FREQUENCY)*time)
comp_sum = comp_sine_1/2 + comp_sine_2/2
# np.save('Upconverted_signal', upconverted_signal)

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.plot(time, high_freq_carrier, label=f'carrier ({HIGH_FREQUENCY}Hz)')
plt.plot(time, low_freq_signal, label=f'signal ({LOW_FREQUENCY}Hz)')
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.plot(time, upconverted_signal, label='upconverted')
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(0,HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2)
plt.xticks(list(np.arange(0, HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2, 10))+[HIGH_FREQUENCY-LOW_FREQUENCY,HIGH_FREQUENCY+LOW_FREQUENCY])
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.stem(freqs, sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.ylim(0,3000)
plt.xlim(HIGH_FREQUENCY-2*LOW_FREQUENCY,HIGH_FREQUENCY+2*LOW_FREQUENCY)
plt.xticks(np.arange(HIGH_FREQUENCY-2*LOW_FREQUENCY,HIGH_FREQUENCY+2*LOW_FREQUENCY, step=1))
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.plot(time, comp_sine_1, linewidth = 1.5, label=f'component 1 ({HIGH_FREQUENCY - LOW_FREQUENCY}Hz)')
plt.plot(time, comp_sine_2, linewidth = 1.5, label=f'component 2 ({HIGH_FREQUENCY + LOW_FREQUENCY}Hz)')
plt.xlim(0, 0.5)
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.plot(time, comp_sum, label='component sum')
plt.xlim(0,0.5)
plt.legend(loc = 'center', ncol=2 , bbox_to_anchor=(0.5, 1.2))
plt.show()