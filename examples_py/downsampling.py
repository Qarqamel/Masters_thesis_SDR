import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot

SIGNAL_FREQUENCY        = 2
SAMPLING_FREQUENCY      = 15

time_original = np.linspace(0, 1, int(10e4))
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
spectrum = np.fft.fft(sinewave_original)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)

samp_freq_list = [60, 30, 20, 15]

RES = 150
DISP_SPECTRUM_SIZE = 30
TIME_LIM = 1

for freq, sign in zip(samp_freq_list, ['< fsamp/2', '= fsamp/2', '> fsamp/2', '= fsamp']):
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    time = np.linspace(0+0.025, 1+0.025, freq+1)
    sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)

    if freq == samp_freq_list[0]:
        my_plot([time_original, time],
                {f'signal)':sinewave_original,
                 f'samples (fs = {freq} Hz)':sinewave},
                [3, 1.5],
                ['-', '.'], leg_ncol=1, res = RES)
        plt.title('original samples', loc = 'left')
    else:
        my_plot([time_original, time],
                {'':sinewave_original,
                 f'samples (fs = {freq} Hz)':sinewave},
                [3, 1.5],
                ['-', '.'], leg_ncol=2, res = RES)
        plt.title(f'downsampled by a factor of {int(samp_freq_list[0]/freq)}', loc = 'left')
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.xlim(0,TIME_LIM)
    plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
    
    
    if freq == samp_freq_list[-1]:
        plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
        plt.xlabel('t')
