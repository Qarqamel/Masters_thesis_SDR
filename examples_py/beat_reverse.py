import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES           = 10000
SIGNAL_FREQUENCY_1      = 1
SIGNAL_FREQUENCY_2      = 10

time = np.linspace(0, 1, NR_OF_SAMPLES)
sig_1 = np.sin(time*2*PI*SIGNAL_FREQUENCY_1)
sig_2 = np.sin(time*2*PI*SIGNAL_FREQUENCY_2)
beat_sig = sig_1 * sig_2
spectrum = np.fft.fft(beat_sig)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)
component_1_freq = (SIGNAL_FREQUENCY_2 - SIGNAL_FREQUENCY_1)
component_2_freq = (SIGNAL_FREQUENCY_1 + SIGNAL_FREQUENCY_2)
component_1 = (1/2) * np.cos(time*2*PI*component_1_freq)
component_2 = (1/2) * np.cos(time*2*PI*component_2_freq)

RES = 150

my_plot(time, {f'{SIGNAL_FREQUENCY_1} Hz':sig_1,
               f'{SIGNAL_FREQUENCY_2} Hz':sig_2},
        styles = ['C0', 'C2'],
        leg_ncol = 2, res = RES)
plt.xlim(0,1)
plt.ylim(-1.1,1.1)
plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)

my_plot(time, {f'{SIGNAL_FREQUENCY_1} Hz * {SIGNAL_FREQUENCY_2} Hz':beat_sig}, styles = ['C1'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,1)
plt.xlabel('t')

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

my_plot(freqs, {'':spectrum_abs}, styles = ['C1'], stem=True, res = RES)
plt.xlabel('f')
plt.ylim(200,3000)
plt.xlim(0, SIGNAL_FREQUENCY_2*3/2)
plt.xticks(list(np.arange(0,SIGNAL_FREQUENCY_2*3/2, step=2))+[SIGNAL_FREQUENCY_2 - SIGNAL_FREQUENCY_1, SIGNAL_FREQUENCY_2 + SIGNAL_FREQUENCY_1])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {f'{int(component_1_freq)} Hz':component_1,
               f'{int(component_2_freq)} Hz':component_2},
        styles = ['C4', 'C9'],
        leg_ncol=2, res = RES)
plt.xlim(0,1)
plt.ylim(-1.1,1.1)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlabel('t')
