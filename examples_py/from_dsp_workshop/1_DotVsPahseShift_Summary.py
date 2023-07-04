import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

# PARAMETER
PHASE_SHIFT_LIST = np.linspace(0, pi,30, endpoint=True)

dot_list = []

for shift in PHASE_SHIFT_LIST:
    # VECTORS
    t = np.linspace(0, 2*pi,30, endpoint=False)
    
    Ref = np.sin(t)
    Shifted = np.sin(t+shift)
    Ref_mult_Shifted = Ref*Shifted
    dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted
    dot_list.append(dot_product)
    
plt.plot(PHASE_SHIFT_LIST, dot_list, 'p-', color='blue')
plt.title('Dot vs Shift')
plt.xlabel('shift')
plt.ylabel('dot')
plt.grid()
plt.axhline(y=0,color='black')
plt.show()

