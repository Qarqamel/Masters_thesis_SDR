import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

SAMPLING_FREQUENCY      = 9
ALIAS_FREQUENCY         = 10
PHASE                   = 0

time = np.linspace(0, 1, int(10e4))
signal = np.sin(time*2*PI*(ALIAS_FREQUENCY-SAMPLING_FREQUENCY) + PHASE)
alias = np.sin(time*2*PI*ALIAS_FREQUENCY + PHASE)
time_samples = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sine_samples = np.sin(time_samples*2*PI*ALIAS_FREQUENCY+PHASE)

RES = 150

my_plot([time, time, time_samples],
        {f'signal ({ALIAS_FREQUENCY-SAMPLING_FREQUENCY}Hz)':signal,
         f'alias ({ALIAS_FREQUENCY}Hz)':alias,
         f'samples ({SAMPLING_FREQUENCY}Hz)':sine_samples},
        [1, 1, 1],
        ['-', '-', 'r.'],
        leg_ncol=3,
        res = RES)

