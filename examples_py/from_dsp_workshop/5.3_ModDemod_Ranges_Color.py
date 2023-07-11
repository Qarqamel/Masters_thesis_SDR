import numpy as np
import matplotlib.pyplot as plt
from auxiliary_lib import my_plot

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

pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
# AMPL_VECTOR = (0.5,1,1.5,2,2.5,3,3.5,4)
# AMPL_NR = len(AMPL_VECTOR)
TRANSMISSION_NR = 200
NOISE_DEVIATION = [1.2,1,0.6]

for nd, iter in zip(NOISE_DEVIATION, range(3)):
    AMPL_VECTOR = np.linspace(nd, 4, int(4/nd))
    AMPL_NR = len(AMPL_VECTOR)
    
    # CALCULATION
    t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
    
    ampl_list = [] # create amplitude list
    
    # for number in AMPL_VECTOR:
    for i in range(TRANSMISSION_NR):
        
        Tx_amp = AMPL_VECTOR[i%AMPL_NR]
        
        # modulation
        
        Carrier = np.sin(t)
        Tx = Tx_amp*Carrier
        
        # channel
        Rx=Tx + np.random.normal(0, nd, TIME_VECTOR_SIZE) # ideal one    
        
        # demodulation
                
        Ref  = np.sin(t)     
        dot  = np.dot(Rx, Ref)
        Rx_amp = 2*dot/TIME_VECTOR_SIZE # decode amplitude
        ampl_list.append(Rx_amp) # append amplitude to list
    
    # PRESENTATION  
    plt.figure(figsize = [2, 2.5], dpi=RES)
    # Rx plot
    for i in range(AMPL_NR):
        plt.plot(ampl_list[i::AMPL_NR], 'p')
    plt.axhline(y=0,color='black')
    plt.grid(axis='y')
    plt.title(f'NOISE_DEVIATION = {nd}')
    if iter == 0:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)
    plt.show()
