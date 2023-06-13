import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot

SIGNAL_FREQUENCY        = 10
SAMPLING_FREQUENCY      = 40

time_original = np.linspace(0, 1, int(10e4))
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)
time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)
spectrum = np.fft.fft(sinewave_original)
spectrum = spectrum[0:len(spectrum)//2]
spectrum_abs = np.absolute(spectrum)

sig_freq_list = [10, 20, 35]

RES = 150
DISP_SPECTRUM_SIZE = 50
TIME_LIM = 0.8

for freq, sign in zip(sig_freq_list, ['<', '=', '>']):
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*freq)
    time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
    sinewave = np.sin(time*2*PI*freq)
    spectrum = np.fft.fft(sinewave_original)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)

    if freq == sig_freq_list[0]:
        my_plot([time_original, time],
                {f'signal ({freq} Hz)':sinewave_original,
                 f'samples (fs = {SAMPLING_FREQUENCY} Hz)':sinewave},
                [1, 1.5],
                ['-', '.'], leg_ncol=1, res = RES)
    else:
        my_plot([time_original, time],
                {f'signal ({freq} Hz)':sinewave_original,
                 '':sinewave},
                [1, 1.5],
                ['-', '.'], leg_ncol=2, res = RES)
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.xlim(0,TIME_LIM)
    plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
    plt.title(f'fsig {sign} fsamp/2', loc = 'left')
    
    alias = np.sin(time_original*2*PI*(freq-SAMPLING_FREQUENCY))
    plt.plot(time_original, alias, 'C1--', linewidth = 0.5)
    
    if freq == sig_freq_list[-1]:
        plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
        plt.xlabel('t')

for freq in sig_freq_list:
    time_original = np.linspace(0, 1, int(10e4))
    sinewave_original = np.sin(time_original*2*PI*freq)
    time = np.linspace(0, 1, SAMPLING_FREQUENCY+1)
    sinewave = np.sin(time*2*PI*freq)
    spectrum = np.fft.fft(sinewave_original)
    spectrum = spectrum[0:len(spectrum)//2]
    spectrum_abs = np.absolute(spectrum)
    
    alias = np.sin(time_original*2*PI*(freq-SAMPLING_FREQUENCY))
    spectrum_al = np.fft.fft(alias)
    spectrum_al = spectrum_al[0:len(spectrum_al)//2]
    spectrum_al_abs = np.absolute(spectrum_al)
    
    freqs = np.linspace(0, 10e4/2, int(10e4/2))
    my_plot(freqs, {'':spectrum_abs, ' ':spectrum_al_abs}, styles=['C0', 'C1'], stem=True, res=RES, fig_height=0.6)    
    plt.ylim(0,60000)
    plt.xlim(0, DISP_SPECTRUM_SIZE)
    plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=10))+ [SAMPLING_FREQUENCY] + sig_freq_list + list(abs(SAMPLING_FREQUENCY-np.array(sig_freq_list))))
    plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    if freq == sig_freq_list[0]:
        plt.axvline(x = SAMPLING_FREQUENCY, color = 'r', label = 'sampling frequency', linestyle = '--', linewidth = 1)
        plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)
    else:
        plt.axvline(x = SAMPLING_FREQUENCY, color = 'r', label = '', linestyle = '--', linewidth = 1)
        
    if freq == sig_freq_list[-1]:
        plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
        plt.xlabel('f')