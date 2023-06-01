import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES           = 10000
SIGNAL_FREQUENCY_1      = 20
SIGNAL_FREQUENCY_2      = 24

time = np.linspace(0, 1, NR_OF_SAMPLES)
sig_1 = np.sin(time*2*PI*SIGNAL_FREQUENCY_1)
sig_2 = np.sin(time*2*PI*SIGNAL_FREQUENCY_2)
beat_sig = sig_1 + sig_2
osc_freq = (SIGNAL_FREQUENCY_1 + SIGNAL_FREQUENCY_2)/2
sig_osc = np.sin(time*2*PI*osc_freq)
amp_chng_freq = (SIGNAL_FREQUENCY_1 - SIGNAL_FREQUENCY_2)/2
sig_amp = 2*np.cos(time*2*PI*amp_chng_freq)


my_plot(time, {f'signal_1 ({SIGNAL_FREQUENCY_1}Hz)':sig_1,
               f'signal_2 ({SIGNAL_FREQUENCY_2}Hz)':sig_2},
        leg_ncol = 2)
plt.show()

my_plot(time, {'beat':beat_sig})
plt.show()

my_plot(time, {'osc':sig_osc, 'amp_chng':sig_amp}, leg_ncol=2)
plt.show()