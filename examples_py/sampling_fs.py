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

samp_freq_list = [40, 20, 15, 10]

RES = 150
DISP_SPECTRUM_SIZE = 30
TIME_LIM = 0.8

for freq, sign in zip(samp_freq_list, ['< fsamp/2', '= fsamp/2', '> fsamp/2', '= fsamp']):
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    time = np.linspace(0+0.025, 1+0.025, freq+1)
    sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
    spectrum = np.fft.fft(sinewave_original)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)

    if freq == samp_freq_list[0]:
        my_plot([time_original, time],
                {f'signal ({SIGNAL_FREQUENCY} Hz)':sinewave_original,
                 f'samples (fs = {freq} Hz)':sinewave},
                [3, 1.5],
                ['-', '.'], leg_ncol=1, res = RES, fig_height=0.6)
    else:
        my_plot([time_original, time],
                {'':sinewave_original,
                 f'samples (fs = {freq} Hz)':sinewave},
                [3, 1.5],
                ['-', '.'], leg_ncol=2, res = RES, fig_height=0.6)
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.xlim(0,TIME_LIM)
    plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
    plt.title(f'fsig {sign}', loc = 'left')

    if (freq == SIGNAL_FREQUENCY):
        alias = np.sin(np.full_like(time_original, time[0])*2*PI*SIGNAL_FREQUENCY)
    elif (SIGNAL_FREQUENCY>freq/2):
        alias = np.sin(time_original*2*PI*(freq-SIGNAL_FREQUENCY)+PI*1/4)
    else:
        alias = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    plt.plot(time_original, alias, 'C1--', linewidth = 1)
    
    if freq == samp_freq_list[-1]:
        plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
        plt.xlabel('t')

for freq in samp_freq_list:
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    time = np.linspace(0, 1, freq+1)
    sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
    spectrum = np.fft.fft(sinewave_original)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)
    
    if (freq == SIGNAL_FREQUENCY):
        alias = np.sin(np.full_like(time_original, time[0])*2*PI*SIGNAL_FREQUENCY)
    elif (SIGNAL_FREQUENCY>freq/2):
        alias = np.sin(time_original*2*PI*(freq-SIGNAL_FREQUENCY)+PI*1/4)
    else:
        alias = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
    spectrum_al = np.fft.fft(alias)
    spectrum_al = spectrum_al[0:len(spectrum_al)//2]
    spectrum_al_abs = np.absolute(spectrum_al)
    
    if freq == SIGNAL_FREQUENCY:
        spectrum_al_abs[0] = 50000
    
    freqs = np.linspace(0, 10e4/2, int(10e4/2))
    my_plot(freqs, {'':spectrum_abs, ' ':spectrum_al_abs},
            styles=['C0', 'C1'], line_widths = [6, 3], stem=True, res=RES, fig_height=0.6)    
    plt.ylim(10000,60000)
    plt.xlim(0, DISP_SPECTRUM_SIZE)
    plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SIGNAL_FREQUENCY] + list(np.array(samp_freq_list)/2) + list(abs(np.array(samp_freq_list)-SIGNAL_FREQUENCY)))
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    if freq == samp_freq_list[0]:
        plt.axvline(x = freq/2, color = 'r', label = 'sampling frequency/2', linestyle = '--', linewidth = 1.5)
        plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)
    else:
        plt.axvline(x = freq/2, color = 'r', label = '', linestyle = '--', linewidth = 1.5)
        
    if freq == samp_freq_list[-1]:
        plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
        plt.xlabel('f')
