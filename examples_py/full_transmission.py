import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

def calculate_fft(signal):
    spectrum = np.fft.fft(signal)
    spectrum = spectrum[0:len(spectrum)//2]
    return np.absolute(spectrum)

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(1, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

PAYLOAD                     = [0,1,1,0,0,1,0,1,1,1]
DATA_FREQUENCY              = 1
SAMPLES_PER_SEC             = int(10e3)
CARRIER_FREQUENCY           = 20
ADC_THRESHOLD               = 0.2

time = np.linspace(0, len(PAYLOAD)/DATA_FREQUENCY, int(len(PAYLOAD)/DATA_FREQUENCY*SAMPLES_PER_SEC))
freqs = np.linspace(0, SAMPLES_PER_SEC/2, int(SAMPLES_PER_SEC*len(PAYLOAD)/DATA_FREQUENCY/2))

signal = []
for bit in PAYLOAD:
    signal += [bit]*int(SAMPLES_PER_SEC/DATA_FREQUENCY)
signal_spectrum = calculate_fft(signal)

carrier = np.sin(2*PI*CARRIER_FREQUENCY*time)
carrier_spectrum = calculate_fft(carrier)

tx = carrier*signal
tx_spectrum = calculate_fft(tx)

# np.save('OOK_Transmission', tx)
# rx = np.load('OOK_Transmission.npy')

rx = tx

IF_FREQUENCY = 15

dwncnvrtd = rx * np.sin(2*PI*time*IF_FREQUENCY)
dwncnvrtd_spectrum = calculate_fft(dwncnvrtd)

filtered = lpf(dwncnvrtd, 10, SAMPLES_PER_SEC)
filtered_spectrum = calculate_fft(filtered)

SAMPLING_FREQ = 40

time_samp = np.linspace(0, len(PAYLOAD)-1/SAMPLING_FREQ, len(PAYLOAD)*SAMPLING_FREQ)
sampled_cont = filtered
sampled = filtered[0::int(SAMPLES_PER_SEC/SAMPLING_FREQ)]

rectified_cont = np.absolute(filtered)
rectified = np.absolute(sampled)

envelope_cont = lpf(rectified_cont, 2, SAMPLES_PER_SEC)/1.2
envelope = lpf(rectified, 2, SAMPLING_FREQ)

decod_signal_cont = []
for sample in envelope_cont:
    if sample > ADC_THRESHOLD:
        decod_signal_cont.append(1)
    else:
        decod_signal_cont.append(0)
decod_signal = []
for sample in envelope:
    if sample > ADC_THRESHOLD:
        decod_signal.append(1)
    else:
        decod_signal.append(0)

RES = 150
DISP_SPECTRUM_SIZE = 40

my_plot(time, {'Payload':signal}, styles = ['C0'], leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
my_plot(time, {'Payload':signal}, styles = ['C0'], leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)

my_plot(freqs, {'':signal_spectrum},
        stem = True, res = RES,  styles = ['C0'])
plt.xlabel('f')
plt.xlim(-0.1, DISP_SPECTRUM_SIZE)
plt.ylim(0,80000)
# plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {'Carrier':carrier}, styles = ['C0'], leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
my_plot(time, {'Carrier':carrier}, styles = ['C0'], leg_ncol = 2, res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)

my_plot(freqs, {'':carrier_spectrum},
        stem = True, res = RES,  styles = ['C0'])
plt.xlabel('f')
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.ylim(0,60000)
# plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {'Tx':tx}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot(time, {'Tx':tx}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot(freqs, {'':tx_spectrum},
        stem = True, res = RES,  styles = ['C0'])
plt.xlabel('f')
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.ylim(0,40000)
# plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {'Rx':rx}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot(time, {'Rx':rx}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot(time, {'downconverted':dwncnvrtd}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot(time, {'downconverted':dwncnvrtd}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot(freqs, {'':dwncnvrtd_spectrum},
        stem = True, res = RES,  styles = ['C0'])
plt.xlabel('f')
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.ylim(0,20000)
# plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot(time, {'filtered':filtered}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot(time, {'filtered':filtered}, styles = ['C0'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot(freqs, {'':filtered_spectrum},
        stem = True, res = RES,  styles = ['C0'])
plt.xlabel('f')
plt.xlim(0, DISP_SPECTRUM_SIZE)
plt.ylim(0,20000)
# plt.xticks(list(np.arange(0, DISP_SPECTRUM_SIZE, 2))+[HIGH_FREQUENCY-IF_FREQUENCY,HIGH_FREQUENCY+IF_FREQUENCY])
plt.tick_params(left = False, labelleft = False, bottom = True, labelbottom = True)

my_plot([time_samp, time], {'sampled':sampled, '':sampled_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot([time_samp, time], {'sampled':sampled, '':sampled_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot([time_samp, time], {'rectified':rectified, '':rectified_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot([time_samp, time], {'rectified':rectified, '':rectified_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot([time_samp, time], {'envelope':envelope, '':envelope_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot([time_samp, time], {'envelope':envelope, '':envelope_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')

my_plot([time_samp, time], {'decoded':decod_signal, '':decod_signal_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,10)
plt.xlabel('t')
my_plot([time_samp, time], {'decoded':decod_signal, '':decod_signal_cont}, styles = ['C0.', 'C0--'], res = RES)
plt.tick_params(left = True, labelleft = True, bottom = True, labelbottom = True)
plt.xlim(0,2)
plt.xlabel('t')
