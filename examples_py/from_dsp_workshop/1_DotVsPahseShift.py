import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

# PARAMETER
PHASE_SHIFT_LIST = np.linspace(0, pi,9, endpoint=True)

dot_list = []

for shift in PHASE_SHIFT_LIST:
    # VECTORS
    t = np.linspace(0, 2*pi,30, endpoint=False)
    
    Ref = np.sin(t)
    Shifted = np.sin(t+shift)
    Ref_mult_Shifted = Ref*Shifted
    dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted
    dot_list.append(dot_product)
    
    #PLOTS (HINT: use separate plots, not one with grid)
    
    # components
    plt.plot(t, Ref, 'p-', color='blue', label='Ref')
    plt.plot(t, Shifted, 'p-', color='green', label='Shifted')
    plt.title('Components')
    plt.grid()
    plt.axhline(y=0,color='black')
    plt.ylim(-1,1)
    plt.legend()
    plt.show()
    
    # multiplication, HINT: use "stem" function for ploting
    plt.stem(t, Ref_mult_Shifted, markerfmt = 'C1o', label='Ref_mult_Shifted')
    plt.title('Multiplication')
    plt.grid()
    plt.axhline(y=0,color='red')
    plt.ylim(-1,1)
    plt.legend()
    plt.show()
    # print phase shift and dot product value
    print(f'phase_shift = {shift : 0.2f}')
    print(f'dot_product = {dot_product : 0.2f}')
    
plt.plot(PHASE_SHIFT_LIST, dot_list, 'p-', color='blue')
plt.title('Dot vs Shift')
plt.xlabel('shift')
plt.ylabel('dot')
plt.grid()
plt.axhline(y=0,color='black')
plt.show()

