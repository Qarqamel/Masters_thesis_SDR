import os
import numpy as np
from matplotlib import pyplot as plt
from my_serial import my_serial,read,writeln

def samples_from_file_to_iq(filepath):
    data = np.fromfile(filepath, dtype=np.byte)
    data = np.ctypeslib.as_array(data)
    iq = data.astype(np.float64).view(np.complex128)
    iq /= 127.5
    iq -= (1 + 1j)
    return iq

# Parameters

# REGENERATE_SAMPLES - skips the transmission and reception steps and only performs visualization of previous data when False
REGENERATE_SAMPLES  = True

# SIGNAL_FREQUENCY - adjust the frequency of signal to be transmitted
# possible values:
# 300 - 10K bps  :  3333 - 100 us for AM
# 0.5 - 30 ksps  :  5000 - 33 us for FM
SIGNAL_FREQUENCY    = 1000

# SIGNAL_DATA - signal data to be transmitted. Must be a string of ones and zeros
SIGNAL_DATA         = "0110100110"

# TUNER_FREQUENCY - choose SDR's tuner frequency
TUNER_FREQUENCY     = 433920000

# SAMPLING_FREQUENCY - choose SDR's sampling frequency
# possible values:
# 225001-300000 or 900001-3200000 sps
SAMPLING_FREQUENCY  = 250000

# GAIN - set SDR's gain (0 for auto)
GAIN                = 0

# SAMPLE_NR - number of samples to be captured by SDR
SAMPLE_NR           = 50000

# path to the file with sample data
samples_filepath = r'..\samples\samples_freq_' + f'{TUNER_FREQUENCY/1e6}GHz_samp_{SAMPLING_FREQUENCY/1e3}kHz.dat'

# Transmission
if REGENERATE_SAMPLES:
    
    # initialization of the transmission, by sending frequency and data to Arduino with tx module
    with my_serial(3) as sr:
        print(read(sr))        
        writeln(sr, str(SIGNAL_FREQUENCY))
        
        print(read(sr))        
        writeln(sr, SIGNAL_DATA)

    # reception with SDR, using rtl_sdr
    os.system(r'..\..\rtl-sdr-64bit-20230409\rtl_sdr ' + 
              f'-g {GAIN} ' +
              f'-f {TUNER_FREQUENCY} ' +
              f'-s {SAMPLING_FREQUENCY} ' + 
              f'-n {SAMPLE_NR} ' + 
              samples_filepath)

# read samples from file
samples_iq = samples_from_file_to_iq(samples_filepath)
sample_set_size = len(samples_iq)

# Calculate magnitude and angle from compelx samples
magnitude = np.absolute(samples_iq)
angle = np.angle(samples_iq)

# Create time vector
t = np.linspace(0, sample_set_size/SAMPLING_FREQUENCY, sample_set_size)

plt.plot(t, magnitude, '-', label='samples')
plt.legend()
plt.title('Samples')
plt.xlabel('time [s]')
#plt.axvline(x=0.00282, color='r', linestyle='--')
#plt.xlim(0.0016, 0.0040) # 0.0024
plt.grid()
plt.show()

# Calculate fft
sig_spectrum = np.fft.fft(samples_iq)
sig_spectrum = np.concatenate((sig_spectrum[int(sample_set_size/2):], sig_spectrum[1:int(sample_set_size/2)]))
sig_spectrum_abs = np.absolute(sig_spectrum)

# Create frequencies vector
freqs = np.linspace(TUNER_FREQUENCY - SAMPLING_FREQUENCY/2, TUNER_FREQUENCY + SAMPLING_FREQUENCY/2, sample_set_size-1)

plt.axvline(x=TUNER_FREQUENCY, color='r', linestyle='--')
plt.plot(freqs, sig_spectrum_abs)
plt.title('FFT')
plt.xlabel('Frequency [Hz]')
plt.grid()
#plt.ylim(0, 8000)
plt.show()


