import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
NOISE_DEVIATION = [1, 2, 4]
TRANSMISSION_NR = 10

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

for nd in NOISE_DEVIATION:
    AMPL_VECTOR_SIN = ( 1, -1,  1, -1)
    AMPL_VECTOR_COS = ( 1,  1, -1, -1)
    
    # CALCULATION
    t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
    
    carrier_sin = ref_sin = np.sin(t) 
    carrier_cos = ref_cos = np.cos(t) 
    
    amplitudes_sin = list()
    amplitudes_cos = list()
    
    for i in range(TRANSMISSION_NR):
        for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
            
            # modulation
            Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
            
            # real channel
            Rx = Tx + np.random.normal(0, nd, TIME_VECTOR_SIZE)
                
            # demodulation
            ampl = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
            amplitudes_sin.append(ampl)
            
            ampl = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
            amplitudes_cos.append(ampl)
    
    # PRESENTATION  
    # Rx plot
    plt.figure(figsize = [2, 2], dpi=RES)
    plt.grid(alpha=0.3)
    for j in range(40):
        plt.scatter(amplitudes_cos[j], amplitudes_sin[j], color=('red','orange','green','blue')[j%4], marker='.')
    plt.ylabel('sin_ampl.')
    plt.xlabel('cos_ampl.')
    plt.axhline(y=0,color='black', linewidth=0.8)
    plt.axvline(x=0,color='black', linewidth=0.8)
    plt.ylim(-4,4)
    plt.xlim(-4,4)
    plt.yticks(range(-4,5))
    plt.xticks(range(-4,5))
    plt.title(f'dev = {nd}')

