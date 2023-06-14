import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES   = 10000
LOW_FREQUENCY   = 1
HIGH_FREQUENCY  = 10

time = np.linspace(0, 1, NR_OF_SAMPLES)
low_freq_signal     = np.sin(2*PI*LOW_FREQUENCY*time)
high_freq_carrier   = np.sin(2*PI*HIGH_FREQUENCY*time)
upconverted_signal = low_freq_signal*high_freq_carrier
sig_spectrum = np.fft.fft(upconverted_signal)
sig_spectrum = sig_spectrum[0:len(sig_spectrum)//2]
sig_spectrum_abs = np.absolute(sig_spectrum)
comp_sine_1 =  (1/2) * np.cos(2*PI*(HIGH_FREQUENCY-LOW_FREQUENCY)*time)
comp_sine_2 = -(1/2) * np.cos(2*PI*(HIGH_FREQUENCY+LOW_FREQUENCY)*time)
comp_sum = comp_sine_1 + comp_sine_2
# np.save('Upconverted_signal', upconverted_signal)

RES = 150

my_plot(time, {f'carrier ({HIGH_FREQUENCY}Hz)':high_freq_carrier,
               f'signal ({LOW_FREQUENCY}Hz)':low_freq_signal},
        styles = ['C2', 'C0'],
        leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.xlim(0,1)

my_plot(time, {f'upconverted signal        sin({LOW_FREQUENCY}t) * sin({HIGH_FREQUENCY}t) = sin({HIGH_FREQUENCY-LOW_FREQUENCY}t) + sin({HIGH_FREQUENCY+LOW_FREQUENCY}t)':upconverted_signal}, styles = ['C1'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
plt.xlim(0,1)

my_plot(time, {f'{HIGH_FREQUENCY - LOW_FREQUENCY}Hz':comp_sine_1,
               f'{HIGH_FREQUENCY + LOW_FREQUENCY}Hz':comp_sine_2},
        styles = ['C4', 'C9'],
        leg_ncol = 2, res = RES)
plt.xlim(0,1)
plt.ylim(-1.1,1.1)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlabel('t')

signals_spectrums = []
for sig in [low_freq_signal, high_freq_carrier, 2*comp_sine_1, 2*comp_sine_2]:
    spectrum = np.fft.fft(sig)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)
    signals_spectrums.append(spectrum_abs)

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))
my_plot(freqs, {'':sig_spectrum_abs*2,
                ' ':signals_spectrums[0],
                '  ':signals_spectrums[1],
                '   ':signals_spectrums[2],
                '    ':signals_spectrums[3]},
        styles = ['C1', 'C0','C2', 'C4', 'C9'],
        line_widths = [4, 1.5, 1.5, 1.5, 1.5],
        stem = True, res = RES)
plt.xlabel('f')
plt.ylim(500,6000)
plt.xlim(0,HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2)
plt.xticks(list(np.arange(0, HIGH_FREQUENCY+LOW_FREQUENCY+HIGH_FREQUENCY/2, 2))+[HIGH_FREQUENCY, LOW_FREQUENCY, HIGH_FREQUENCY-LOW_FREQUENCY,HIGH_FREQUENCY+LOW_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
