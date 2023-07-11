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
AMPL_VECTOR = (1.5, 0.5, 2.5)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ampl_list = [] # create amplitude list

for number in AMPL_VECTOR:
    
    # modulation
    
    Carrier = np.sin(t)
    Tx = Carrier*number
    
    # channel
    Rx=Tx + np.random.normal(0, 0.2, TIME_VECTOR_SIZE) # ideal one    
    
    # demodulation
            
    Ref  = np.sin(t)     
    dot  = np.dot(Rx, Ref)
    ampl = 2*dot/TIME_VECTOR_SIZE # decode amplitude
    ampl_list.append(ampl) # append amplitude to list

    # errors_list = np.array(ampl_list) - AMPL_VECTOR

# PRESENTATION  

    if number == AMPL_VECTOR[0]:
        plt.figure(figsize = [6.4, 2.4], dpi=RES)
        plt.plot(Rx)
        plt.axhline(y=0,color='black', linewidth = 0.8)
        plt.ylim(-2.2,2.2)
        plt.grid(axis='y')
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
        plt.show()

# Rx plot
    plt.figure(figsize = [2, 1.5], dpi=RES)
    plt.plot(Rx)
    plt.axhline(y=0,color='black', linewidth = 0.8)
    for ln in (-3,-2,-1,1,2,3):    
        plt.axhline(y=ln, linestyle='--', linewidth = 0.7, color='black')
    plt.ylim(-3.2,3.2)
    # plt.grid(axis='y')
    if number == AMPL_VECTOR[0]:
        plt.tick_params(left = True, labelleft = True, bottom = False, labelbottom = False)
    else:
        plt.tick_params(left = False, labelleft = False, bottom = False, labelbottom = False)

    plt.show()



