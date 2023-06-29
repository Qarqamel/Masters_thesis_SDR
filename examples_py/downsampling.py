import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from auxiliary_lib import my_plot,calculate_fft
import scipy.signal

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

SIGNAL_FREQUENCY_1 = 5
SIGNAL_FREQUENCY_2 = 20
ORIGINAL_SAMPLING_FREQ = 100
DECIMATION_FACTOR = 5
FILTER_CUTOFF_FREQUENCY = 10

time_original = np.linspace(0, 1, ORIGINAL_SAMPLING_FREQ+1)
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY_1) + np.sin(time_original*2*PI*SIGNAL_FREQUENCY_2)
spectrum_original = calculate_fft(sinewave_original)
time_decimated = time_original[1::DECIMATION_FACTOR]
sinewave_decimated = sinewave_original[1::DECIMATION_FACTOR]
spectrum_decimated = calculate_fft(sinewave_decimated)

sinewave_filtered = lpf(sinewave_original, FILTER_CUTOFF_FREQUENCY, ORIGINAL_SAMPLING_FREQ)
sinewave_filt_decimated = sinewave_filtered[1::DECIMATION_FACTOR]
spectrum_filt_decimated = calculate_fft(sinewave_filt_decimated)

RES = 150
DISP_SPECTRUM_SIZE = 30
TIME_LIM = 1

my_plot([time_original, time_decimated],
        {f'original samples (fs = {ORIGINAL_SAMPLING_FREQ} Hz)':sinewave_original,
         f'samples decimated by a factor of {DECIMATION_FACTOR} (fs = {round(ORIGINAL_SAMPLING_FREQ/DECIMATION_FACTOR, 1)} Hz)':sinewave_decimated},
        [1.5, 1.5],
        ['C0.', 'C1.'], leg_ncol=1, res = RES)
plt.ylim(-2.2,2.2)
plt.xlim(0,TIME_LIM)
plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.xlabel('t')

spectrum_decimated[0] /= 2
freqs_og = np.linspace(0, (ORIGINAL_SAMPLING_FREQ)/2, int((ORIGINAL_SAMPLING_FREQ)/2))
freqs_dec = freqs_og[0:int((ORIGINAL_SAMPLING_FREQ)/2/DECIMATION_FACTOR)]
my_plot([freqs_og, freqs_dec],
        {'':spectrum_original, ' ':spectrum_decimated*DECIMATION_FACTOR},
        styles = ['C0', 'C1'],
        line_widths = [4, 1.5],
        stem=True, res=RES)
plt.ylim(20,60)
plt.xlim(-1, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=5))+ [SIGNAL_FREQUENCY_1, SIGNAL_FREQUENCY_2])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)
plt.xlabel('f')

my_plot([time_original, time_original, time_decimated],
        {f'original samples (fs = {ORIGINAL_SAMPLING_FREQ} Hz)':sinewave_original,
         f'filtered original samples (fs = {ORIGINAL_SAMPLING_FREQ} Hz)':sinewave_filtered,
         f'samples decimated by a factor of {DECIMATION_FACTOR} (fs = {round(ORIGINAL_SAMPLING_FREQ/DECIMATION_FACTOR, 1)} Hz)':sinewave_filt_decimated},
        [1.5, 1.5, 1.5],
        ['C0.', 'C2.', 'C1.'], leg_ncol=1, res = RES)
plt.ylim(-2.2,2.2)
plt.xlim(0,TIME_LIM)
plt.xticks(list(np.arange(0, TIME_LIM, step=0.1)))
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.xlabel('t')

my_plot([freqs_og, freqs_dec],
        {'':spectrum_original, ' ':spectrum_filt_decimated*DECIMATION_FACTOR},
        styles = ['C0', 'C1'],
        line_widths = [4, 1.5],
        stem=True, res=RES)
plt.ylim(20,60)
plt.xlim(-1, DISP_SPECTRUM_SIZE)
plt.xticks(list(np.arange(0,DISP_SPECTRUM_SIZE, step=5))+ [SIGNAL_FREQUENCY_1, SIGNAL_FREQUENCY_2])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)
plt.axvline(x = FILTER_CUTOFF_FREQUENCY, color = 'r', label = 'filter cutoff frequency', linestyle = '--', linewidth = 1.5)
plt.legend(loc = 'lower center', ncol=1 , bbox_to_anchor=(0.5, 1), framealpha=0)
plt.xlabel('f')
