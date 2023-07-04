import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (0.5,1,1.5,2,2.5,3,3.5,4)
AMPL_NR = len(AMPL_VECTOR)
TRANSMISSION_NR = 200
NOISE_DEVIATION = 0.5

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
    Rx=Tx + np.random.normal(0, NOISE_DEVIATION, TIME_VECTOR_SIZE) # ideal one    
    
    # demodulation
            
    Ref  = np.sin(t)     
    dot  = np.dot(Rx, Ref)
    Rx_amp = 2*dot/TIME_VECTOR_SIZE # decode amplitude
    ampl_list.append(Rx_amp) # append amplitude to list

# PRESENTATION  

# Rx plot
for i in range(AMPL_NR):
    plt.plot(ampl_list[i::AMPL_NR], 'p')
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.title(f'NOISE_DEVIATION = {NOISE_DEVIATION}')
plt.show()

#  
print(f'received amplitudes: {ampl_list}')

