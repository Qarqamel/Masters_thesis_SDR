import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
pi = np.pi

plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
plt.rc('font', family='Arial')

RES = 500

FIGSIZE=[2,1.5]

t = np.linspace(0, 3*(2*pi),100, endpoint=False)

y_triangle_sum = np.zeros(len(t)) # summaric vector filled with zeros
y_square_sum = np.zeros(len(t)) # summaric vector filled with zeros
y_sine_sum = np.zeros(len(t)) # summaric vector filled with zeros

plt.figure(figsize=FIGSIZE, dpi=RES)
for i, clr in zip(range(3), ['C0', 'C2', 'C6']): # "3' - nr of componenets
    
    # generating random values of phase shift and amplitudes
    # rand function generates single random nr in range from 0 to 1
    phase = np.random.rand()*(2*pi) 
    ampl  = np.random.rand()
    
    # generating different waveforms 
    # select single waveform by comenting the remaining ones
    
    y_triangle = ampl * signal.sawtooth(t+phase,0.5) #triangle
    
    plt.plot(t,y_triangle,'-', color = clr)
    y_triangle_sum += y_triangle

plt.title('Triangle')
plt.ylabel('Componenets')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

plt.figure(figsize=FIGSIZE, dpi=RES)
plt.ylabel('Sum')
plt.plot(t,y_triangle_sum,'C1-')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

plt.figure(figsize=FIGSIZE, dpi=RES)
for i, clr in zip(range(3), ['C0', 'C2', 'C6']): # "3' - nr of componenets
    
    # generating random values of phase shift and amplitudes
    # rand function generates single random nr in range from 0 to 1
    phase = np.random.rand()*(2*pi) 
    ampl  = np.random.rand()
    
    # generating different waveforms 
    # select single waveform by comenting the remaining ones

    y_square = ampl * np.sign(np.sin(t+phase))     # rectangle
    
    plt.plot(t,y_square,'-', color = clr)
    y_square_sum += y_square

plt.title('Rectangle')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

plt.figure(figsize=FIGSIZE, dpi=RES)
plt.plot(t,y_square_sum,'C1-')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

plt.figure(figsize=FIGSIZE, dpi=RES)
for i, clr in zip(range(3), ['C0', 'C2', 'C6']): # "3' - nr of componenets
    
    # generating random values of phase shift and amplitudes
    # rand function generates single random nr in range from 0 to 1
    phase = np.random.rand()*(2*pi) 
    ampl  = np.random.rand()
    
    # generating different waveforms 
    # select single waveform by comenting the remaining ones

    y_sine = ampl * np.sin(t+phase)               # sine
    
    plt.plot(t,y_sine,'-', color = clr)
    y_sine_sum += y_sine

plt.title('Sine')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

plt.figure(figsize=FIGSIZE, dpi=RES) 
plt.plot(t,y_sine_sum,'C1-')
# plt.ylim(-1,1)
plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
plt.show()

