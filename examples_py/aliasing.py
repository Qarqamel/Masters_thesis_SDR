import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

SAMPLING_FREQUENCY      = 9
SIGNAL_FREQUENCY        = 10
PHASE                   = 0

time = np.linspace(0, 1, int(10e4))
signal = np.sin(time*2*PI*SIGNAL_FREQUENCY + PHASE)
alias_frequency = SIGNAL_FREQUENCY-SAMPLING_FREQUENCY
alias = np.sin(time*2*PI*alias_frequency + PHASE)
time_samples = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sine_samples = np.sin(time_samples*2*PI*SIGNAL_FREQUENCY+PHASE)

samp_freq_list = [25, 22, 20, 20, 18, 15, 9]
ph_list = [0,0,0,PI/6,0,0,0]

RES = 150
for freq, ph in zip(samp_freq_list, ph_list):
    time = np.linspace(0, 1, int(10e4))
    signal = np.sin(time*2*PI*SIGNAL_FREQUENCY + ph)
    alias_frequency = SIGNAL_FREQUENCY-freq
    alias = np.sin(time*2*PI*alias_frequency + ph)
    time_samples = np.linspace(0, 1, freq+1)
    sine_samples = np.sin(time_samples*2*PI*SIGNAL_FREQUENCY+ph)

    my_plot([time, time, time_samples],
            {f'signal ({SIGNAL_FREQUENCY}Hz)':signal,
             f'alias ({abs(alias_frequency)}Hz)':alias,
             f'samples ({freq}Hz)':sine_samples},
            [1.5, 0.5, 1],
            ['C0-', 'C1--', 'r.'],
            leg_ncol=3,
            res = RES)
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.legend(loc = 'lower center', ncol=3 , bbox_to_anchor=(0.5, 0.9), framealpha=0.3, fontsize = 6)
