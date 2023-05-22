import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

SAMPLING_FREQ = 10000
TIME = 1
FREQ_L = 5
FREQ_H = 50
FREQ_IF = 40

time = np.linspace(0, TIME, SAMPLING_FREQ*TIME)

sine_l = np.sin(2*PI*FREQ_L*time)+1
sine_h = np.sin(2*PI*FREQ_H*time)

sine_shifted = (sine_l)*sine_h

plt.plot(time, sine_l)
plt.show()

plt.plot(time, sine_h)
plt.show()

plt.plot(time, sine_l)
plt.plot(time, sine_shifted)
plt.show()



sig_spectrum = np.fft.fft(sine_shifted)
sig_spectrum = sig_spectrum[0:int(SAMPLING_FREQ*TIME/2)]
sig_spectrum_abs = np.absolute(sig_spectrum)
freqs = np.linspace(0, SAMPLING_FREQ/2, int(SAMPLING_FREQ/2*TIME))

sine_1 = np.sin(2*PI*(FREQ_H-FREQ_L)*time+np.angle(sig_spectrum[FREQ_H-FREQ_L]))
sine_2 = np.sin(2*PI*FREQ_H*time+np.angle(sig_spectrum[FREQ_H]))
sine_3 = np.sin(2*PI*(FREQ_H+FREQ_L)*time+np.angle(sig_spectrum[FREQ_H+FREQ_L]))
plt.plot(time, sine_1)
plt.show()
plt.plot(time, sine_2)
plt.show()
plt.plot(time, sine_3)
plt.show()
plt.plot(time, sine_1/2+sine_3/2+sine_2)
plt.show()

plt.stem(freqs, sig_spectrum_abs)
plt.xlim(0,100)
plt.show()

sine_if = np.sin(2*PI*FREQ_IF*time)
sine_unshifted = sine_shifted*sine_if
sine_lpf = lpf(sine_unshifted, 30, SAMPLING_FREQ)
plt.plot(sine_lpf)
plt.show()
sig_spectrum = np.fft.fft(sine_lpf)
# sig_spectrum = sig_spectrum[0:int(SAMPLING_FREQ*TIME/2)]
sig_spectrum_abs = np.absolute(sig_spectrum)
freqs = np.linspace(0, SAMPLING_FREQ/2, int(SAMPLING_FREQ/2*TIME))
plt.stem(sig_spectrum_abs)
plt.xlim(0,100)
plt.show()




