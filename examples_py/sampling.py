import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot

SIGNAL_FREQUENCY        = 3
SAMPLING_FREQUENCY      = 4

time_original = np.linspace(0, 1, 10000)
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)

RES = 150

my_plot([time_original, time],
        {f'signal frequency = {SIGNAL_FREQUENCY}':sinewave_original,
         f'sampling frequency = {SAMPLING_FREQUENCY}':sinewave},
        [1, 1.5],
        ['-', '.'], leg_ncol=2, res = RES)

