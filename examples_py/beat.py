import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES           = 10000
SIGNAL_FREQUENCY_1      = 10
SIGNAL_FREQUENCY_2      = 12

time = np.linspace(0, 1, NR_OF_SAMPLES)
sig_1 = np.sin(time*2*PI*SIGNAL_FREQUENCY_1)
sig_2 = np.sin(time*2*PI*SIGNAL_FREQUENCY_2)
beat_sig = sig_1 + sig_2
spectrum = np.fft.fft(beat_sig)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)
factor_1_freq = (SIGNAL_FREQUENCY_2 - SIGNAL_FREQUENCY_1)/2
factor_2_freq = (SIGNAL_FREQUENCY_1 + SIGNAL_FREQUENCY_2)/2
factor_1 = np.cos(time*2*PI*factor_1_freq)
factor_2 = np.sin(time*2*PI*factor_2_freq)

RES = 500

my_plot(time, {f'signal 1 ({SIGNAL_FREQUENCY_1}Hz)':sig_1,
               f'signal 2 ({SIGNAL_FREQUENCY_2}Hz)':sig_2},
        leg_ncol = 2, res = RES)


my_plot(time, {'beat':beat_sig}, res = RES)

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

my_plot(freqs, {'dft':spectrum}, stem=True, res = RES)
plt.xlabel('frequency')
plt.ylim(0,25)
plt.xlim(0, SIGNAL_FREQUENCY_2*3/2)
# plt.xticks(np.arange(0,120, step=10))

my_plot(time, {f'factor 1 ({factor_1_freq}Hz)':factor_1,
               f'factor 2 ({factor_2_freq}Hz)':factor_2},
        leg_ncol=2, res = RES)
