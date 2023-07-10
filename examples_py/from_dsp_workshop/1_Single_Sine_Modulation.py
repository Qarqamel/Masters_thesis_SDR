import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1,2,0.5,-1,-2)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier = np.sin(t)

Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx,Carrier*amp)

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

# PRESENTATION
plt.figure(dpi=RES)
plt.plot(Tx)
plt.axhline(y=0,color='black')
plt.title('Tx')
plt.grid(axis='y')
plt.show()

# SAVING
np.save('TxSignal',Tx)

