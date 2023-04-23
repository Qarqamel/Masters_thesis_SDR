import numpy as np
from matplotlib import pyplot

try:                from itertools import izip
except ImportError: izip = zip
    
x = np.fromfile('F:/mtm/magisterka/rtl-sdr-64bit-20230409/samples.dat', dtype=np.byte)

data = np.ctypeslib.as_array(x)
iq = data.astype(np.float64).view(np.complex128)
iq /= 127.5
iq -= (1 + 1j)

mag = np.absolute(iq)
ang = np.angle(iq)

pyplot.plot(mag, '.')