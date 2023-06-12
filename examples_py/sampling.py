import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot

SIGNAL_FREQUENCY        = 10
SAMPLING_FREQUENCY      = 15

time_original = np.linspace(0, 1, int(10e4))
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
spectrum = np.fft.fft(sinewave_original)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)

samp_freq_list = [70, 40, 15]

RES = 150
DISP_SPECTRUM_SIZE = 100

for freq in samp_freq_list:
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    time = np.linspace(0, 1, freq+1)
    sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
    spectrum = np.fft.fft(sinewave_original)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)

    my_plot([time_original, time],
            {f'signal ({SIGNAL_FREQUENCY} Hz)':sinewave_original,
             f'samples (fs = {freq} Hz)':sinewave},
            [1, 1.5],
            ['-', '.'], leg_ncol=2, res = RES)
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.xlim(0,1)
    
    if freq == samp_freq_list[-1]:
        alias = np.sin(time_original*2*PI*(SIGNAL_FREQUENCY-samp_freq_list[-1]))
        plt.plot(time_original, alias, 'C1--', linewidth = 0.5)
    plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
    plt.xlabel('t')
    
    freqs = np.linspace(0, 10e4/2, int(10e4/2))
    my_plot(freqs, {'':spectrum_abs}, stem=True, res=RES)
    plt.xlabel('f')
    plt.ylim(0,60000)
    plt.xlim(0, DISP_SPECTRUM_SIZE)
    plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY])
    plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
    plt.axvline(x = freq, color = 'r', label = 'sampling frequency', linestyle = '--', linewidth = 1)
    plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)
