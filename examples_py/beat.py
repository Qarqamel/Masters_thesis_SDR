import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES           = 10000
SIGNAL_FREQUENCY_1      = 20
SIGNAL_FREQUENCY_2      = 23

time = np.linspace(0, 1, NR_OF_SAMPLES)
sig_1 = np.sin(time*2*PI*SIGNAL_FREQUENCY_1)
sig_2 = np.sin(time*2*PI*SIGNAL_FREQUENCY_2)
beat_sig = sig_1 + sig_2

my_plot(time, {f'signal_1 ({SIGNAL_FREQUENCY_1}Hz)':sig_1})
plt.show()

my_plot(time, {f'signal_2 ({SIGNAL_FREQUENCY_2}Hz)':sig_2})
plt.show()

my_plot(time, {f'signal_1 ({SIGNAL_FREQUENCY_1}Hz)':sig_1,
               f'signal_2 ({SIGNAL_FREQUENCY_2}Hz)':sig_2},
        leg_ncol = 2)
plt.show()

my_plot(time, {'beat':beat_sig})
plt.show()
