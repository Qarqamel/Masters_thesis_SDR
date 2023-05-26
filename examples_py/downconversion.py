import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

NR_OF_SAMPLES = 10000
HIGH_FREQUENCY = 50
IF_FREQUENCY = 40
FILTER_CUTOFF = 20

time = np.linspace(0, 1, NR_OF_SAMPLES)
high_freq_signal = np.sin(2*PI*HIGH_FREQUENCY*time)
# high_freq_signal = np.load('Upconverted_signal.npy')
if_freq_osc = np.sin(2*PI*IF_FREQUENCY*time)
downconverted_signal = high_freq_signal*if_freq_osc
dwncnv_sig_spectrum = np.fft.fft(downconverted_signal)
dwncnv_sig_spectrum = dwncnv_sig_spectrum[0:len(dwncnv_sig_spectrum)//2]
dwncnv_sig_spectrum_abs = np.absolute(dwncnv_sig_spectrum)
comp_sine_1 =  np.cos(2*PI*(HIGH_FREQUENCY-IF_FREQUENCY)*time)
comp_sine_2 = -np.cos(2*PI*(HIGH_FREQUENCY+IF_FREQUENCY)*time)
component_sum = comp_sine_1/2 + comp_sine_2/2
filtered_signal = lpf(downconverted_signal, FILTER_CUTOFF, NR_OF_SAMPLES)
filt_sig_spectrum = np.fft.fft(filtered_signal)
filt_sig_spectrum = filt_sig_spectrum[0:len(filt_sig_spectrum)//2]
filt_sig_spectrum_abs = np.absolute(filt_sig_spectrum)

plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('high_freq_signal')
plt.plot(time, high_freq_signal, label='high_freq_signal')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('if_freq')
plt.plot(time, if_freq_osc, label='if_freq')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('downconverted')
plt.plot(time, downconverted_signal, label='downconverted')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

freqs = np.linspace(0, NR_OF_SAMPLES/2, int(NR_OF_SAMPLES/2))

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('dft')
plt.stem(freqs, dwncnv_sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.xlim(0,2*HIGH_FREQUENCY)
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 1')
plt.plot(time, comp_sine_1, label='component 1')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 2')
plt.plot(time, comp_sine_2, label='component 2')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component 1/component 2')
plt.plot(time, comp_sine_1, label='component 1')
plt.plot(time, comp_sine_2, label='component 2')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('component sum')
plt.plot(time, component_sum, label='component sum')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('filtered')
plt.plot(time, filtered_signal, label='filtered')
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.title('dft')
plt.stem(freqs, filt_sig_spectrum_abs, label='dft', basefmt = '')
plt.xlabel('frequency')
plt.xlim(0,2*HIGH_FREQUENCY)
plt.legend(loc = 'lower right', ncol=2, bbox_to_anchor=(1, -0.6))
plt.show()