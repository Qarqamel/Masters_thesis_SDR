import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt

AMPLITUDE       = 1
FREQUENCY       = 10
PHASE           = 0*PI

time = np.linspace(0, 1, 1000)
sinewave = AMPLITUDE * np.sin(time*2*PI*FREQUENCY + PHASE)

plt.figure(dpi=150)
plt.title('Sinewave')
plt.xlabel('time [s]')
plt.ylim([-5, 5])
plt.grid()
plt.plot(time, sinewave)
plt.show()