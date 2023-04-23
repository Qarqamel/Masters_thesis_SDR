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

regenerate_samples = True

# signal frequency
# 300 - 10K bps  :  3333 - 100 us for AM
# 0.5 - 30 ksps  :  5000 - 33 us for FM
sig_freq        = 1000
sig_data        = "0110100110"

tune_freq       = 433920000
# sampling frequency
# 225001-300000 or 900001-3200000 sps
sampling_freq   = 2048000
sample_nr       = 50000

samples_filepath = r'..\samples\samples_freq_' + f'{tune_freq/1e6}GHz_samp_{sampling_freq/1e3}kHz.dat'

if regenerate_samples:
    with my_serial(3) as sr:
        print(read(sr))        
        writeln(sr, str(sig_freq))
        
        print(read(sr))        
        writeln(sr, sig_data)

    os.system(r'..\..\rtl-sdr-64bit-20230409\rtl_sdr '+
              f'-f {tune_freq} ' +
              f'-s {sampling_freq} ' + 
              f'-n {sample_nr} ' + 
              samples_filepath)

samples_iq = samples_from_file_to_iq(samples_filepath)
sample_set_size = len(samples_iq)

mag = np.absolute(samples_iq)
ang = np.angle(samples_iq)

t = np.linspace(0, sample_set_size/sampling_freq, sample_set_size)

plt.plot(t, mag, '.')
plt.title('Samples')
plt.xlabel('time [s]')
plt.grid()
plt.show()

sig_spectrum = np.fft.fft(samples_iq)
sig_spectrum = np.concatenate((sig_spectrum[int(sample_set_size/2):], sig_spectrum[1:int(sample_set_size/2)]))
sig_spectrum_abs = np.absolute(sig_spectrum)

freqs = np.linspace(tune_freq - sampling_freq, tune_freq + sampling_freq, sample_set_size-1)

plt.plot(freqs, sig_spectrum_abs)
plt.title('FFT')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.ylim(0, 5000)
plt.show()


