import numpy as np
import matplotlib.pyplot as plt
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

RES = 100

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1,2,0.5)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier = np.sin(t)

Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx,Carrier*amp)

    # PRESENTATION
    plt.figure(figsize = [2, 1.5], dpi=RES)
    plt.plot(Carrier*amp)
    plt.axhline(y=0,color='black',linewidth=0.8)
    plt.ylim(-2.2,2.2)
    if amp == AMPL_VECTOR[0]:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    else: 
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    if amp == AMPL_VECTOR[1]:
        plt.title(f'Tx\n\nAMPL = {amp}')
    else:
        plt.title(f'AMPL = {amp}')
    plt.grid(axis='y')
    plt.show()

# SAVING
np.save('TxSignal',Tx)

